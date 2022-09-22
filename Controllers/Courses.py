from random import shuffle
from flask import render_template, request, redirect, jsonify, url_for
from Helper.database import Database

from Helper.helper import checkAuth, findLocate, loadSite
from Models.Courses import Course

coursedb = Database("Courses")

def index():
    if checkAuth(request.cookies.get("_accessToken")) == 0:
        return redirect(url_for('users_router.SignIn'))
    course = coursedb.select()
    return loadSite("Dashboard.html", title="Courses Detail", data={"courses": course})

def getQuestions(cid, maxLength = 25):
    result = []
    root_answer = []
    questions = Database("Questions").select({"cid": cid})
    answers = Database("Answers")
    for question in questions:
        ans = {
            "qid": question['id'],
            "title": question['title'],
            "answers": {}
        }
        for ans_id in question['answers'].split(", "):
            ans['answers'] = answers.select({"id": ans_id}, 1)[0]
            root_answer.append(ans.copy())
    del questions
    del answers
    tmp = []
    i = ind = 0
    for question in root_answer:
        if question['qid'] in tmp:
            continue
        ques = {
            "id": question['qid'],
            "title": question['title'],
            "a":[{"id": question['answers']['id'], "a": question['answers']['ans'], "i": ind}],
            "c": question['answers']['id'],
        }
        ind += 1
        for ans in root_answer:
            if len(ques['a']) == 4:
                break
            shuffle(root_answer)
            if question['qid'] != ans['qid']:
                ques['a'].append({"id": ans['answers']['id'], "a": ans['answers']['ans'], "i": ind})
                ind += 1
        shuffle(ques['a'])
        result.append(ques.copy())
        tmp.append(question['qid'])
        i += 1
        if i == maxLength:
            break
    del tmp
    del root_answer
    return result

def checkCorrect(answers = []):
    cor = 0
    for x in answers:
        question = Database("Questions").select({"id": x['qid']}, 1)
        if question is None:
            continue

        if x['aid'] in question[0]['answers'].split(", "):
            cor += 1
    score = cor * 10 / len(answers)
    return "{:.1f}".format(score)
    


def insert():
    if checkAuth(request.cookies.get("_accessToken")) == 0:
        return redirect(url_for('users_router.SignIn'))
    status = -1
    if request.method == "POST":
        course = request.form['name']
        image = request.form['img']
        tags = request.form['tags']
        db = coursedb
        course = Course(course, image, tags)
        course = course.serialize()
        status = 0
        if db.insert(course):
            status = 1
    tags = Database("Tags").select()
    return loadSite("AddCourse.html", status=status, data={"course":request.form, "tags": tags})

def takeExam(id):
    if checkAuth(request.cookies.get("_accessToken")) == 0:
        return redirect(url_for('users_router.SignIn'))
    score = None
    if request.method == "POST":
        questions = []
        for x in request.form:
            questions.append({"qid": x, "aid": request.form[x]})
        score = checkCorrect(questions)
        del questions
        
    exam = coursedb.select({"id": id}, 1)
    if len(exam) == 0:
        return redirect("/courses")
    title = exam[0]['name']
    questions = getQuestions(exam[0]['id'])
    if len(exam[0]['child']) != 0:
        list_questions = []
        for x in exam[0]['child']:
            for y in getQuestions(x['id']):
                list_questions.append(y)
        questions = list_questions
    del exam
    return loadSite("Exam.html", title, data={"questions": questions, "score": score})

def getAnswers(questions = []):
    db_answers = Database("Answers")

    for i, question in enumerate(questions):
        ans_arr = question['answers'].split(", ")
        ans_ = []
        for ans in ans_arr:
            answers = db_answers.select({"id": ans}, 1)
            if len(answers) == 0:
                continue
            ans_.append(answers[0])
        questions[i]['answers'] = ans_.copy()
    
    return questions

def viewCourse(id):
    if checkAuth(request.cookies.get("_accessToken")) == 0:
        return redirect(url_for('users_router.SignIn'))
    try:
        course = coursedb.select({"id": id})[0]
        questions = Database("Questions").select()
        questions = getAnswers(questions)
        return loadSite("CourseDetail.html", course['name'], data={"course":course,"questions":questions})
    except:
        return redirect("/courses")

def deleteCourse(id):
    if checkAuth(request.cookies.get("_accessToken")) == 0:
        return redirect(url_for('users_router.SignIn'))
    coursedb.delete({"id": int(id)})
    return redirect("/")

def addLesson(id):
    if checkAuth(request.cookies.get("_accessToken")) == 0:
        return redirect(url_for('users_router.SignIn'))
    status = -1
    if request.method == "POST":
        course = request.form['name']
        image = request.form['img']
        tags = request.form['tags']
        db = coursedb
        course = Course(course, image, tags)
        course = course.serialize()
        root_course = Database("Courses").select({"id": id})
        if len(root_course) == 0:
            return redirect(url_for('courses_router.index'))
        root_course[0]['child'].append(course)
        status = 0
        if Database("Courses").update(root_course[0], {"id": id}):
            status = 1
    tags = Database("Tags").select()
    return loadSite("AddCourse.html", "Add Lesson", status=status, data={"course":request.form, "tags": tags})

def deleteLesson(id, lid):
    try:
        course = coursedb.select({"id": id}, 1)[0]
        i = findLocate(course['child'], {"id": lid})
        del course['child'][i]
        coursedb.update(course, {"id": id})
        return redirect(url_for("courses_router.index")+"view/"+id)
    except:
        return redirect(url_for("courses_router.index")+"view/"+id)

def learnLesson(id, lid):
    try:
        questions = []
        course = coursedb.select({"id": id}, 1)[0]
        i = findLocate(course['child'], {"id": lid})
        lesson = course['child'][i]
        questions = Database("Questions").select({"cid": lesson['id']})
        questions = getAnswers(questions)
        return loadSite("Learn.html", course['name'], data={'lesson': lesson, 'questions': questions, "length": len(questions)})
    except:
        return redirect(url_for("courses_router.index")+"view/"+id)
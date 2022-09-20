from flask import request, redirect
from Helper.helper import loadSite
from Helper.database import Database
from Models.Answers import Answers
from Models.Questions import Question
def index():
    return "Question for course"

def addQuestionCourse(cid):
    cid = int(cid)
    if request.method == 'POST':
        topic = request.form['topic']
        title = request.form['title']
        answers = request.form['ans']
        ans_id = checkAnswers(answers, topic)
        Database("Questions").insert(Question(title, ans_id, topic, cid).serialize())

    course = Database("Courses").select({"id": cid})[0]
    question = Database("Questions").select({"cid": cid})
    for q in question:
        q['answers'] = q['answers'].split(", ")
        for i, an in enumerate(q['answers']):
            an = Database("Answers").select({"id": an}, 1)[0]
            q['answers'][i] = an['ans']
        q['answers'] = ", ".join(q['answers'])
    return loadSite("AddQuestion.html", data={"course": course, "questions": question})

def checkAnswers(answers, topic):
    result = ""
    ans = answers.split(",")
    for an in ans:
        an = an.strip()
        answer = Database("Answers")
        ans = answer.select({"ans": an, "topic": topic})
        if len(ans) == 0:
            ans = Answers(an, topic).serialize()
            answer.insert(ans)
        else:
            ans = ans[0]
        result += "{}, ".format(ans["id"])
    result = result[:-2]
    return result

def deleteQuestionCourse(qid, cid):
    ques_db = Database("Questions")
    question = ques_db.select({"id": qid}, 1)
    if len(question) == 0:
        return redirect("/questions/add/"+cid)
    answer = Database("Answers")
    for ans_id in question[0]['answers'].split(", "):
        answer.delete({"id": ans_id})
    ques_db.delete({"id": qid})
    return redirect("/questions/add/"+cid)
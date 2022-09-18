from flask import request
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
        checkAnswers(answers, topic)
        Database("Questions").insert(Question(title, answers, topic, cid).serialize())

    course = Database("Courses").select({"id": cid})[0]
    question = Database("Questions").select({"cid": cid})
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
    return result
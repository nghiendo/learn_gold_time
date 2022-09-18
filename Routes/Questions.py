from flask import Blueprint
from Controllers.Questions import index, addQuestionCourse

question_router = Blueprint("question_router", __name__)
question_router.route("/", methods=['GET'])(index)
question_router.route("/add/<cid>", methods=['GET', 'POST'])(addQuestionCourse)

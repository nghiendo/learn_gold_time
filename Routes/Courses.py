from flask import Blueprint

from Controllers.Courses import deleteCourse, index, insert, takeExam, viewCourse, addLesson, deleteLesson, learnLesson
courses_router = Blueprint("courses_router", __name__)
courses_router.route("/", methods=['GET'])(index)
courses_router.route("/add", methods=['GET', 'POST'])(insert)
courses_router.route("/add/<id>", methods=['GET', 'POST'])(addLesson)
courses_router.route("/view/<id>", methods=['GET'])(viewCourse)
courses_router.route("/learn/<id>/<lid>", methods=['GET'])(learnLesson)
courses_router.route("/delete/<id>", methods=['GET'])(deleteCourse)
courses_router.route("/delete/<id>/<lid>", methods=['GET'])(deleteLesson)
courses_router.route("/exam/<id>", methods=['GET', 'POST'])(takeExam)

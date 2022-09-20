from flask import Blueprint

from Controllers.Courses import deleteCourse, index, insert, takeExam, viewCourse
courses_router = Blueprint("courses_router", __name__)
courses_router.route("/", methods=['GET'])(index)
courses_router.route("/add", methods=['GET', 'POST'])(insert)
# courses_router.route("/view/<id>", methods=['GET'])(viewCourse)
# courses_router.route("/delete/<id>", methods=['GET'])(deleteCourse)
# courses_router.route("/exam/<id>", methods=['GET', 'POST'])(takeExam)

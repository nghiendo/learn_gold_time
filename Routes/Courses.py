from flask import Blueprint

from Controllers.Courses import index, insert, viewCourse
courses_router = Blueprint("courses_router", __name__)
courses_router.route("/", methods=['GET'])(index)
courses_router.route("/view/<id>", methods=['GET'])(viewCourse)
courses_router.route("/add", methods=['GET', 'POST'])(insert)

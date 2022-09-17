from flask import Blueprint

from Controllers.Courses import index
courses_router = Blueprint("courses_router", __name__)
courses_router.route("/", methods=['GET'])(index)
from ast import Delete
from flask import Flask
from Routes.Courses import courses_router
from Routes.Users import users_router
from Routes.Questions import question_router
from Routes.Tags import tags_router
from Routes.Delete import delete_router

app = Flask(__name__)
app.config.from_object("config")
app.secret_key = "NguyenKhoaLearn"

app.register_blueprint(courses_router, url_prefix="/api/courses")
app.register_blueprint(question_router, url_prefix="/questions")
app.register_blueprint(tags_router, url_prefix="/tags")
app.register_blueprint(delete_router, url_prefix="/delete")
app.register_blueprint(users_router, url_prefix="/api/users")

if __name__ == "main":
    app.run()
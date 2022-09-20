from ast import Delete
from flask import Flask, render_template, request, redirect
from Controllers.Users import SignIn
from Helper.helper import checkAuth
from Routes.Courses import courses_router
from Routes.Users import users_router
from Routes.Questions import question_router
from Routes.Delete import delete_router

app = Flask(__name__)

app.config.from_object("config")
def blabla():
    token = request.cookies.get("_accessToken")
    if token is None or checkAuth(token) is False:
        return SignIn()
app.before_request_funcs = {
    None: [blabla]
}
app.register_blueprint(courses_router, url_prefix="/courses")
app.register_blueprint(question_router, url_prefix="/questions")
app.register_blueprint(delete_router, url_prefix="/delete")
app.register_blueprint(users_router, url_prefix="/")
# @app.route("/")
# def index():
#     return render_template('Login.html', title="Login")

if __name__ == "main":
    app.run()
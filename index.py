from flask import Flask, render_template
from Routes.Courses import courses_router
from Routes.Users import users_router
app = Flask(__name__)

app.config.from_object("config")
app.register_blueprint(courses_router, url_prefix="/courses")
app.register_blueprint(users_router, url_prefix="/users")

@app.route("/")
def index():
    return render_template('Login.html', title="Login")

if __name__ == "main":
    app.run()
from flask import Flask, render_template
from Routes.Courses import courses_router
app = Flask(__name__)

app.config.from_object("config")
app.register_blueprint(courses_router, url_prefix="/courses")


@app.route("/")
def index():
    return render_template('Dashboard.html', title="Dashboard")

if __name__ == "main":
    app.run()
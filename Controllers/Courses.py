import json
from flask import render_template, request
from Helper.database import Database

from Helper.helper import loadSite
from Models.Courses import Course

coursedb = Database("Courses")

def index():
    course = coursedb.select()
    return loadSite("Dashboard.html", "Courses Detail", data={"courses": course})

def insert():
    status = -1
    if request.method == "POST":
        course = request.form['name']
        image = request.form['img']
        tags = request.form['tags']
        db = coursedb
        course = Course(course, image, tags)
        course = course.serialize()
        status = 0
        if db.insert(course):
            status = 1
    return loadSite("AddCourse.html", status=status, data=request.form)

def viewCourse(id):
    course = coursedb.select({"id": int(id)})[0]
    return loadSite("CourseDetail.html", data=course)
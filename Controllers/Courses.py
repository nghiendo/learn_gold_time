from flask import render_template, request

from Helper.helper import loadSite
def index():
    return loadSite("Dashboard.html", "Courses Detail")
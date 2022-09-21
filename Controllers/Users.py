from hashlib import md5, sha1
import json
from time import time
from flask import request, redirect, render_template, make_response, session
from Helper.database import Database
from Helper.helper import checkAuth, loadSite, response

def loadSignIn():
    return render_template("Login.html", title="Sign In")
    
def checkForm(req):
    if req.method != "POST":
        return 0
    email = req.form['email']
    password = req.form['password']
    User = Database('Users')
    users = User.select({
        "email": email,
        "password": md5(password.encode('utf-8')).hexdigest()
    })

    if len(users) == 0:
        return 0
    session['auth'] = email
    return 1

def SignIn():
    if checkAuth(request.cookies.get('_accessToken')):
        return redirect("/courses")
    result = checkForm(request)
    
    return loadSite("Login.html", "Sign In", status = result)


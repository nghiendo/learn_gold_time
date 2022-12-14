from hashlib import md5
from flask import request, redirect, render_template, session, url_for, globals, jsonify
from Helper.database import Database
from Helper.helper import checkAuth, createToken, loadSite, setToken
from config import rootfile

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
    # globals.Token = createToken(email)
    return 1

def SignIn():
    if checkAuth(request.cookies.get('_accessToken')):
        return redirect(url_for("courses_router.index"))
    result = checkForm(request)
    if result == 1:
        return setToken()
    return loadSite("Login.html", "Sign In", status = result, data={"result":result})
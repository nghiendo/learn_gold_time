from hashlib import md5
from flask import request, redirect, render_template, session, url_for, globals, jsonify, Response
from Helper.database import Database
from Helper.helper import checkAuth, createToken, loadSite, setToken
from config import rootfile, path_private_key
from cryptography.fernet import Fernet
from os import path
from time import time
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

def getAllUsers():
    if request.method != "GET":
        return Response(status=500)
    with open(path.join(path_private_key()), 'rb') as f:
        key = f.read()
        F = Fernet(key)
        token = F.encrypt(f"Valid/{str(int(time()))}/to/{str(int(time()) + 86400)}".encode())
        encrypt = F.encrypt(f"hp09.com@gmail.com/{str(int(time()))}/5/{token.decode()}".encode())
        decrypt = F.decrypt(encrypt)
        print(F.decrypt(decrypt.decode().split(".")[-1].encode()))
        return decrypt
    return (request.headers.get('Authorization'))
    Users = Database('Users').select()
    return jsonify(Users)
    # return Response(
    #     response=json.dumps({"sts": 0, "msg": "Error auth", "data":[], "token":""}),
    #     status=200,
    #     mimetype='application/json'
    # )
    # return jsonify({"sts": 0, "msg": "Error auth", "data":[], "token":""})

def SignIn():
    if request.method != "POST":
        return "hello"
    if checkAuth(request.cookies.get('_accessToken')):
        return redirect(url_for("courses_router.index"))
    result = checkForm(request)
    if result == 1:
        return setToken()
    return loadSite("Login.html", "Sign In", status = result, data={"result":result})
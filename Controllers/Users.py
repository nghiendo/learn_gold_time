from hashlib import md5, sha1
import json
from time import time
from flask import request, redirect, render_template
from Helper.database import Database
from Helper.helper import response
def SignIn():
    if request.method != 'POST':
        return "Hello World"
    email = request.form['email']
    password = request.form['password']
    User = Database('Users')
    users = User.select({
        "email": email,
        "password": md5(password.encode('utf-8')).hexdigest()
    })
    token = "{}.{}.{}".format(sha1(email.encode('utf-8')).hexdigest(), int(time() + 43200), 5)
    print(len(users))
    # return response(sts=0) if len(users) is 0 else response(sts=1, token=token)
    return render_template("Login.html", success=0 if len(users) == 0 else 1)
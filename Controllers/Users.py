from flask import request
from Models.Users import insert
def SignIn():
    if request.method != 'GET':
        return False
    email = request.form['email']
    password = request.form['password']
    return True
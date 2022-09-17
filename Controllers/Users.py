from flask import request, redirect
from Helper.database import Database
def SignIn():
    if request.method != 'POST':
        return "Hello World"
    email = request.form['email']
    password = request.form['password']
    User = Database('Users')
    users = User.select({
        "email": email,
        "password": password
    })
    print(users)

    return "Hello World"
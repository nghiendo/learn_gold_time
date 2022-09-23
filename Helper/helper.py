from hashlib import md5, sha1
from html.parser import HTMLParser
from time import time
from flask import render_template, make_response, session, request, globals
import json

def response(sts = 0, data = None, token = None):
    return json.dumps({sts: 0, data: data, _token: token})

def hash(data, type='md5'):
    if type == 'md5':
        return md5(data.encode()).hexdigest()
    elif type == 'sha1':
        return sha1(data.encode()).hexdigest()

def loadSite(Site = None, title = None, status = 0, data = []):
    return render_template(Site, title=title, data=data, status=status)

def checkAuth(_token = None):
    try:
        _token = request.cookies.get("_accessToken") or globals.Token
        if len(_token) == 0:
            return 0
        token = _token.split(".")
        if int(time()) > int(token[1]) and token[2] != 5:
            return 0
        return 1
    except:
        return 0
def createToken(auth):
    return "{}.{}.{}".format(sha1(auth.encode('utf-8')).hexdigest(), int(time() + 43200), 5)
def setToken():
    if "auth" not in session:
        return False
    token = createToken(session['auth'])
    # resp = make_response(render_template("Login.html"))
    # resp.set_cookie("_accessToken", token, 604800)
    # return resp
    return globals.Token

def findLocate(content = [], WHERE = {}):
    for i, x in enumerate(content):
        flag = False
        for key, value in WHERE.items():
            if x[key] == value:
                flag = True
            else:
                flag = False
                break
        if flag == True:
            return i
    return []
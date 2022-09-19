from hashlib import md5, sha1
from html.parser import HTMLParser
from time import time
from flask import render_template
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

def checkAuth(_token):
    try:
        if len(_token) == 0:
            return 0
        token = _token.split(".")
        if int(time()) > int(token[1]) and token[2] != 5:
            return 0
        return 1
    except:
        return 0

from flask import request, redirect
from Helper.helper import checkAuth
def index(id, params):
    if checkAuth(request.cookies.get("_accessToken")) is False:
        return redirect("/")
    obj = id[0]
    id = id[1:]
    if(obj == "C"):
        return deleteCourse(id)
    return obj

def deleteCourse(id):
    return redirect("/courses/delete/"+id)


from Helper.database import Database
from flask import request, redirect, url_for
from Helper.helper import loadSite, checkAuth
from Models.Tags import Tags

def addTag():
    if checkAuth(request.cookies.get("_accessToken")) == 0:
        return redirect(url_for('users_router.SignIn'))
    tag = {}
    if request.method == "POST":
        name = request.form['name']
        tag = Tags(name).serialize()
        if len(Database("Tags").select()) >= 999:
            return redirect("/tags/add")
        Database("Tags").insert(tag)
    tags = Database("Tags").select()
    return loadSite("AddTag.html", "Add Tag", data={"tag": tag, "tags": tags})

def editTag(id):
    if checkAuth(request.cookies.get("_accessToken")) == 0:
        return redirect(url_for('users_router.SignIn'))
    try:
        if request.method == "POST":
            name = request.form['name']
            Database("Tags").update({"name": name}, {"id": id})
        tag = Database("Tags").select({"id": id})
        tags = Database("Tags").select()
        return loadSite("AddTag.html", "Edit Tag", data={"tag": tag[0], "tags": tags})
    except:
        return redirect("/tags/add")
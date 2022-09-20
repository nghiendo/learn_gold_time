from Helper.database import Database
from flask import request
from Helper.helper import loadSite
from Models.Tags import Tags

def index():
    tags = Database("Tags").select()
    tree = []
    for tag in tags:
        if tag['root'] == "root":
            tree.append(tag)
        else:
            for i, t in enumerate(tags):
                if t['id'] == tag['root']:
                    tree[i]['child'].append(tag)
    print(tree)
    return loadSite("TreeTags.html", "Tree Tags")

def addTag():
    tag = {}
    if request.method == "POST":
        name = request.form['name']
        root = request.form['root']
        tag = Tags(name, root).serialize()
        Database("Tags").insert(tag)
    tags = Database("Tags").select()
    return loadSite("AddTag.html", "Add Tag", data={"tags": tags, "tag": tag})
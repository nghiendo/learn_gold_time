import json
import os
from flask import jsonify
basedir = os.path.abspath(os.path.dirname(__file__))

def rootfile():
    site = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(site, "data", "Users.json")
    return jsonify(json.load(open(json_url, "r")))
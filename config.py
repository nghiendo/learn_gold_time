import json
import os
from flask import jsonify
basedir = os.path.realpath(os.path.dirname(__file__))
def rootfile():
    return basedir
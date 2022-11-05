import json
import os
from flask import jsonify
basedir = os.path.realpath(os.path.dirname(__file__))
def rootfile():
    return basedir
def path_private_key():
    return os.path.join(basedir, "private_key.key")

def config_encypt():
    pass
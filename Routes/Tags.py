from flask import Blueprint
from Controllers.Tags import index, addTag

tags_router = Blueprint("tags_router", __name__)
tags_router.route("/", methods=['GET', 'POST'])(index)
tags_router.route("/add", methods=['GET', 'POST'])(addTag)

from flask import Blueprint
from Controllers.Tags import addTag, editTag

tags_router = Blueprint("tags_router", __name__)
tags_router.route("/", methods=['GET', 'POST'])(addTag)
tags_router.route("/add", methods=['GET', 'POST'])(addTag)
tags_router.route("/edit/<id>", methods=['GET', 'POST'])(editTag)

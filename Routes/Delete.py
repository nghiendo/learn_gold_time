from flask import Blueprint
from Controllers.Delete import index
delete_router = Blueprint("delete_router", __name__)
delete_router.route("/<id>/<params>", methods=['GET'])(index)
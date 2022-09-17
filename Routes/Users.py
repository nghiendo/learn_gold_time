from flask import Blueprint

users_router = Blueprint("users_router", __name__)
users_router.route("/signin", methods=['GET'])
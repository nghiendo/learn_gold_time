from flask import Blueprint

from Controllers.Users import SignIn, checkLogin

users_router = Blueprint("users_router", __name__)
users_router.route("/", methods=['GET', 'POST'])(SignIn)
users_router.route("/signin", methods=['GET', 'POST'])(checkLogin)
# users_router.route("/signin", methods=['POST'])(SignIn)
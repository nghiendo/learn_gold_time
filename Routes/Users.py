from flask import Blueprint

from Controllers.Users import SignIn, getAllUsers

users_router = Blueprint("users_router", __name__)
users_router.route("/", methods=['GET'])(getAllUsers)
users_router.route("/sign-in", methods=['POST'])(SignIn)
# users_router.route("/signin", methods=['POST'])(SignIn)
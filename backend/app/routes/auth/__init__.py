from flask import Blueprint

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login")
def login():
    # implementation
    pass


@auth_bp.route("/register")
def login():
    # implementation
    pass

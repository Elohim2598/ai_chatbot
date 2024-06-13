from flask import Blueprint

api_bp = Blueprint("api", __name__)


@api_bp.route("/v1/chat")
def chat():
    # implementation
    pass


@api_bp.route("/v1/completion")
def getcompletion():
    # implementation
    pass


@api_bp.route("/v1/totalConversations")
def getchat():
    # implementation
    pass

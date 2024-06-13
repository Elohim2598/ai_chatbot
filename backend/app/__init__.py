from flask import Flask
from app.routes import heartbeat_bp, api_bp, auth_bp


def create_app(debug: bool = False):
    app = Flask(__name__)
    app.config["DEBUG"] = debug
    app.register_blueprint(heartbeat_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(auth_bp)
    return app

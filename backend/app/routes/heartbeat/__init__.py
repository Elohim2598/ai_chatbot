from flask import Blueprint, jsonify

heartbeat_bp = Blueprint("heartbeat", __name__)


@heartbeat_bp.route("/heartbeat", methods=['GET'])
def heartbeat():
    return jsonify({"alive": True})

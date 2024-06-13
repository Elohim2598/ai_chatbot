from flask import Blueprint

v1 = Blueprint('v1_blueprint', __name__, url_prefix='/api/v1')

from .heartbeat import heartbeat
from .hello import hello
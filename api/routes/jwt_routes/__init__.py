from flask import Blueprint

jwt_bp = Blueprint('jwt_bp', __name__)

from . import routes
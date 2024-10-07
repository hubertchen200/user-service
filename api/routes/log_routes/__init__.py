from flask import Blueprint

log_bp = Blueprint('log_bp', __name__)

from . import routes
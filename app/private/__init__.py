from flask import Blueprint

private_bp = Blueprint('private_bp', __name__)

from . import routes

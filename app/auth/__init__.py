from flask import Blueprint

bp_auth = Blueprint('auth', __name__)

from app.auth import routes
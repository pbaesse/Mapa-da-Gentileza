from flask import Blueprint

bp_feed = Blueprint('feed', __name__)

from app.feed import routes

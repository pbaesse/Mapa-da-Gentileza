from flask import render_template, Blueprint
from app.feed.forms import NewKindnessForm


bp_feed = Blueprint('feed', __name__, url_prefix='/feed')


@bp_feed.route("/new_kindness", methods=['GET', 'POST'])
def new_kindness():
    pass


def configure(app):
	app.register_blueprint(bp_feed)
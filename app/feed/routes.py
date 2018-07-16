from flask import render_template, Blueprint
from flask_login import login_required
from app.feed.forms import NewKindnessForm


bp_feed = Blueprint('feed', __name__, url_prefix='/feed')


@bp_feed.route("/")
@login_required
def feed():
    return render_template("feed/feed.html", msg="Massa")


@bp_feed.route("/new_kindness", methods=['GET', 'POST'])
@login_required
def new_kindness():
    pass


def configure(app):
    app.register_blueprint(bp_feed)

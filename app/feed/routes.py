from flask import render_template, Blueprint
from flask_login import login_required, current_user
from app.models import Kindness, Users
from app.feed.forms import NewKindnessForm
from app.controllers.users_controller import UsersController


bp_feed = Blueprint('feed', __name__, url_prefix='/feed')


@bp_feed.before_app_request
def before_request():
    if current_user.is_authenticated:
        UsersController.last_access(current_user)


@bp_feed.route("/")
@login_required
def feed():
    form = NewKindnessForm()
    return render_template("feed/feed.html", form=form)


@bp_feed.route("/<username>")
@login_required
def get_user(username):
    user = Users.query.filter_by(username=username).first()
    return render_template("feed/user_profile.html", user=user)


def configure(app):
    app.register_blueprint(bp_feed)

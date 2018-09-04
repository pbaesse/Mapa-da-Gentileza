from flask import render_template, Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import Kindness, Users, Kindness_Files, Tags
from app.feed.forms import NewKindnessForm, UpdateKindnessForm
from app.controllers.users_controller import UsersController
from app.controllers.kindness_controller import KindnessController
from app.controllers.kindness_files_controller import KindnessFilesController
from extensions import photos


bp_feed = Blueprint('feed', __name__, url_prefix='/feed')


@bp_feed.before_app_request
def before_request():
    if current_user.is_authenticated:
        UsersController.last_access(current_user)


@bp_feed.route("/", methods=['GET', 'POST'])
@login_required
def feed():
    form = NewKindnessForm()
    tags = Tags.query.all()
    tags_list = [(tag.id, tag.description) for tag in tags]
    form.tags.choices = tags_list
    if form.validate_on_submit():
        post_image = form.file.data
        kindness = Kindness(title=form.title.data, latitude=form.latitude.data,
                            longitude=form.longitude.data, body=form.body.data, user_id=current_user.id)
        controller = KindnessController()
        id_kindness = controller.save_new_kindness(kindness)
        KindnessFilesController.save_image(post_image, id_kindness)
        print("ID: {} ".format(id_kindness))
        # ajeitar essa mensagem.
        return jsonify(data={'message': 'Postado {}'.format(form.title.data)})
    return render_template("feed/feed.html", form=form)


@bp_feed.route("/list_kindness", methods=['GET'])
def list_kindness():
    posts = Kindness.query.all()
    return jsonify([kindness.to_json() for kindness in posts])


@bp_feed.route("/<username>")
@login_required
def get_user(username):
    user = Users.query.filter_by(username=username).first()
    return render_template("feed/user_profile.html", user=user)


@bp_feed.route("/update_kindness")
def update_kindness():
    form = UpdateKindnessForm()
    if form.validate_on_submit():
        data = request.get_json()
        kindness = Kindness(title=data['title'], latitude=data[
                            'latitude'], longitude=data['longitude'], body=data['body'])
        controller = KindnessController()
        controller.update_kindness(
            kindness_up=kindness, kindness_identifier=data['identifier'])
        return jsonify(response={'message': 'Post {} atualizado com sucesso'.format(form.title.data)})
    return render_template("feed/feed.html", form=form)


def configure(app):
    app.register_blueprint(bp_feed)

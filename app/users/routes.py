import os
from datetime import datetime
from flask import Blueprint, request, render_template, redirect, url_for, jsonify, send_from_directory
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from dynaconf import settings
from app.models import Users, Kindness
from app.schemas import UserSchema, KindnessSchema
from app.helpers import convert_object_to_json
from app.controllers.users_controller import UsersController
from app.controllers.files_controller import FilesController
from app.users.forms import UpdateProfileForm, UpdatePasswordForm, SearchUserForm


bp_users = Blueprint('users', __name__, url_prefix='/users')


@bp_users.route("/search", methods=['POST'])
@login_required
def search_user():
    form = SearchUserForm()
    data = request.get_json()
    search = data['search']
    users = Users.query.filter((Users.username.contains(search)) | (Users.first_name.contains(search)))
    return jsonify([user.to_json() for user in users])


@bp_users.route("/<username>")
@login_required
def get_user(username):
    form = UpdateProfileForm(current_user.username)
    user = Users.query.filter_by(username=username).first()
    return render_template("users/user_profile.html", user=user, title=user.username, form=form)


@bp_users.before_app_request
def before_request():
    if current_user.is_authenticated:
        UsersController.last_access(current_user)


@bp_users.route("/settings/edit_profile", methods=['POST'])
@login_required
def edit_profile():
    form = UpdateProfileForm(current_user.username)
    if form.validate_on_submit():
        # corrigir a inserção da data no banco. ERRO.
        avatar = form.avatar.data
        date_birth = form.year_birth.data + "-" + \
            form.month_birth.data + "-" + form.birthday.data


        user = Users(username=form.username.data, first_name=form.first_name.data, last_name=form.last_name.data,
                     about_me=form.about_me.data, avatar=avatar, date_birth=str(datetime.strptime(date_birth, "%Y-%m-%d")),
                     status=form.status.data, phone=form.phone.data)
        controller = UsersController()
        print("CURRENT USER: {}".format(current_user))
        controller.update_profile(user=user, current_user=current_user)
        return jsonify(data={'message': 'Perfil atualizado com sucesso!'})
    return jsonify(data={'message': 'Erro ao atualizar o perfil'})


@bp_users.route("/settings/get_profile", methods=['GET'])
@login_required
def get_profile():
    user_data = UserSchema().dump(current_user)
    return jsonify({'user': user_data.data})


@bp_users.route("/uploads/users_images/<path:filename>")
def get_profile_pic(filename):
    return send_from_directory(settings.get('UPLOAD_USERS_FOLDER'), filename)


@bp_users.route("/settings/update_password", methods=['GET', 'POST'])
@login_required
def update_password():
    form = UpdatePasswordForm()
    if form.validate_on_submit():
        controller = UsersController()
        data = request.get_json()
        print(data)
        if controller.check_pass(password=data['old_password'], pass_hash=current_user.password_hash):
            controller.update_password(
                user=current_user, new_password=form.new_password.data)
            return jsonify(data={'message': 'Password atualizada com sucesso!'})
        return redirect(url_for('users.update_password'))
    return render_template("users/update_password.html", form=form)


def configure(app):
    app.register_blueprint(bp_users)

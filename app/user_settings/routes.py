import os
from flask import Blueprint, request, render_template, redirect, url_for, jsonify
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from dynaconf import settings
from datetime import datetime
from app.models import Users
from app.controllers.users_controller import UsersController
from app.controllers.files_controller import FilesController
from app.user_settings.forms import UpdateProfileForm, UpdatePasswordForm


bp_user_settings = Blueprint(
    'user_settings', __name__, url_prefix='/settings')


@bp_user_settings.before_app_request
def before_request():
    if current_user.is_authenticated:
        UsersController.last_access(current_user)


@bp_user_settings.route("/edit_profile", methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = UpdateProfileForm(current_user.username)
    if form.validate_on_submit():
        # corrigir a inserção da data no banco. ERRO.
        date_birth = form.year_birth.data + "-" + \
            form.month_birth.data + "-" + form.birthday.data

        filename = secure_filename(form.avatar.data)
        avatar.save()
        user = Users(first_name=form.first_name.data, last_name=form.last_name.data,
                     about_me=form.about_me.data, avatar=filename, date_birth=str(datetime.strptime(date_birth, "%Y-%m-%d")))
        controller = UsersController()
        controller.update_profile(user=user, current_user=current_user)
        return redirect(url_for('user_settings.edit_profile'))
    return render_template("user_settings/edit_profile.html", form=form)

@bp_user_settings.route("/get_profile", methods=['GET'])
def get_profile():
    print(current_user)
    return jsonify(current_user.to_json())


@bp_user_settings.route("/update_password", methods=['GET', 'POST'])
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
        return redirect(url_for('user_settings.update_password'))
    return render_template("user_settings/update_password.html", form=form)


def configure(app):
    app.register_blueprint(bp_user_settings)

from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import login_required, current_user
from datetime import datetime
from app.models import Users
from app.controllers.users_controller import UsersController
from app.user_settings.forms import UpdateProfileForm, UpdatePasswordForm


bp_user_settings = Blueprint(
    'user_settings', __name__, url_prefix='/settings')


@bp_user_settings.route("/edit_profile", methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = UpdateProfileForm(current_user.username)
    if form.validate_on_submit():
        user = Users(first_name=form.first_name.data, last_name=form.last_name.data,
                     about_me=form.about_me.data, avatar=form.avatar.data)
        controller = UsersController()
        controller.update_profile(user=user, current_user=current_user)
        #date_birth = form.year_birth.data + "-" + form.month_birth.data + "-"+form.birthday.data
        # current_user.date_birth = str(
        # datetime.strptime(date_birth, "%Y-%m-%d"))
        return redirect(url_for('user_settings.edit_profile'))
    elif request.method == "GET":
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.about_me.data = current_user.about_me
        form.avatar.data = current_user.avatar
    return render_template("user_settings/edit_profile.html", form=form)


@bp_user_settings.route("/update_password", methods=['GET', 'POST'])
@login_required
def update_password():
    form = UpdatePasswordForm()
    if form.validate_on_submit():
        controller = UsersController()
        if controller.check_password(password=form.new_password.data, current_user=current_user):
            controler.update_password(
                user=current_user, new_password=form.new_password.data)
            return redirect(url_for('user_settings.update_password'))
        return redirect(url_for('user_settings.update_password'))
    return render_template("user_settings/update_password.html", form=form)


def configure(app):
    app.register_blueprint(bp_user_settings)

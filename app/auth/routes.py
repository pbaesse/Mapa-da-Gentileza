from flask import render_template, redirect, flash, request, url_for, Blueprint
from flask_login import login_user, current_user, logout_user
from app.models import Users
from app.auth.forms import RegisterForm, LoginForm, ResetPasswordForm, RequestResetPasswordForm
from app.controllers.users_controller import UsersController
from app.services.mail import send_password_reset_email, send_confirm_email


bp_auth = Blueprint('auth', __name__, url_prefix='/auth')


@bp_auth.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('feed.feed'))
    form = RegisterForm()
    if form.validate_on_submit():
        # ajeitar isso aqui quando estiver codificando as rotas
        ip_client = request.remote_addr
        genre = "Masculino"
        date = "1999-11-28"
        user = Users(username=form.username.data, email=form.email.data,
                     password_hash=form.password.data, first_name=form.first_name.data, genre=genre, date_birth=date, device_ip_register=ip_client)
        controller = UsersController()
        controller.save_new_user(user)
        send_confirm_email(user)
        return render_template("auth/confirm_email_msg.html", user=user)
    return render_template("auth/register.html", form=form)


@bp_auth.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('feed.feed'))
    form = LoginForm()
    if form.validate_on_submit():
        controller = UsersController()
        user = controller.login(form.email.data, form.password.data)
        if user is not None:
            login_user(user)
            return redirect(url_for('feed.feed'))
        return redirect(url_for('auth.login'))
    return render_template("auth/login.html", form=form)


@bp_auth.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('feed.feed'))
    user = UsersController.verify_token_reset_password(token)
    if not user:
        return redirect(url_for('auth.login'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        controller = UsersController()
        controller.update_password(user=user, new_password=form.password.data)
        return redirect(url_for('auth.login'))
    return render_template("auth/reset_password.html", form=form, token=token)


@bp_auth.route("/reset_password_request", methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('feed.feed'))
    form = RequestResetPasswordForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash("Verifique seu email para instruções de redefinição.")
        return redirect(url_for('auth.login'))
    return render_template("auth/reset_password_request.html", form=form)


@bp_auth.route("/confirm_email/<token>", methods=['GET', 'POST'])
def confirm_email(token):
    user = UsersController.verify_token_confirmed_email(token)
    if not user:
        return redirect(url_for('auth.register'))
    controller = UsersController()
    controller.confirmed_email(user)
    return redirect(url_for('auth.login'))


@bp_auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


def configure(app):
    app.register_blueprint(bp_auth)

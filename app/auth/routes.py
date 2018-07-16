from flask import render_template, redirect, request, url_for, Blueprint
from flask_login import login_user, current_user, logout_user
from app.models import Users
from app.auth.forms import RegisterForm, LoginForm
from app.controllers.users_controller import UsersController


bp_auth = Blueprint('auth', __name__, url_prefix='/auth')


@bp_auth.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('feed.feed'))
    form = RegisterForm()
    if form.validate_on_submit():
        # ajeitar isso aqui quando estiver codificando as rotas
        ip = "197.123.12.23"
        genre = "Masculino"
        date = "1999-11-28"
        user = Users(username=form.username.data, email=form.email.data,
                     password_hash=form.password.data, first_name=form.first_name.data, genre=genre, date_birth=date, device_ip_register=ip)
        controller = UsersController()
        controller.save_new_user(user)
        return render_template("feed/feed.html", msg="Seu cadastro foi realizado com sucesso, Larry.")
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
        return redirect(url_for('login'))
    return render_template("auth/login.html", form=form)


@bp_auth.route("/reset_password", methods=['GET', 'POST'])
def reset_password():
    pass


@bp_auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


def configure(app):
    app.register_blueprint(bp_auth)

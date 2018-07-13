from flask import render_template, redirect, request, url_for
from app.auth import bp_auth
from app.models import Users
from app.auth.forms import RegisterForm
from app.controllers.users_controller import UsersController


@bp_auth.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # ajeitar isso aqui quando estiver codificando as rotas
        ip = "197.123.12.23"
        first_name = "Matheus"
        genre = "Masculino"
        date = "1999-11-28"
        user = Users(username=form.username.data, email=form.email.data,
                     password_hash=form.password.data, first_name=first_name, genre=genre, date_birth=date, device_ip_register=ip)
        controller = UsersController()
        controller.save_new_user(user)
        # redirecionar para o inicio
        return render_template("auth/teste.html", msg="Seu cadastro foi realizado com sucesso, Larry.")
    return render_template("auth/login.html", form=form)


@bp_auth.route("/login", methods=['GET', 'POST'])
def login():
    pass


@bp_auth.route("/reset_password", methods=['GET', 'POST'])
def reset_password():
    pass

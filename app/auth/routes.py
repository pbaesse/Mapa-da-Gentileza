from app.auth import bp_auth
from app.models import Users
from app.auth.forms import RegisterForm
from app.controllers import users_controllers
from flask import render_template, redirect, request, url_for 


@bp_auth.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        #ajeitar isso aqui quando estiver codificando as rotas
        avatar = "vsvskvjsdvsv"
        ip = "197.123.12.23"
        user = Users(form.username.data, form.email.data, form.password.data, avatar, ip)
        UsersController.save_new_user(user)
        #redirecionar para o inicio
        return render_template("auth/teste.html", msg="Seu cadastro foi realizado com sucesso, Larry.")
    return render_template("auth/login.html", form=form)

@bp_auth.route("/login", methods=['GET', 'POST'])
def login():
    pass


@bp_auth.route("/reset_password", methods=['GET', 'POST'])
def reset_password():
    pass



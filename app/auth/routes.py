from app.auth import bp_auth
from app.models import Users
from flask import render_template, redirect, request, url_for
from app.auth.forms import RegisterForm


@bp_auth.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        #ajeitar isso aqui quando estiver codificando as rotas
        avatar = "vsvskvjsdvsv"
        ip = "197.123.12.23"
        user = Users(form.username.data, form.email.data, form.password.data, avatar, ip)
        user.save()
        #consertar isso aqui.
        return render_template("auth/teste.html", msg="Seu cadastro foi realizado com sucesso, Larry.")
    return render_template("auth/login.html", form=form)

@bp_auth.route("/login", methods=['GET', 'POST'])
def login():
    pass


@bp_auth.route("/reset_password", methods=['GET', 'POST'])
def reset_password():
    pass



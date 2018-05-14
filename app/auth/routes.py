from app.auth import bp_auth
from app.models import User
from flask import render_template, redirect, request, url_for
from app.auth.forms import RegisterForm


@bp_auth.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        #ajeitar isso aqui quando estiver codificando as rotas
        avatar = "vsvskvjsdvsv"
        user = User(form.username.data, form.email.data, form.password.data, avatar)
        user.save()
        #consertar isso aqui.
        return render_template("auth/teste.html", msg="Seu cadastro foi realizado com sucesso, Larry.")
    return render_template("auth/login.html", form=form)
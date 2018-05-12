from app.auth import bp_auth
from app.models import User
from flask import render_template

@bp_auth.route("/login", methods=['GET', 'POST'])
def login():
    pass
    #terminar a lógica dos models antes de escrever as rotas.
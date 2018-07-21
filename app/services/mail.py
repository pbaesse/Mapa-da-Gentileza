from threading import Thread
from flask import render_template, Blueprint, current_app
from flask_mail import Message
from extensions import mail
from dynaconf import settings
from app.controllers.users_controller import UsersController

# criar a tarefa assincrona para enviar o email.

bp_mail = Blueprint('mail', __name__, template_folder="templates/email/")


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(
        current_app._get_current_object(), msg)).start()

# Refatorar isso aqui depois para deixar mais genérico e escrever menos código.


def send_password_reset_email(user):
    token = UsersController.generate_token_reset_password(user.id)
    text_body = render_template(
        "email/reset_password.txt", user=user, token=token)
    html_body = render_template(
        "email/reset_password.html", user=user, token=token)
    send_email("KindnessMap. Reset your password.", sender=current_app.config['ADMINS'][
               0], recipients=[user.email], text_body=text_body, html_body=html_body)


def send_confirm_email(user):
    token = UsersController.generate_token_confirmed_email(user.email)
    html_body = render_template(
        "email/confirm_email.html", user=user, token=token)
    send_email("KindnessMap. Confirm email", sender=current_app.config[
               'ADMINS'][0], recipients=[user.email], text_body=None ,html_body=html_body)


def configure(app):
    app.register_blueprint(bp_mail)

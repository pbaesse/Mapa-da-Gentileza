from flask import Blueprint

bp_user_settings = Blueprint(
    'user_settings', __name__, url_prefix='/user_settings')


def configure(app):
    app.register_blueprint(bp_user_settings)

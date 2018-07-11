from flask import Flask
from config import Config
from extensions import db, migrate, login

from app.auth import bp_auth
from app.errors import bp_errors
from app.feed import bp_feed
from app import models
from app.controllers import users_controller


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    #registro dos blueprints dos modulos do app
    app.register_blueprint(bp_auth, url_prefix='/auth')
    app.register_blueprint(bp_errors)
    app.register_blueprint(bp_feed, url_prefix='/feed')

    return app


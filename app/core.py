from flask import Flask
from flask_uploads import configure_uploads
from config import Config
from extensions import db, migrate, login, dynaconf

from app.auth import routes as accounts
from app.errors import routes as errors
from app.feed import routes as feed
from app import models
from app.controllers import users_controller


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    dynaconf.init_app(app)
    #configure_uploads(app, photos)

    # configurando os blueprints
    accounts.configure(app)
    errors.configure(app)
    feed.configure(app)

    return app

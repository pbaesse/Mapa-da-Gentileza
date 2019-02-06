from flask import Flask
from config import Config
from extensions import db, migrate, login, dynaconf, mail, marshmallow, moment

from app.auth import routes as accounts
from app.errors import routes as errors
from app.feed import routes as feed
from app.users import routes as users
#from app.common import image
from app.services import mail as email
from app import models
from app.controllers import users_controller


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    marshmallow.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    dynaconf.init_app(app)
    mail.init_app(app)
    moment.init_app(app)

    # configurando os blueprints
    accounts.configure(app)
    errors.configure(app)
    feed.configure(app)
    users.configure(app)
    #image.configure(app)
    email.configure(app)

    return app

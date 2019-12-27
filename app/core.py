from flask import Flask, Blueprint
from config import Config
from extensions import api, db, migrate, login, dynaconf, mail, marshmallow
from app import models
from app.controllers import users_controller

from app.services.users_endpoints import namespace_user
from app.services.kindness_endpoints import namespace_kindness
from app.services.auth_endpoints import namespace_auth
from app.services.tags_endpoints import namespace_tags


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    blueprint = Blueprint("api", __name__)

    api.init_app(blueprint)
    app.register_blueprint(blueprint)

    db.init_app(app)
    marshmallow.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    dynaconf.init_app(app)
    mail.init_app(app)

    api.add_namespace(namespace_user)
    api.add_namespace(namespace_kindness)
    api.add_namespace(namespace_auth)
    api.add_namespace(namespace_tags)

    return app

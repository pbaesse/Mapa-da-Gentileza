from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from dynaconf import FlaskDynaconf
from flask_marshmallow import Marshmallow

from app.authorizations import authorizations


api = Api(version="beta", title="Mapa da Gentileza API", description="Mapa da Gentileza API", authorizations=authorizations)
db = SQLAlchemy()
marshmallow = Marshmallow()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = u"Faca login para acessar"
mail = Mail()
dynaconf = FlaskDynaconf()

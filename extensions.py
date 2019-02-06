from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
from dynaconf import FlaskDynaconf
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
marshmallow = Marshmallow()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = u"Faca login para acessar"
mail = Mail()
moment = Moment()
dynaconf = FlaskDynaconf()

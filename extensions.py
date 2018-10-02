from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from dynaconf import FlaskDynaconf


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = u"Faca login para acessar"
mail = Mail()
dynaconf = FlaskDynaconf()

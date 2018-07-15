from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from dynaconf import FlaskDynaconf

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
dynaconf = FlaskDynaconf()
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from app.auth import bp_auth

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager()

#melhorar esse código criando uma fábrica de apps. Vejo isso depois.
app.register_blueprint(bp_auth, url_prefix='/auth')

from app import models
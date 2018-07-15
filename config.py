import os
from dotenv import load_dotenv
from dynaconf import settings
from db import DatabaseSettings


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    """ Class that defines the application settings."""

    SECRET_KEY = settings.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = DatabaseSettings.get_db()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
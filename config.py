import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	""" Class that defines the application settings."""

	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://userdb:passdb@localhost/KindnessMap'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY = '&a*50Aj#'
from dynaconf import settings


class DatabaseSettings:

	@staticmethod
	def get_db():
		user = settings.get('MYSQL_USER')
		password = settings.get('MYSQL_PASSWORD')
		host = settings.get('MYSQL_HOST')
		database = settings.get('MYSQL_DATABASE')
		return "mysql+pymysql://{}:{}@{}/{}".format(user, password, host, database)
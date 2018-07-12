from app.models import Users
from datetime import datetime
from app.app import login
import bcrypt
import random


class UsersController:

	
	@login.user_loader
	def load_user(username):
		return Users.query.get(username)


	@staticmethod
	def save_new_user(self, user):
		received_data = [
			user.first_name, user.email,
			user.password, user.genre,
			user.date_birth, user.username		
		]

		if all(received_data):
			user.pass_hash = encrypt_pass(user.password)
			user.save()


	def login(email, password):
		user = Users.query.filter_by(email=email).first()
		if user is not None and check_pass(password, user.pass_hash):
			return user


	def update_profile(self, user):
		pass


	def get_all_users(self):
		return Users.query.all()


	def get_user_by_username(self, username):
		return Users.query.filter_by(username=username).first()


	def search_users_by_name(self, first_name):
		return Users.query.filter_by(first_name=first_name)


	def generate_unique_username(self, first_name):
		numero = random.randrange(datetime.now().second * datetime.now().minute) + 77
		return user.first_name + str(numero)


	def delete_account(self, user):
		pass


	def update_password(self, user):
		pass


	def encrypt_pass(self, password):
		return bcrypt.hashpw(password, bcrypt.gensalt(9))


	def check_pass(self, password, pass_hash):
		return bcrypt.checkpw(password, pass_hash)

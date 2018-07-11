from app.models import Users
from datetime import datetime
import random


class UsersController:

	
	@staticmethod
	def save_new_user(self, user):
		received_data = [
			user.first_name, user.email,
			user.password, user.genre,
			user.date_birth, user.username		
		]

		if all(received_data):
			#enviar email de confirmação antes de habilitar conta.
			user.save()


	def update_profile(self, user):
		pass


	def get_all_users(self):
		return Users.query.all()


	def get_user_by_id(self, user):
		return Users.query.filter_by_id(id=user.id).first()


	def search_users_by_name(self, user):
		return Users.query.filter_by(first_name=user.first_name)


	def generate_unique_username(self, first_name):
		numero = random.randrange(datetime.now().second * datetime.now().minute) + 77
		return user.first_name + str(numero)


	def delete_account(self, user):
		pass


	def update_password(self, user):
		pass

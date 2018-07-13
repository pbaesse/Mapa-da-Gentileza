import bcrypt
import random
from datetime import datetime
from app.models import Users
from app.core import login


class UsersController:

    @login.user_loader
    def load_user(username):
        return Users.query.get(username)

    def encrypt_pass(self, password):
        return bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt(9))

    def check_pass(self, password, pass_hash):
        return bcrypt.checkpw(password.encode('utf8'), pass_hash)

    def save_new_user(self, user):
        received_data = [
            user.first_name, user.email,
            user.password_hash, user.genre,
            user.date_birth, user.username
        ]

        if all(received_data):
            user.password_hash = self.encrypt_pass(user.password_hash)
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
        numero = random.randrange(
            datetime.now().second * datetime.now().minute) + 77
        return user.first_name + str(numero)

    def delete_account(self, user):
        pass

    def update_password(self, user):
        pass

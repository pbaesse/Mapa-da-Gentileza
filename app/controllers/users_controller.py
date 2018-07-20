import bcrypt
import random
import jwt
from time import time
from dynaconf import settings
from datetime import datetime
from app.models import Users
from app.core import login
from extensions import db


class UsersController:

    @login.user_loader
    def load_user(username):
        return Users.query.get(username)

    def encrypt_pass(self, password):
        return bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt(9))

    def check_pass(self, password, pass_hash):
        return bcrypt.checkpw(password.encode('utf8'), pass_hash.encode('utf8'))

    def save_new_user(self, user):
        received_data = [
            user.first_name, user.email,
            user.password_hash, user.genre,
            user.date_birth, user.username
        ]

        if all(received_data):
            user.password_hash = self.encrypt_pass(user.password_hash)
            db.session.add(user)
            db.session.commit()

    def login(self, email, password):
        user = Users.query.filter_by(email=email).first()
        if user is not None and self.check_pass(password, user.password_hash):
            return user

    def update_profile(self, user):
        pass

    def generate_unique_username(self, first_name):
        numero = random.randrange(
            datetime.now().second * datetime.now().minute) + 77
        return user.first_name + str(numero)

    def delete_account(self, user):
        pass

    def update_password(self, user):
        user.password_hash = self.encrypt_pass(user.password_hash)
        db.session.commit()

    @staticmethod
    def generate_token_reset_password(id_user, expire_in=600):
        return jwt.encode({'reset_password': id_user, 'exp': time() + expire_in},
                          settings.get('SECRET_KEY'), algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_token_reset_password(token):
        try:
            id = jwt.decode(token, settings.get('SECRET_KEY'),
                            algorithm=['HS256'])['reset_password']
        except:
            return
        return Users.query.get(id)

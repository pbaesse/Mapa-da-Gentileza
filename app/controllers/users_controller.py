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
        if user is not None and self.check_pass(password, user.password_hash) and user.confirmed:
            return user

    """def save_avatar(self, image):
        filename = photos.save(image, folder="users_images/")
        extension = filename.split('.')[-1]
        return filename

    def update_profile(self, user, current_user):
        current_user.first_name = user.first_name
        current_user.last_name = user.last_name
        current_user.about_me = user.about_me
        current_user.avatar = self.save_avatar(user.avatar)
        db.session.commit()"""

    def delete_account(self, user):
        pass

    @staticmethod
    def last_access(user):
        user.last_access = datetime.utcnow()
        db.session.commit()

    def update_password(self, user, new_password):
        user.password_hash = self.encrypt_pass(new_password)
        db.session.commit()

    def confirmed_email(self, user):
        user.confirmed = True
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

    @staticmethod
    def generate_token_confirmed_email(email_user, expire_in=600):
        return jwt.encode({'confirm_email': email_user, 'exp': time() + expire_in},
                          settings.get('SECRET_KEY'), algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_token_confirmed_email(token):
        try:
            email = jwt.decode(token, settings.get(
                'SECRET_KEY'), algorithm=['HS256'])['confirm_email']
        except:
            return
        return Users.query.filter_by(email=email).first()

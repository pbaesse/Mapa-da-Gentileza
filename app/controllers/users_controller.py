import bcrypt
import random
from datetime import datetime
import jwt
from time import time
from dynaconf import settings
from app.models import Users
from app.core import login
from app.controllers.files_controller import FilesController
from extensions import db


class UsersController:


    def encrypt_pass(self, password):
        return bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt(9))

    def check_pass(self, password, pass_hash):
        return bcrypt.checkpw(password.encode('utf8'), pass_hash.encode('utf8'))

    def save_new_user(self, first_name=None, email=None, password=None, genre=None, date_birth=None, username=None, device_ip_register=None):

        user = Users(first_name=first_name, email=email, genre=genre, date_birth=date_birth, username=username, device_ip_register=device_ip_register)

        user.password_hash = self.encrypt_pass(password)

        db.session.add(user)
        db.session.commit()


    def search_user(self, search):
        return Users.query.filter((Users.username.contains(search)) | (Users.first_name.contains(search))).all()


    def get_user_profile(self, id_user):
        return Users.query.filter_by(id=id_user).first()


    def login(self, email, password):
        user = Users.query.filter_by(email=email).first()
        if user is not None and self.check_pass(password, user.password_hash) and user.confirmed:
            return user

    def save_avatar(self, image=None, type_upload=None, id_kindness=None, id_user=None):
        if image is not None:
            controller = FilesController()
            print("ID USUÁRIO DA IMAGEM: {}".format(id_user))
            filename = controller.save_image(files=image, type_upload="img_profile", id_user=id_user)
            print("FILENAME IN UPDATE PROFILE: {}".format(filename))
            return filename


    def update_profile(self, id_user, first_name, last_name, about_me, date_birth):
        current_user = Users.query.get(id_user)
        current_user.first_name = first_name
        current_user.last_name = last_name
        current_user.about_me = about_me
        current_user.date_birth = date_birth
        db.session.commit()

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

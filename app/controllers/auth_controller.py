import bcrypt
import datetime
import jwt
from dynaconf import settings
from extensions import db
from app.models import Users


class AuthController:

    def check_pass(self, password, pass_hash):
        return bcrypt.checkpw(password.encode('utf8'), pass_hash.encode('utf8'))

    def login(self, email, password):
        user = Users.query.filter_by(email=email).first()
        if user is not None and self.check_pass(password, user.password_hash):
            return user

    def save_token(self, token, id_user):
        user = Users.query.get(id_user)
        user.auth_token = token
        db.session.commit()

    def logout(self, id_user):
        user = Users.query.get(id_user)
        user.auth_token = None
        db.session.commit()

    def generate_auth_token(self, id_user):
        try:
            payload = {
                "exp": datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=2592000),
                "iat": datetime.datetime.utcnow(),
                "sub": id_user
            }
            return jwt.encode(
                payload,
                settings.get("SECRET_KEY"),
                algorithm="HS256"
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(token):
        try:
            payload = jwt.decode(token, settings.get("SECRET_KEY"))
            return payload["sub"]
        except jwt.ExpiredSignatureError:
            return "Signature expired. log in again"
        except jwt.InvalidTokenError:
            return "Invalid token. log in again"


    @staticmethod
    def auth_token_is_valid(token=None):

        if token is not None:
            resp = AuthController.decode_auth_token(token)

            if not isinstance(resp, str):
                user = Users.query.filter_by(id=resp).first()
                response = {
                    "status": "success",
                    "data": {
                        "id_user": user.id,
                        "username": user.username
                    }
                }
                return response, 200
            response = {
                "status": "fail",
                "message": resp
            }
            return response, 401
        else:
            response = {
                "status": "fail",
                "message": "Fail a valid auth token"
            }
            return response, 401

from flask import request, make_response, jsonify
from flask_restplus import Resource
from extensions import api
from app.serializers.auth_serializer import auth_serializer
from app.controllers.auth_controller import AuthController

namespace_auth = api.namespace("auth", description="Operations related with auth")

@namespace_auth.route("/login")
class AuthCollection(Resource):

    def __init__(self, api=None, *args, **kwargs):
        super(AuthCollection, self).__init__(api, args, kwargs)
        self.auth = AuthController()


    @api.expect(auth_serializer)
    def post(self):
        data = request.json

        email = data.get('email')
        password = data.get('password')
        user = self.auth.login(email=email, password=password)
        if user:
            token = self.auth.generate_auth_token(id_user=user.id)
            if token:
                self.auth.save_token(token=token.decode(), id_user=user.id)
                response = {
                    "status": "success",
                    "message": "Logged successfuly",
                    "X-API-KEY": token.decode()
                }
                return response, 200
        else:
            response = {
                "status": "fail",
                "message": "Users does not exists"
            }
            return response, 404

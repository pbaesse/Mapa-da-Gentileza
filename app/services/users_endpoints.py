from flask import request
from flask_restplus import Resource
from extensions import api
from app.schemas import UserSchema
from app.util.decorator import token_required
from app.serializers.user_serializer import user_create_serializer
from app.controllers.users_controller import UsersController

namespace_user = api.namespace("user", description="Operations related with users")

parser = api.parser()
parser.add_argument("search", type=str)


@namespace_user.route("/")
class UserCollection(Resource):

    def __init__(self, api=None, *args, **kwargs):
        super(UserCollection, self).__init__(api, args, kwargs)
        self.user = UsersController()


    @api.doc(security="apiKey")
    @api.expect(parser)
    @token_required
    def get(self):
        schema = UserSchema(many=True)

        args = parser.parse_args()
        search = args["search"]

        data = self.user.search_user(search=search)
        return schema.dump(data)


    @api.expect(user_create_serializer)
    def post(self):
        data = request.json

        email = data.get('email')
        first_name = data.get('first_name')
        password = data.get('password')
        genre = data.get('genre')
        date_birth = data.get('date_birth')
        username = data.get('username')
        device_ip_register = data.get('device_ip_register')

        return self.user.save_new_user(first_name=first_name, email=email, password=password, genre=genre, date_birth=date_birth, username=username, device_ip_register=device_ip_register)


@namespace_user.route("/<id>")
class UsersDetail(Resource):

    def __init__(self, api=None, *args, **kwargs):
        super(UsersDetail, self).__init__(api, args, kwargs)
        self.user = UsersController()


    @api.doc(security="apiKey")
    @token_required
    def get(self, id):
        schema = UserSchema()
        data = self.user.get_user_profile(id_user=id)
        return schema.dump(data)


    @api.doc(security="apiKey")
    @token_required
    def put(self, id):
        data = request.json
        """
        username = data.get('username')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        about_me = data.get('about_me')
        status = data.get('status')
        phone = data.get('phone')

        return self.user.update_profile(id_user=id, username=username, first_name=first_name,
                                        last_name=last_name, about_me=about_me, status=status, phone=phone)
        """

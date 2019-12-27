from flask import request
from flask_restplus import Resource
from extensions import api
from app.util.decorator import token_required
from app.schemas import KindnessDetailSchema, KindnessSchema
from app.serializers.kindness_serializer import kindness_create_serializer
from app.controllers.kindness_controller import KindnessController

namespace_kindness = api.namespace("kindness", description="Operations related with kindness")

parser = api.parser()
parser.add_argument("user_latitude", type=float)
parser.add_argument("user_longitude", type=float)
parser.add_argument("id_user", type=int)


@namespace_kindness.route("/")
class KindnessCollection(Resource):

    def __init__(self, api=None, *args, **kwargs):
        super(KindnessCollection, self).__init__(api, args, kwargs)
        self.kindness = KindnessController()


    #@api.doc(security="apiKey")
    @api.expect(parser)
    #@token_required
    def get(self):
        schema = KindnessSchema(many=True)

        args = parser.parse_args()
        latitude = args["user_latitude"]
        longitude = args["user_longitude"]

        data = self.kindness.get_kindness_by_location(user_latitude=latitude, user_longitude=longitude)

        return schema.dump(data)


    #@api.doc(security="apiKey")
    @api.expect(kindness_create_serializer)
    #@token_required
    def post(self):
        data = request.json

        title = data.get("title")
        latitude = data.get("latitude")
        longitude = data.get("longitude")
        body = data.get("body")
        id_user = data.get("id_user")
        tags = data.get("tags")

        return self.kindness.save_new_kindness(title=title, body=body,
                                               latitude=latitude, longitude=longitude,
                                               id_user=id_user, tags=tags)


@namespace_kindness.route("/<id_kindness>")
class KindnessDetail(Resource):

    def __init__(self, api=None, *args, **kwargs):
        super(KindnessDetail, self).__init__(api, args, kwargs)
        self.kindness = KindnessController()


    @api.doc(security="apiKey")
    @token_required
    def get(self, id_kindness):
        schema = KindnessDetailSchema()
        data = self.kindness.get_kindness_by_id(id_kindness=id_kindness)
        return schema.dump(data)


    @api.doc(security="apiKey")
    @token_required
    def put(self, id):
        pass

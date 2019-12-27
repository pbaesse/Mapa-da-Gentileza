from flask import request
from flask_restplus import Resource
from extensions import api
from app.util.decorator import token_required
from app.schemas import TagsSchema
from app.controllers.tags_controller import TagsController


namespace_tags = api.namespace("tags", description="Operations related with tags")


@namespace_tags.route("/")
class TagsCollection(Resource):

    def __init__(self, api=None, *args, **kwargs):
        super(TagsCollection, self).__init__(api, args, kwargs)
        self.tags = TagsController()


    @api.doc(security="apiKey")
    @token_required
    def get(self):
        schema = TagsSchema(many=True)
        data = self.tags.get_tags()
        return schema.dump(data)

    #@api.doc(security="apiKey")
    #@api.expect(kindness_create_serializer)
    #@token_required
    def post(self):
        pass

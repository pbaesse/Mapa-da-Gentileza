from flask_restplus import fields
from extensions import api


kindness_create_serializer = api.model("Kindness", {
    "title": fields.String(),
    "body": fields.String(required=True),
    "latitude": fields.Float(),
    "longitude": fields.Float(),
    "id_user": fields.Integer(),
    "tags": fields.List(fields.Integer())
})

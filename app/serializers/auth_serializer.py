from flask_restplus import fields
from extensions import api


auth_serializer = api.model('Auth', {
    "email": fields.String(required=True),
    "password": fields.String(required=True)
})

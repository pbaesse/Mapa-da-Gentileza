from flask_restplus import fields
from extensions import api


user_create_serializer = api.model('UserCreate', {
    "email": fields.String(required=True),
    "first_name": fields.String(required=True),
    "password": fields.String(required=True),
    "genre": fields.String(),
    "username": fields.String(required=True),
    "device_ip_register": fields.String(required=True),
    "date_birth": fields.DateTime(dt_format="iso8601")
})

user_update_serializer = api.model('UserUpdate', {
    "email": fields.String(required=True),
    "first_name": fields.String(required=True),
    "genre": fields.String(),
    "username": fields.String(required=True),
    "date_birth": fields.DateTime(dt_format="iso8601"),
    "last_name": fields.String(),
    "about_me": fields.String(),
    "phone": fields.String()
})

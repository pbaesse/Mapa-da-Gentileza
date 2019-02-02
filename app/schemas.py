from marshmallow import fields
from extensions import marshmallow as ma
from app.models import Users, Kindness


class UserSchema(ma.ModelSchema):
    posts = fields.Nested('KindnessSchema', many=True, exclude=('user_id',))
    class Meta:
        model = Users


class KindnessSchema(ma.ModelSchema):
    user = fields.Nested(UserSchema)
    class Meta:
        model = Kindness

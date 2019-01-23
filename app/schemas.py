from extensions import marshmallow as ma
from app.models import Users, Kindness


class UserSchema(ma.ModelSchema):
    class Meta:
        model = Users


class KindnessSchema(ma.ModelSchema):
    class Meta:
        model = Kindness

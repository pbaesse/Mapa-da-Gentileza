from marshmallow import fields
from extensions import marshmallow as ma
from app.models import Users, Kindness, Tags


class UserSchema(ma.ModelSchema):
    posts = fields.Nested('KindnessSchema', many=True, exclude=('user_id',))
    class Meta:
        model = Users


class KindnessSchema(ma.ModelSchema):
    user = fields.Nested(UserSchema)
    #tags = fields.Nested('TagsSchema', many=True)
    class Meta:
        model = Kindness

#corrigir isso aqui.
class TagsSchema(ma.ModelSchema):
    kindness = fields.Nested(KindnessSchema)
    class Meta:
        model = Tags

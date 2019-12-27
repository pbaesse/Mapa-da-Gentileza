from marshmallow import fields
from extensions import marshmallow as ma
from app.models import Users, Kindness, Tags


class UserSchema(ma.ModelSchema):
    class Meta:
        model = Users
        exclude = ('password_hash', 'auth_token', 'device_ip_register', 'count_logins',
                   'date_last_login_failed', 'date_last_change_pass', 'count_logins_failed',
                   'confirmed', 'posts',)


class KindnessSchema(ma.ModelSchema):
    user = fields.Nested(UserSchema)
    class Meta:
        model = Kindness
        fields = ('id_kindness', 'identifier', 'title', 'latitude', 'longitude',)

#corrigir isso aqui.
class TagsSchema(ma.ModelSchema):
    class Meta:
        model = Tags


class KindnessDetailSchema(ma.ModelSchema):
    class Meta:
        model = Kindness
        

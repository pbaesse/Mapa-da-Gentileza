from app.models import Tags
from extensions import db


class TagsController:

    def save_new_tag(self):
        pass

    def get_tags(self):
        return Tags.query.all()

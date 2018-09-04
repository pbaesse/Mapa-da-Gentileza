import uuid
from app.models import Kindness, Tags
from extensions import db


class KindnessController:

    def save_new_kindness(self, kindness):
        received_data = [
            kindness.body, kindness.latitude,
            kindness.longitude, kindness.user_id,
            kindness.title
        ]

        if all(received_data):
            kindness.identifier = str(uuid.uuid1())
            db.session.add(kindness)
            db.session.commit()

            db.session.refresh(kindness)
            return kindness.id_kindness

    def delete_kindness(self, kindness_identifier):
        Kindness.query.filter_by(identifier=kindness_identifier).delete()
        db.session.commit()

    def update_kindness(self, kindness_up, kindness_identifier):
        kindness = Kindness.query.filter_by(identifier=kindness_identifier)
        kindness.title = kindness_up.title
        kindness.body = kindness_up.body
        kindness.latitude = kindness_up.latitude
        kindness.longitude = kindness_up.longitude
        db.session.commit()

    def save_kindness_tags(self, kindness, tags):
        pass

from uuid
from app.models import Kindness, Kindness_Files
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

    def delete_kindness(self, kindness_identifier):
        Kindness.query.filter_by(identifier=kindness_identifier).delete()
        db.session.commit()

    def update_kindness(self, kindness):
        pass

    def upload_file_kindness(self, kindness_file):
        pass


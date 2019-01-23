import uuid
from app.models import Kindness, Tags
from app.exceptions import CreateKindnessException
from app.controllers.files_controller import FilesController
from extensions import db


class KindnessController:

    def save_new_kindness(self, kindness, tags, image=None):
        try:
            kind_files = None

            if image is not None:
                kind_files = self.upload_kindness_image(post_image=image)

            kindness.identifier = str(uuid.uuid1())
            db.session.add(kindness)
            db.session.commit()

            db.session.refresh(kindness)
            id_kindness = kindness.id_kindness
            self.save_kindness_tags(id_kindness=id_kindness, id_tags=tags)

            if kind_files is not None:
                kind_files.id_kindness = id_kindness
                db.session.add(kind)
                db.session.commit()
            return id_kindness
        except Exception as ex:
            raise CreateKindnessException("Erro ao salvar o post. {}".format(ex))


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

    def save_kindness_tags(self, id_kindness, id_tags):
        kindness = Kindness.query.filter_by(id_kindness=id_kindness).first()
        tags = Tags.query.filter_by(id=id_tags).first()
        kindness.tags = [tags]
        db.session.commit()

    def upload_kindness_image(self, post_image):
        try:
            files = FilesController()
            kind_files = files.save_image(files=post_image, type_upload="img_kindness")
            return kind_files
        except Exception as e:
            raise e

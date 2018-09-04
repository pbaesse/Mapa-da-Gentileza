import os
import uuid
from app.models import Kindness_Files
from extensions import photos, db


class KindnessFilesController:


    @staticmethod
    def save_image(image, id_kindness):
        filename = photos.save(image)
        extension = filename.split('.')[-1]
        kind_image = Kindness_Files(file_path=filename, file_extension=extension, id_kindness=id_kindness)
        db.session.add(kind_image)
        db.session.commit()


    def get_meta_data(self):
        pass

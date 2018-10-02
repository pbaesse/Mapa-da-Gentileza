import os
import uuid
from flask import send_from_directory
from dynaconf import settings
from app.models import Kindness_Files
from extensions import db


class FilesController:


    def save_image(self, files, type_upload, id_kindness=None, id_user=None):
        images = self.process_files(files, type_upload)
        for image in images:
            files.save(image)
            if type_upload == "img_profile":
                users = Users()
            kind = Kindness_Files(file_path=image, extension="png", id_kindness=id_kindness)
            db.session.add(kind)
            db.session.commit()


    def get_meta_data(self):
        pass

    @staticmethod
    def convert():
        image = send_from_directory(settings.get('UPLOADED_PHOTOS_DEST'), "eueu.jpg")
        print("Imagem {} ".format(image))
        print("Filename {} ".format(filename))

    def process_files(self, files, type_upload):
        images = []
        for f in files:
            filename = f.filename
            if type_upload == "img_profile":
                images.append("/".join([settings.get('UPLOAD_USERS_FOLDER'), filename]))
            images.append("/".join([settings.get('UPLOAD_KINDNESS_FOLDER'), filename]))
        return images

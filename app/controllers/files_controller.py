import os
import uuid
from flask import send_from_directory
from werkzeug.utils import secure_filename
from dynaconf import settings
from app.models import Kindness_Files
from app.exceptions import UploadImageException
from extensions import db


class FilesController:

    #Fazer com que esse método pare de retonar um objeto e retorne apenas o filename e extension
    def save_image(self, files, type_upload, id_user=None):
        try:

            filename, extension = self.get_meta_data(files=files)

            if type_upload == "img_profile":
                if files.save(os.path.join(settings.get('UPLOAD_USERS_FOLDER'), filename)):
                    return filename
            elif type_upload == "img_kindness":
                if files.save(os.path.join(settings.get('UPLOAD_KINDNESS_FOLDER'), filename)):
                    return Kindness_Files(file_path=filename, file_extension=extension)
        except Exception as ex:
            raise UploadImageException("Erro ao salvar a imagem")


    def get_meta_data(self, files):
        try:
            extension = files.filename.split(".")[1]
            filename = str(uuid.uuid1())+"."+extension
            return filename, extension
        except Exception as e:
            raise Exception("OOOOOOOpsssSSSS")

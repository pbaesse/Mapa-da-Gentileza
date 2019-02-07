import os
import uuid
from dynaconf import settings
from app.models import Kindness_Files
from app.exceptions import UploadImageException


class FilesController:

    #Fazer com que esse método pare de retonar um objeto e retorne apenas o filename e extension
    def save_image(self, files, type_upload, id_user=None):
        print("CHAMOU SAVE IMAGE")
        extension = files.filename.split(".")[1]
        filename = str(uuid.uuid1())+"."+extension
        print("FIRST FILENAME IN SAVE IMAGE: {}".format(filename))
        if type_upload == "img_profile":
            files.save(os.path.join(settings.get('UPLOAD_USERS_FOLDER'), filename))
            print("FILENAME IN SAVE IMAGE: {}".format(filename))
            return filename


    def get_meta_data(self, files):
        try:
            extension = files.filename.split(".")[1]
            filename = str(uuid.uuid1())+"."+extension
            return filename, extension
        except Exception as e:
            raise Exception("OOOOOOOpsssSSSS")


"""
elif type_upload == "img_kindness":
if files.save(os.path.join(settings.get('UPLOAD_KINDNESS_FOLDER'), filename)):
    return Kindness_Files(file_path=filename, file_extension=extension)
"""

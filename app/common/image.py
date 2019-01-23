from flask import Blueprint, send_from_directory
from dynaconf import settings


bp_images = Blueprint('images', __name__, url_prefix='/uploads')

"""
@bp_images.route("/users_images/<path:filename>")
def get_image(filename):
    return send_from_directory(settings.get('UPLOAD_USERS_FOLDER'), filename)

def convert_to_base64(filename):
    image = send_from_directory(settings.get('UPLOADED_PHOTOS_DEST'), filename)
    print("Imagem {} ".format(image))
    print("Filename {} ".format(filename))
    return "dvsbsbsbsb"

def configure(app):
    app.register_blueprint(bp_images)
"""

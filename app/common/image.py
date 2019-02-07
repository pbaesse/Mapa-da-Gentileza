from flask import Blueprint, send_from_directory, current_app
from dynaconf import settings


bp_images = Blueprint('images', __name__,)

"""
@bp_images.route("/media/<path:filename>")
def media(filename):
    return send_from_directory(current_app.config.get('MEDIA_ROOT'), filename)

def convert_to_base64(filename):
    image = send_from_directory(settings.get('UPLOADED_PHOTOS_DEST'), filename)
    print("Imagem {} ".format(image))
    print("Filename {} ".format(filename))
    return "dvsbsbsbsb"

def configure(app):
    app.register_blueprint(bp_images)
"""

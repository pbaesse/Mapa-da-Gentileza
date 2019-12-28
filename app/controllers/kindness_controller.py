import math
import uuid
from app.models import Kindness, Tags
from app.exceptions import CreateKindnessException
from app.controllers.files_controller import FilesController
from app.util.geolocation import GeoLocation
from extensions import db


class KindnessController:

    def save_new_kindness(self, title, body, latitude, longitude, id_user, tags, image=None):
        try:
            kind_files = None

            if image is not None:
                kind_files.file_path = self.upload_kindness_image(post_image=image)


            kindness = Kindness(title=title, body=body, latitude=latitude, longitude=longitude, user_id=id_user)
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

    def update_kindness(self, title, body, latitude, longitude, kindness_identifier):
        kindness_to_update = Kindness.query.filter_by(identifier=kindness_identifier)
        kindness_to_update.title = title
        kindness_to_update.body = body
        kindness_to_update.latitude = latitude
        kindness_to_update.longitude = longitude
        db.session.commit()


    def get_kindness_by_location(self, user_latitude, user_longitude):

        search_radius = 500
        earth_radius = 6371
        angular_radius = search_radius/earth_radius

        lat_min = user_latitude - angular_radius
        lat_max = user_latitude + angular_radius

        delta_lon = math.asin(math.sin(math.radians(angular_radius)) / math.cos(user_latitude))

        lon_min = user_longitude - delta_lon
        lon_max = user_longitude + delta_lon


        query = ('SELECT id_kindness, identifier, title, latitude, longitude FROM Kindness '
                 'WHERE (latitude >= '+str(lat_min)+' AND latitude <= '+str(lat_max)+') AND '
                 '(longitude >= '+str(lon_min)+' AND longitude <= '+str(lon_max)+') AND '
                 'acos(sin('+str(user_latitude)+') * sin(latitude) + cos('+str(user_latitude)+') * '
                 'cos(latitude) * cos(longitude - ('+str(user_longitude)+'))) <= '+str(angular_radius))

        res = db.session.execute(query)

        kindness_list = []

        for row in res:
            kindness = Kindness(id_kindness=row.id_kindness, identifier=row.identifier, title=row.title,
                                latitude=row.latitude, longitude=row.longitude)

            kindness_list.append(kindness)

        return kindness_list


    def get_kindness_by_id(self, id_kindness):
        return Kindness.query.filter_by(id_kindness=id_kindness).first()

    def save_kindness_tags(self, id_kindness, id_tags):
        tags = []

        kindness = Kindness.query.filter_by(id_kindness=id_kindness).first()

        for id in id_tags:
            tag = Tags.query.filter_by(id=id).first()
            tags.append(tag)

        kindness.tags = tags
        db.session.commit()

    def upload_kindness_image(self, post_image):
        try:
            files = FilesController()
            filename = files.save_image(files=post_image, type_upload="img_kindness")
            return filename
        except Exception as e:
            raise e

from app.models import Kindness, Kindness_Files


class KindnessController:

    def save_new_kindness(self, kindness):
    	received_data = [
    		kindness.body, kindness.latitude, 
    		kindness.longitude, kindness.user_id,
    		kindness.unnamed
    	]

    	if all(received_data):
    		kindness.save()

    def delete_kindness(self, kindness):
        pass

    def update_kindness(self, kindness):
        pass

    def get_all_kindness(self):
        return Kindness.query.all()

    def get_kindness_by_id(self, id):
        return kindness.query.filter_by_id(id=id).first()

    def upload_file_kindness(self, kindness_file):
        pass

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField, SelectField, RadioField, HiddenField
from wtforms.validators import DataRequired, ValidationError
from app.models import Tags


class NewKindnessForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired()])
	body = TextAreaField('Body', validators=[DataRequired()])
	tags = SelectField('Tags', coerce=int, validators=[DataRequired()])
	latitude = HiddenField('latitude')
	longitude = HiddenField('longitude')
	#unnamed = RadioField('Unnamed', choices=[('True', 'Unnamed')])
	file = FileField('Image')
	save_post = SubmitField('Post')


class UpdateKindnessForm(FlaskForm):
	pass

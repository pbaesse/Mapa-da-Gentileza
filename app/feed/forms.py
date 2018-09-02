from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField, SelectField, RadioField, HiddenField
from wtforms.validators import DataRequired, ValidationError
from extensions import photos


class NewKindnessForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired()])
	body = TextAreaField('Body', validators=[DataRequired()])
	#tags = SelectField('Tags', choices=[('1', 'Tag1'), ('2','Tag2'), ('3','Tag3')])
	#unnamed = RadioField('Unnamed', choices=[('True', 'Unnamed')])
	#files = FileField('Images', validators=[FileAllowed(photos, "Images only!!")])
	save_post = SubmitField('Post')


class UpdateKindnessForm(FlaskForm):
	pass

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, RadioField
from wtforms.validators import DataRequired, ValidationError


class NewKindnessForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired()])
	body = TextAreaField('Body', validators=[DataRequired()])
	#tags = SelectField('Tags', choices=[('1', 'Tag1'), ('2','Tag2'), ('3','Tag3')])
	#unnamed = RadioField('Unnamed', choices=[('True', 'Unnamed')])
	save_post = SubmitField('Post')
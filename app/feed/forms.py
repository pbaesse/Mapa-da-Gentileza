from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, RadioField
from wtforms.validators import DataRequired, ValidationError


class NewKindnessForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired()])
	body = TextAreaField('Body', validators=[DataRequired()])
	tags = SelectField('Tags', choices=[('Teste1'), ('Teste2'), ('Teste3')])
	unnamed = RadioField('Unnamed', choices=[('True', 'Unnamed')])
	post = SubmitField('Post')
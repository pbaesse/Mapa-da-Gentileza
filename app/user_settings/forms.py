from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DateField, TextAreaField
from wtforms.file import FileField
from wtforms.validators import Email, EqualTo, DataRequired, ValidationError
from app.models import Users


class UpdatePassword(FlaskForm):
	old_password = PasswordField('Old password', validators=[DataRequired()])
	new_password = PasswordField('New password', validators=[DataRequired()])
	update = SubmitField('Update')


class UpdateProfile(FlaskForm):
	first_name = StringField('First name', validators=[DataRequired()])
	last_name = StringField('Last name')
	about_me = TextAreaField('Biography')
	avatar = FileField()
	birthday = StringField('Day', validators=[DataRequired()])
	#substituir por select com os meses existentes.
	month_birth = StringField('Month', validators=[DataRequired()])
	year_birth = StringField('Year', validators=[DataRequired()])
	update = SubmitField('Update')
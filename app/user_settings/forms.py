from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DateField, TextAreaField, FileField
#from wtforms.file import FileField
from wtforms.validators import Email, EqualTo, DataRequired, ValidationError
from app.models import Users


class UpdatePasswordForm(FlaskForm):
    old_password = PasswordField('Old password', validators=[DataRequired()])
    new_password = PasswordField('New password', validators=[DataRequired()])
    update = SubmitField('Update')


class UpdateProfileForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name')
    about_me = TextAreaField('Biography')
    avatar = FileField('Avatar')
    #birthday = StringField('Day', validators=[DataRequired()])
    # substituir por select com os meses existentes.
    #month_birth = StringField('Month', validators=[DataRequired()])
    #year_birth = StringField('Year', validators=[DataRequired()])
    update = SubmitField('Update')

    def __init__(self, current_username, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)
        self.current_username = current_username

    def validate_username(self, username):
        if username.data != self.current_username:
            user = Users.query.filter_by(username=self.username.data).first()
            if user is not None:
                pass
                # mensagem de erro de username existente.

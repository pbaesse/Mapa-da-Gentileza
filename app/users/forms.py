from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DateField, TextAreaField, FileField
#from wtforms.file import FileField
from wtforms.validators import Email, EqualTo, DataRequired, ValidationError
from app.models import Users


class SearchUserForm(FlaskForm):
    search = StringField('Digite sua busca')
    send = SubmitField('Buscar')


class UpdatePasswordForm(FlaskForm):
    old_password = PasswordField('Old password', validators=[DataRequired()])
    new_password = PasswordField('New password', validators=[DataRequired()])
    update = SubmitField('Update')


class UpdateProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name')
    about_me = TextAreaField('Biography')
    status = StringField('Status')
    phone = StringField('Phone')
    avatar = FileField('Avatar')
    birthday = StringField('Day')
    month_birth = SelectField('Month', choices=[('01', 'January'), ('02', 'February'), ('03', 'March'), ('04', 'April'), ('05', 'May'), ('06', 'June'), (
        '07', 'July'), ('08', 'August'), ('09', 'September'), ('10', 'October'),
        ('11', 'November'), ('12', 'December')])
    year_birth = StringField('Year')
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
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DateField
from wtforms.validators import Email, EqualTo, DataRequired, ValidationError
from app.models import Users


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    #genre = SelectField(choices=[('Masculine', 'Masculine'), ('Feminine', 'Feminine'), ('Other', 'Other')])
    date_birth = DateField('Date Birth', validators=[DataRequired()])
    signUp = SubmitField('Sign Up')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('New password', validators=[DataRequired()])
    password_confirm = PasswordField('Repeat password', validators=[
                                     DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset')


class RequestResetPasswordForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    send = SubmitField('Send')
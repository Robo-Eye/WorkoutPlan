from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, EqualTo, Length, Email

class LoginForm(FlaskForm):
    username = StringField("Username: ", validators=[InputRequired()])
    password = PasswordField("Password: ", validators=[InputRequired()])

    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    username = StringField("Username: ", validators=[InputRequired()])
    email = EmailField("Email: ", validators=[InputRequired(), Email()])
    password = PasswordField("Password: ", validators=[InputRequired(), Length(min=8, max=256)])
    confirm_password = PasswordField("Confirm Password: ", validators=[InputRequired(), EqualTo("password")])

    submit = SubmitField("Register")

class UpdateInfo(FlaskForm):
    email = EmailField("Old Email: ", validators=[InputRequired(), Email()])
    newEmail = EmailField("New Email: ", validators=[InputRequired(), Email()])
    submit = SubmitField("Update")

class UpdateUsername(FlaskForm):
    username = StringField("Old Username: ", validators=[InputRequired()])
    newUsername = StringField("New Username: ", validators=[InputRequired()])
    submit = SubmitField("Update")

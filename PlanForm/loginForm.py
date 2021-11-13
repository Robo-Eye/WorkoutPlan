from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired

class LoginForm(FlaskForm):
    username = StringField("Username: ", validators=[InputRequired()])
    password = PasswordField("Password: ", validators=[InputRequired()])

    submit = SubmitField("Submit")

class RegisterForm(FlaskForm):
    username = StringField("Username: ", validators=[InputRequired()])
    password = PasswordField("Password: ", validators=[InputRequired()])
    confirm_password = PasswordField("Confirm Password: ", validators=[InputRequired()])
    email = EmailField("Email: ", validators=[InputRequired()])

    submit = SubmitField("Submit")
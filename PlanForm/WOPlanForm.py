import enum
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.core import IntegerField, SelectField
from wtforms.validators import InputRequired

# gender, age, weight, height, area of focus, goals, time frame

# having issues with this and sending an arguement to it


class WorkoutForm(FlaskForm):
    # consider reworking/looking at gender
    gender = SelectField("Gender: ", choices=[('Male', 'Male'), (
        'Female', 'Female')], validators=[InputRequired()])
    age = IntegerField("Age: ", validators=[InputRequired()])
    weight = IntegerField("Weight: ", validators=[InputRequired()])
    height = IntegerField("Height: ", validators=[InputRequired()])
    areaOfFocus = SelectField("Area of Focus: ", validators=[InputRequired()])
    goals = SelectField("Goals: ", validators=[InputRequired()])
    timeline = SelectField("Timeline: ", validators=[InputRequired()])
    submit = SubmitField("Submit")

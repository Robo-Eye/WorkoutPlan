import enum
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.core import SelectField
from wtforms.validators import InputRequired

# gender, age, weight, height, area of focus, goals, time frame


class Gender(enum.Enum):
    Male = 'Male'
    Female = 'Female'
    PreferNotToSay = 'Prefer Not To Say'

    def __str__(self):
        return self.value


choices = [
    (str(choice), choice) for choice in Gender
]


class WorkoutForm(FlaskForm):
    gender = SelectField("Gender: ", Options=choices,
                         validators=[InputRequired()])

from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.fields.core import IntegerField, SelectField
from wtforms.validators import InputRequired


class WorkoutForm(FlaskForm):
    gender = SelectField("Gender: ", choices=[('', 'Select a Gender'), ('Male', 'Male'), (
        'Female', 'Female')], validators=[InputRequired()])
    age = IntegerField("Age: ", validators=[InputRequired()])
    weight = IntegerField("Weight (in lbs): ", validators=[InputRequired()])
    height = IntegerField("Height (in inches): ", validators=[InputRequired()])
    areaOfFocus = SelectField("Area of Focus: ", choices=[('', 'Select an Area of Focus'), ('Abs', 'Core Improvement'), ('Chest', 'Chest'), (
        'Shoulders', 'Shoulders'), ('Back', 'Back'), ('Biceps', 'Biceps'), ('Triceps', 'Triceps'), ('Legs', 'Legs'), ('Cardio', 'Cardio')], validators=[InputRequired()])
    goals = SelectField("Goals: ", choices=[('', 'Select a Goal'), ('Endurance', 'Increase Endurance'), (
        'Strength', 'Increase Strength'), ('Bodybuilding', 'Bodybuilding')], validators=[InputRequired()])
    frequency = SelectField("Times per week: ", choices=[
                            ('', 'Select a Frequency'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], validators=[InputRequired()])
    submit = SubmitField("Submit")

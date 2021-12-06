from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.fields.core import FloatField, IntegerField, SelectField, SelectMultipleField
from wtforms.validators import InputRequired, NumberRange


class WorkoutForm(FlaskForm):
    gender = SelectField("Gender: ", choices=[('', 'Select a Gender'), ('Male', 'Male'), (
        'Female', 'Female')], validators=[InputRequired()])
    age = IntegerField("Age: ", validators=[InputRequired()])
    weight = FloatField("Weight (in lbs): ", validators=[
                        InputRequired(), NumberRange(min=50, max=800, message="Please enter a reasonable weight (50lbs to 800lbs)")])
    height = FloatField("Height (in inches): ", validators=[
                        InputRequired(), NumberRange(min=36, max=108,  message="Please enter a reasonable height (36in to 108in)")])
    areaOfFocus = SelectMultipleField("Area of Focus: ", choices=[('', 'Select an Area of Focus'), ('Abs', 'Core Improvement'), ('Chest', 'Chest'), (
        'Shoulders', 'Shoulders'), ('Back', 'Back'), ('Biceps', 'Biceps'), ('Triceps', 'Triceps'), ('Legs', 'Legs')], validators=[InputRequired()])
    goals = SelectField("Goals: ", choices=[('', 'Select a Goal'), ('16', 'Increase Endurance'), ('12', 'Bodybuilding'),  (
        '8', 'Increase Strength')], validators=[InputRequired()])
    numberofsets = SelectField("Number of Sets ", choices=[
        ('', 'Select Number of Sets'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], validators=[InputRequired()])
    submit = SubmitField("Submit")

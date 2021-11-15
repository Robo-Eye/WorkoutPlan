import flask
import os
from WOPlanForm import WorkoutForm
from flask.app import Flask
from flask import render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy

scriptdir = os.path.abspath(os.path.dirname(__file__))
dbpath = os.path.join(scriptdir, 'workoutPlan.sqlite3')

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SECRET_KEY'] = 'RandomPhraseToKeepItSafe'
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{dbpath}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


class UserForm(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # Genders parameter throwing and error
    gender = db.Column(db.Unicode, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    areaOfFocus = db.Column(db.Unicode, nullable=False)
    goals = db.Column(db.Unicode, nullable=False)
    timeline = db.Column(db.Integer, nullable=False)


@app.get('/workoutform/')
def get_blank_form():
    wf = WorkoutForm()
    return render_template("newplan.j2", wf=wf)

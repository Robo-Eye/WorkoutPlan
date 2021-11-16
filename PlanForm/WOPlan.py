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
    gender = db.Column(db.Unicode, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    areaOfFocus = db.Column(db.Unicode, nullable=False)
    goals = db.Column(db.Unicode, nullable=False)
    frequency = db.Column(db.Integer, nullable=False)


@app.get('/workoutform/')
def get_blank_form():
    wf = WorkoutForm()
    return render_template("newplan.j2", wf=wf)


@app.post('/workoutform/')
def post_blank_form():
    wf = WorkoutForm()
    if wf.validate():
        completed_form = UserForm(gender=wf.gender.data, age=wf.age.data,
                                  weight=wf.weight.data, height=wf.height.data,
                                  areaOfFocus=wf.areaOfFocus.data, goals=wf.goals.data,
                                  frequency=wf.frequency.data)
        db.session.add(completed_form)
        db.session.commit()
        return redirect(url_for("get_completed_form"))
    else:
        for field, error in wf.errors.items():
            flash(f"{field}: {error}")
        return redirect(url_for("get_blank_form"))


@app.get('/completedform/')
def get_completed_form():
    wf = WorkoutForm()
    pass

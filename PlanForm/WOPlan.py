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


class Abs(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    workouts = db.Column(db.Unicode)
    link_to_wo = db.Column(db.Unicode)


class Chest(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    workouts = db.Column(db.Unicode)
    link_to_wo = db.Column(db.Unicode)


class Shoulders(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    workouts = db.Column(db.Unicode)
    link_to_wo = db.Column(db.Unicode)


class Back(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    workouts = db.Column(db.Unicode)
    link_to_wo = db.Column(db.Unicode)


class Biceps(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    workouts = db.Column(db.Unicode)
    link_to_wo = db.Column(db.Unicode)


class Triceps(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    workouts = db.Column(db.Unicode)
    link_to_wo = db.Column(db.Unicode)


class Legs(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    workouts = db.Column(db.Unicode)
    link_to_wo = db.Column(db.Unicode)


db.drop_all()
db.create_all()

multiple_abs = [
    Abs(workouts="Ab crunches",
        link_to_wo="https://www.youtube.com/watch?v=Xyd_fa5zoEU"),
    Abs(workouts="Russian twists",
        link_to_wo="https://www.youtube.com/watch?v=JyUqwkVpsi8"),
    Abs(workouts="Plank hold",
        link_to_wo="https://www.youtube.com/watch?v=Oi9pmH45W7A"),
    Abs(workouts="Leg raises",
        link_to_wo="https://www.youtube.com/watch?v=ttdkm6ESUjI"),
    Abs(workouts="Knee raises",
        link_to_wo="https://www.youtube.com/watch?v=KNzJ3GuIpB8")
]
db.session.add_all(multiple_abs)
db.session.commit()
multiple_chest = [
    Chest(workouts="Flat barbell bench press",
          link_to_wo="https://www.youtube.com/watch?v=-MAABwVKxok"),
    Chest(workouts="Dumbbell chest fly",
          link_to_wo="https://youtu.be/eozdVDA78K0"),
    Chest(workouts="Dumbbell pullover",
          link_to_wo="https://youtu.be/tpLnfSQJ0gg"),
    Chest(workouts="Flat machine bench press",
          link_to_wo="https://youtu.be/xUm0BiZCWlQ"),
    Chest(workouts="Cable crossover",
          link_to_wo="https://www.youtube.com/watch?v=taI4XduLpTk")
]
db.session.add_all(multiple_chest)
db.session.commit()
multiple_shoulders = [
    Shoulders(workouts="Seated barbell shoulder press",
              link_to_wo="https://www.youtube.com/watch?t=4s&v=oBGeXxnigsQ"),
    Shoulders(workouts="Seated dumbbell shoulder press",
              link_to_wo="https://youtu.be/qEwKCR5JCog"),
    Shoulders(workouts="Arnold press",
              link_to_wo="https://youtu.be/6Z15_WdXmVw"),
    Shoulders(workouts="Dumbbell lateral raises",
              link_to_wo="https://youtu.be/3VcKaXpzqRo"),
    Shoulders(workouts="Machine shoulder press",
              link_to_wo="https://www.youtube.com/watch?t=2s&v=Wqq43dKW1TU")
]
db.session.add_all(multiple_shoulders)
db.session.commit()

multiple_back = [
    Back(workouts="", link_to_wo=""),
    Back(workouts="", link_to_wo=""),
    Back(workouts="", link_to_wo=""),
    Back(workouts="", link_to_wo=""),
    Back(workouts="", link_to_wo="")
]
db.session.add_all(multiple_back)
db.session.commit()

multiple_biceps = [
    Biceps(workouts="", link_to_wo=""),
    Biceps(workouts="", link_to_wo=""),
    Biceps(workouts="", link_to_wo=""),
    Biceps(workouts="", link_to_wo=""),
    Biceps(workouts="", link_to_wo="")
]
db.session.add_all(multiple_biceps)
db.session.commit()

multiple_triceps = [
    Triceps(workouts="", link_to_wo=""),
    Triceps(workouts="", link_to_wo=""),
    Triceps(workouts="", link_to_wo=""),
    Triceps(workouts="", link_to_wo=""),
    Triceps(workouts="", link_to_wo="")
]
db.session.add_all(multiple_triceps)
db.session.commit()

multiple_legs = [
    Legs(workouts="", link_to_wo=""),
    Legs(workouts="", link_to_wo=""),
    Legs(workouts="", link_to_wo=""),
    Legs(workouts="", link_to_wo=""),
    Legs(workouts="", link_to_wo=""),
    Legs(workouts="", link_to_wo="")
]
db.session.add_all(multiple_legs)
db.session.commit()


@app.get('/workoutform/')
def get_blank_form():
    wf = WorkoutForm()
    return render_template("newplan.j2", wf=wf)


@app.post('/workoutform/')
def post_blank_form():
    wf = WorkoutForm()
    if wf.validate():
        str1 = " "
        areaOfFocusConvert = str1.join(wf.areaOfFocus.data)
        print(areaOfFocusConvert)
        completed_form = UserForm(gender=wf.gender.data, age=wf.age.data,
                                  weight=wf.weight.data, height=wf.height.data,
                                  areaOfFocus=areaOfFocusConvert, goals=wf.goals.data,
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
    return render_template("plancreated.j2", wf=wf)

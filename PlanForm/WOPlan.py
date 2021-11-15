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

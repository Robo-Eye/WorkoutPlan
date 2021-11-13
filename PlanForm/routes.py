from flask import Flask, request, render_template, redirect, url_for, flash

from dbAccess import db
from dbAccess import User
from loginForm import LoginForm

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SECRET_KEY'] = 'correcthorsebatterystaple'

import os, sys
script_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(script_dir)

@app.route("/")
def index():
    return redirect(url_for('register'))

@app.route("/register/", methods=["GET", "POST"])
def register():
    form = LoginForm()
    if request.method == "GET":
        return render_template("register.j2", form=form, loginLink=url_for('login'))
    elif request.method == "POST":
        if form.validate():
            db.session.add(User(username=form.username.data, password=form.password.data, email=form.email.data))
            db.session.commit()
            return redirect(url_for('login'))
        else:
            for field, error in form.errors.items():
                flash(f"{field}: {error}")
            return redirect(url_for('register'))


@app.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "GET":
        return render_template("login.j2", form=form, registerLink=url_for('register'))
    elif request.method == "POST":
        if form.validate():
                # TODO: check if user information matches; if does, log in and send to their profile
               return redirect(url_for('profile'))
        else:
            for field, error in form.errors.items():
                flash(f"{field}: {error}")
            return redirect(url_for('login'))


@app.route("/profile/")
def profile():
    pass

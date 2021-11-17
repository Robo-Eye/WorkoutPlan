from flask import Flask, request, render_template, redirect, url_for, flash
from flask_login import UserMixin, LoginManager, login_required
from flask_login.utils import login_user, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user
from sqlalchemy.orm.attributes import flag_modified

import os, sys
scriptdir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(scriptdir)

from loginForm import LoginForm
from loginForm import RegisterForm
from loginForm import UpdateInfo

from hashing_examples import UpdatedHasher


# get db and pepper file
dbfile = os.path.join(scriptdir, 'workoutPlan.sqlite3')
pepfile = os.path.join(scriptdir, "pepper.bin")

# get pepper key
with open(pepfile, 'rb') as fin:
    pepper_key = fin.read()

pwd_hasher = UpdatedHasher(pepper_key)

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SECRET_KEY'] = 'correcthorsebatterystaple'
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{dbfile}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# get db object
db = SQLAlchemy(app)

# LoginManager
app.login_manager = LoginManager()
app.login_manager.login_view = 'get_login'
@app.login_manager.user_loader
def load_user(uid):
    return User.query.get(int(uid))

class User(UserMixin, db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    password_hash = db.Column(db.LargeBinary)
    email = db.Column(db.Unicode, nullable=False)

    @property
    def password(self):
        raise AttributeError("password is a write-only attribute")
    @password.setter
    def password(self, pwd):
        self.password_hash = pwd_hasher.hash(pwd)
    
    def verify_password(self, pwd):
        return pwd_hasher.check(pwd, self.password_hash)

    def __str__(self):
        return f"User(id={self.id}, email={self.email})"
    def __repr__(self) -> str:
        return f"User({self.id})"

# # refresh db and add test data
# db.drop_all()
# db.create_all()

# user1 = User(password="meat", email="strawhat@grandline.com")
# user2 = User(password="light", email="misa@gmail.com")

# db.session.add_all((user1, user2))
# db.session.commit()



@app.route("/")
def index():
    return redirect(url_for('home'))

@app.get("/register/")
def get_register():
    form = RegisterForm()
    return render_template("register.j2", form=form, loginLink=url_for('get_login'))

@app.post("/register/")
def post_register():
    form = RegisterForm()
    if form.validate():
        # check if existing account has this email
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None:
            flash("This email is already in use")
            return redirect(url_for('get_reigster'))
        # username and email are both not already being used, create new user
        db.session.add(User(password=form.password.data, email=form.email.data))
        db.session.commit()
        return redirect(url_for('get_login'))
    else:
        for field, error in form.errors.items():
            flash(f"{field}: {error}")
        return redirect(url_for('get_register'))


@app.get("/login/")
def get_login():
    form = LoginForm()
    return render_template("login.j2", form=form, registerLink=url_for('get_register'))
    
@app.post("/login/")
def post_login():
    form = LoginForm()
    if form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        # if user with this email exists and password matches
        if user is not None and user.verify_password(form.password.data):
            # log in user using login_manager
            login_user(user)
            # redirect to page they wanted or to home page
            next = request.args.get("next")
            if next is None or not next.startswith('/'):
                next = url_for('loggedInHome')

            return redirect(next)
        # if user doesn't exist or password is wrong
        else:
            flash("Invalid email or password")
            return redirect(url_for('get_login'))

    else:
        for field, error in form.errors.items():
            flash(f"{field}: {error}")
        return redirect(url_for('get_login'))

@app.get('/logout/')
@login_required
def get_logout():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('index'))

@app.route("/home/")
def home():
    return render_template("home.j2", current_user=current_user)

@app.route("/Home/")
def loggedInHome():
    return render_template("loggedInHome.j2", current_user=current_user)

@app.route("/profile/")
def profile():
    return render_template("profile.j2")

@app.get("/changeInfo/")
def get_changeInfo():
    form = UpdateInfo()
    return render_template("updateInfo.j2", form=form)

@app.post("/changeInfo/")
def post_changeInfo():
    form = UpdateInfo()
    if form.validate():
        # check if existing account has this email
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            flash("The Old Email that was submitted does not match your acctount")
            return redirect(url_for('get_changeInfo'))
        # username and email are both not already being used, create new user
        user.email = form.newEmail.data
        db.session.commit()
        return render_template("profile.j2", form=form)
    else:
        for field, error in form.errors.items():
            flash(f"{field}: {error}")
        return redirect(url_for('get_changeInfo'))
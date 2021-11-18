from sqlalchemy.orm import relationship
from hashing_examples import UpdatedHasher
from loginForm import UpdateInfo
from loginForm import RegisterForm
from loginForm import LoginForm
from flask import Flask, request, render_template, redirect, url_for, flash
from flask_login import UserMixin, LoginManager, login_required
from flask_login.utils import login_user, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from WOPlanForm import WorkoutForm
from flask_login import current_user
from sqlalchemy.orm.attributes import flag_modified

import os
import sys
scriptdir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(scriptdir)


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


class UserForm(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gender = db.Column(db.Unicode, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    areaOfFocus = db.Column(db.Unicode, nullable=False)
    goals = db.Column(db.Unicode, nullable=False)
    frequency = db.Column(db.Integer, nullable=False)
    #workouts = relationship('Workouts', backref='userform')


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


class Workouts(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    abs = db.Column(db.Boolean)
    chest = db.Column(db.Boolean)
    back = db.Column(db.Boolean)
    biceps = db.Column(db.Boolean)
    triceps = db.Column(db.Boolean)
    shoulders = db.Column(db.Boolean)
    legs = db.Column(db.Boolean)
    #userform_id = db.Column(db.Integer, db.ForeignKey('workouts.id'))


db.drop_all()  # for testing
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
    Back(workouts="Sumo deadlift", link_to_wo="https://youtu.be/1v4r9hht_K4"),
    Back(workouts="Bent over rows", link_to_wo="https://youtu.be/9efgcAjQe7E"),
    Back(workouts="T-bar rows", link_to_wo="https://youtu.be/j3Igk5nyZE4"),
    Back(workouts="Single-arm rows", link_to_wo="https://youtu.be/pYcpY20QaE8"),
    Back(workouts="Lat pulldowns – wide grip",
         link_to_wo="https://youtu.be/CAwf7n6Luuc")
]
db.session.add_all(multiple_back)
db.session.commit()

multiple_biceps = [
    Biceps(workouts="E-Z bar bicep curl",
           link_to_wo="https://www.youtube.com/watch?v=zG2xJ0Q5QtI"),
    Biceps(workouts="Barbell preacher curl",
           link_to_wo="https://www.youtube.com/watch?v=nbcgEmZ0Be4"),
    Biceps(workouts="Dumbbell bicep curl",
           link_to_wo="https://youtu.be/sAq_ocpRh_I"),
    Biceps(workouts="Hammer curls", link_to_wo="https://youtu.be/zC3nLlEvin4"),
    Biceps(workouts="Incline bench dumbbell curl",
           link_to_wo="https://youtu.be/soxrZlIl35U")
]
db.session.add_all(multiple_biceps)
db.session.commit()

multiple_triceps = [
    Triceps(workouts="Close-grip bench press",
            link_to_wo="https://youtu.be/cXbSJHtjrQQ"),
    Triceps(workouts="Skull crushers",
            link_to_wo="https://youtu.be/QXzhjRnYRT0"),
    Triceps(workouts="Seated overhead extension",
            link_to_wo="https://youtu.be/YbX7Wd8jQ-Q"),
    Triceps(workouts="Tricep kickbacks",
            link_to_wo="https://www.youtube.com/watch?v=bxPoVw8_khE"),
    Triceps(workouts="Close grip pushups",
            link_to_wo="https://www.youtube.com/watch?v=yy_stTZs5-4)")
]
db.session.add_all(multiple_triceps)
db.session.commit()

multiple_legs = [
    Legs(workouts="Barbell back squats",
         link_to_wo="https://youtu.be/1oed-UmAxFs"),
    Legs(workouts="Dumbbell Bulgarian split squat",
         link_to_wo="https://youtu.be/2C-uNgKwPLE"),
    Legs(workouts="Standing calf raises",
         link_to_wo="https://www.youtube.com/watch?v=wxwY7GXxL4k"),
    Legs(workouts="Leg press", link_to_wo="https://youtu.be/IZxyjW7MPJQ"),
    Legs(workouts="Leg extension",
         link_to_wo="https://www.youtube.com/watch?t=21s&v=YyvSfVjQeL0")
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
    selectedAOF = db.session.query(UserForm.areaOfFocus).all()
    stringAOF = selectedAOF[0]
    stringAOF = stringAOF[0]
    resultAOF = stringAOF.split()
    abs = False
    chest = False
    back = False
    biceps = False
    triceps = False
    shoulders = False
    legs = False
    for x in resultAOF:
        if (x.lower() == "abs"):
            abs = True
        if (x.lower() == "chest"):
            chest = True
        if (x.lower() == "back"):
            back = True
        if (x.lower() == "biceps"):
            biceps = True
        if (x.lower() == "triceps"):
            triceps = True
        if (x.lower() == "shoulders"):
            shoulders = True
        if (x.lower() == "legs"):
            legs = True
    completed_form = Workouts(abs=abs, chest=chest, back=back,
                              biceps=biceps, triceps=triceps, shoulders=shoulders, legs=legs)
    db.session.add(completed_form)
    db.session.commit()
    listAOF = ((abs, "abs"), (chest, "chest"), (back, "back"), (biceps, "biceps"),
               (triceps, "triceps"), (shoulders, "shoulders"), (legs, "legs"))
    return render_template("plancreated.j2", wf=wf, listAOF=listAOF)


@app.post('/completedform/')
def post_completed_form():
    pass


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
        db.session.add(
            User(password=form.password.data, email=form.email.data))
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

@app.route("/workouts/")
def workoutlist():
    return

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

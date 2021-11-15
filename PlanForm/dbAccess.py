import os
from datetime import date
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

scriptdir = os.path.abspath(os.path.dirname(__file__))
dbpath = os.path.join(scriptdir, 'workoutPlan.sqlite3')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{dbpath}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'Users'
    username = db.Column(db.Unicode, primary_key=True)
    password = db.Column(db.Unicode, nullable=False)
    email = db.Column(db.Unicode, nullable=False)

    def __str__(self):
        return f"User(username={self.username}, email={self.email})"

    def __repr__(self) -> str:
        return f"User({self.username})"


# refresh db and add test data
db.drop_all()
db.create_all()

user1 = User(username="luffy", password="meat", email="strawhat@grandline.com")
user2 = User(username="misa", password="light", email="misa@gmail.com")

db.session.add_all((user1, user2))
db.session.commit()

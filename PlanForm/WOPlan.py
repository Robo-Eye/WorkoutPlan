import flask
from flask.app import Flask
from flask import render_template, request, url_for, redirect, flash

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SECRET_KEY'] = 'RandomPhraseToKeepItSafe'


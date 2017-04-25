import os

from flask import Flask, render_template

from models import Patient, Doctor, db

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/')
def home():
    context = {"title": "Doctors and Patients", "patients": Patient.query.all(), "doctors": Doctor.query.all()}
    return render_template('index.html', **context)

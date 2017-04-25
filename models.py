from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Patient(db.Model):
    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Patient {}>'.format(self.name)


class Doctor(db.Model):
    __tablename__ = 'doctors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    speciality = db.Column(db.String())

    def __init__(self, name, speciality):
        self.name = name
        self.speciality = speciality

    def __repr__(self):
        return '<Doctor {}>'.format(self.name)

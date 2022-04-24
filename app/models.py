from email.policy import default
from sqlalchemy.orm import backref
from app import db


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    collaborators = db.relationship('Collaborator', backref='department', lazy=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Department %r>' % self.name


class Collaborator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(40), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    dependents = db.Column(db.Integer, default=0, nullable=False)

    def __init__(self, full_name, department_id, dependents):
        self.full_name = full_name
        self.department_id = department_id
        self.dependents = dependents

    def __repr__(self):
        return 'Collaborator %r' % self.full_name

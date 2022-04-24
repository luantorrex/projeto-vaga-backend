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
    have_dependents = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, full_name, department, have_dependents):
        self.full_name = full_name
        self.department = department
        self.have_dependents = have_dependents

    def __repr__(self):
        return 'Collaborator %r' % self.full_name

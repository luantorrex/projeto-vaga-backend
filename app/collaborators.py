from app import db
from app.models import Collaborator, Department


def list_all():
    collaborators_table = Collaborator.query.all()
    collaborators_dict = {}

    for collaborator in collaborators_table:

        have_dependents = True if collaborator.dependents > 0 else False
        
        collaborators_dict[collaborator.id] = {
            'full_name': collaborator.full_name,
            'department': collaborator.department_id,
            'have_dependents': have_dependents
        }

    return collaborators_dict


def register(data):
    full_name = data['full_name']
    dependents = data['dependents']
    department_id = data['department_id']

    department_exists = Department.query.filter_by(id=department_id).first()
    
    if not department_exists:
        return int(department_id)

    collaborator = Collaborator(full_name=full_name, dependents=dependents, department_id=department_id)
    
    db.session.add(collaborator)
    db.session.commit()

    return full_name

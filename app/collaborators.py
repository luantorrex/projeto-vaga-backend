from app import db
from app.models import Collaborator, Department
from app.departments import check_if_department_exists


def list_per_department(department_id):
    if not check_if_department_exists(department_id):
        return int(department_id)

    collaborators_table = Collaborator.query.filter_by(department_id=department_id)
    collaborators_dict = {}

    for collaborator in collaborators_table:

        have_dependents = True if collaborator.dependents > 0 else False
        
        collaborators_dict[collaborator.id] = {
            'full_name': collaborator.full_name,
            'have_dependents': have_dependents
        }

    return collaborators_dict


def register(data):
    full_name = data['full_name']
    dependents = data['dependents']
    department_id = data['department_id']

    if not check_if_department_exists(department_id):
        return int(department_id)

    collaborator = Collaborator(full_name=full_name, dependents=dependents, department_id=department_id)
    
    db.session.add(collaborator)
    db.session.commit()

    return full_name

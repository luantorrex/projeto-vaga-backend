from app import db
from app.models import Department


def list_all():
    departments_table = Department.query.all()
    departments_dict = {}

    for department in departments_table:
        departments_dict[department.id] = {
            'name': department.name
        }

    return departments_dict


def register(data):
    department_name = data['name']
    department = Department(name=department_name)
    
    db.session.add(department)
    db.session.commit()

    return department_name

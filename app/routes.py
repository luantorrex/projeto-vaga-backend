from crypt import methods
from flask import jsonify, make_response, request
from app import app
from app import departments, collaborators


@app.route('/', methods=['GET'])
def index():
    return make_response(jsonify({
            "msg": "ACMEVita - Main Page."
        }))


@app.route('/departments/list_all', methods=['GET'])
def list_all_departments():
    departments_dict = departments.list_all()

    return make_response(jsonify({
        "departments": departments_dict
    }))


@app.route('/departments/register', methods=['POST'])
def register_department():
    department_name = departments.register(eval(request.data))
    
    return make_response(jsonify({
        "msg": "Departament %r created with success." % department_name 
    }))


@app.route('/collaborators/list_all', methods=['GET'])
def list_all_collaboratos():
    collaborators_dict = collaborators.list_all()

    return make_response(jsonify({
        "collaborators": collaborators_dict
    }))


@app.route('/collaborators/register', methods=['POST'])
def register_collaborator():
    collaborator = collaborators.register(eval(request.data))
    
    # Se não existir departamento com o id que foi recebido, a função register retorna esse id.  
    if isinstance(collaborator, int):
        department_id = collaborator

        return make_response(jsonify({
            "msg": "The collaborator was not registered because the department with id %r does not exist." % department_id 
        }))

    # Se existir departamento, o retorno da função é o nome do funcionário.
    else:
        collaborator_name = collaborator

        return make_response(jsonify({
            "msg": "The collaborator %r was created with success." % collaborator_name
        }))
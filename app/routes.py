from crypt import methods
from flask import jsonify, make_response, request
from app import app
from app import departments
from app.departments import list_all, register

@app.route('/', methods=['GET'])
def index():
    return make_response(jsonify({
            "msg": "ACMEVita - Main Page"
        }))


@app.route('/department/list_all', methods=['GET'])
def list_all_departments():
    departments = list_all()

    return make_response(jsonify({
        "departments": departments
    }))


@app.route('/department/register', methods=['POST'])
def register_department():
    department_name = register(eval(request.data))
    
    return make_response(jsonify({
        "msg": "Departament %r created with success" % department_name 
    }))

from config import Config
from flask import Flask, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'ACMEVITA API'
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

from app import routes, models
from app.models import Department, Collaborator
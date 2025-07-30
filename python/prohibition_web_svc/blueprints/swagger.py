from flask import Blueprint
from flask_swagger_ui import get_swaggerui_blueprint
from python.prohibition_web_svc.config import Config
from flask import send_from_directory
import os

SWAGGER_URL = f'{Config.URL_PREFIX}/docs'  # URL for exposing Swagger UI
API_URL = '/docs/swagger.json'  # URL for your OpenAPI specification (e.g., a JSON file)


swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,    
    config={
        'app_name': "Digital Forms API",
        'info': {
            'title': 'Digital Forms API',
            'version': '1.0.0',
            'description': 'API documentation for the Digital Forms application.',
        },
        'host': 'localhost:5002/api',  # Change this to your host and port
    }
)

bp = Blueprint(SWAGGER_URL, __name__, url_prefix=Config.URL_PREFIX)
@swaggerui_blueprint.route('/swagger.json')
def swagger_json():
    """
    Serve the Swagger JSON file.
    """
    swagger_json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')

    return send_from_directory(swagger_json_path, 'swagger.json')
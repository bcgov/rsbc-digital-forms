from flask_api import FlaskAPI
import logging
from python.prohibition_web_svc.dev_database_seeder import seed_forms_for_development, seed_initial_administrator
from python.prohibition_web_svc.models import db, migrate
from python.prohibition_web_svc.config import Config
from python.prohibition_web_svc.blueprints import static, forms, admin_forms
from python.prohibition_web_svc.blueprints import icbc
from python.prohibition_web_svc.blueprints import user_roles, admin_user_roles, admin_users, users


application = FlaskAPI(__name__)
application.config['SECRET_KEY'] = Config.FLASK_SECRET_KEY
application.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASE_URI
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config["SQLALCHEMY_ECHO"] = False

application.register_blueprint(admin_forms.bp)
application.register_blueprint(admin_user_roles.bp)
application.register_blueprint(admin_users.bp)
application.register_blueprint(forms.bp)
application.register_blueprint(icbc.bp)
application.register_blueprint(static.bp)
application.register_blueprint(user_roles.bp)
application.register_blueprint(users.bp)

db.init_app(application)
migrate.init_app(application, db)

def create_app():
    with application.app_context():
        logging.warning('inside create_app()')
        initialize_app(application)
        return application


def initialize_app(app):
   if Config.ENVIRONMENT in ('dev', 'pr') and not Config.RUNNING_TESTS:
        seed_forms_for_development(db)
        # seed_initial_administrator(db)

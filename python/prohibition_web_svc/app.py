from flask_api import FlaskAPI
import logging
import pytz
from datetime import datetime
from python.common.models import db, migrate, Form, UserRole, User, Agency
from python.common.verbose_logging import VERBOSE_LEVEL_NUM, verbose
from python.prohibition_web_svc.config import Config
from python.prohibition_web_svc.commands import register_commands
from python.prohibition_web_svc.blueprints import static, forms, admin_forms, icbc, user_roles, admin_user_roles, admin_users, users, events, collision, print
from python.prohibition_web_svc.custom_json_encoder import CustomJSONEncoder



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
application.register_blueprint(events.bp)
application.register_blueprint(collision.bp)
application.register_blueprint(print.bp)

db.init_app(application)
migrate.init_app(application, db)
register_commands(application)

application.json = CustomJSONEncoder(application)

def create_app():
    with application.app_context():
        logging.warning('inside create_app()')
        initialize_app(application)
        return application


def initialize_app(app):
    # Create tables if they do not exist already
    @app.before_first_request
    def create_tables_and_seed():
        engine = db.get_engine()
        tables = db.inspect(engine).get_table_names()
        if len(tables) == 0:
            logging.warning('Sqlite database does not exist - creating new file')
            db.create_all()
            _seed_forms_for_development(db)
            seed_initial_administrator(db)
        else:
            logging.info("database already exists - no need to recreate")


def _seed_forms_for_development(database):
    if Config.ENVIRONMENT in ('dev', 'pr'):
        seed_records = []
        prefix = ["JZ", "VZ", "40", "22"]
        for idx, form_type in enumerate(["12Hour", "24Hour", "IRP", "VI"]):
            for x in range(100000, 100100):
                unique_id = '{}{}'.format(prefix[idx], str(x))
                seed_records.append(Form(
                    form_id=unique_id,
                    form_type=form_type))
        database.session.bulk_save_objects(seed_records)
        database.session.commit()
        logging.warning("seed temporary unique form_ids")
    return


def seed_initial_administrator(database):
    vancouver_tz = pytz.timezone("America/Vancouver")
    current_dt = datetime.now(vancouver_tz)
    agency = Agency(agency_name="RoadSafety", agency_id=1)
    database.session.add(agency)
    user = User(username=Config.ADMIN_USERNAME,
                user_guid=Config.ADMIN_USERNAME,
                badge_number='0000',
                agency_id=1,
                first_name="Initial",
                last_name="Administrator",
                login=Config.ADMIN_USERNAME)
    database.session.add(user)
    roles = [
        UserRole(user_guid=Config.ADMIN_USERNAME, role_name='officer', submitted_dt=current_dt, approved_dt=current_dt),
        UserRole(user_guid=Config.ADMIN_USERNAME, role_name='administrator', submitted_dt=current_dt, approved_dt=current_dt)
    ]
    database.session.bulk_save_objects(roles)
    database.session.commit()
    logging.warning("seed initial administrator: " + Config.ADMIN_USERNAME)
    return

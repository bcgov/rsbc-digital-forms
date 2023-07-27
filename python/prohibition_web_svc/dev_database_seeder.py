# dev_database_seeder.py
import logging
from python.prohibition_web_svc.models import Form, User, UserRole
from python.prohibition_web_svc.config import Config
import pytz
from datetime import datetime

def seed_forms_for_development(database):
    if Config.ENVIRONMENT in ('dev', 'pr') and not Config.RUNNING_TESTS:
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

def seed_initial_administrator(database):
    vancouver_tz = pytz.timezone("America/Vancouver")
    current_dt = datetime.now(vancouver_tz)
    user = User(username=Config.ADMIN_USERNAME,
                user_guid=Config.ADMIN_USERNAME,
                badge_number='0000',
                agency="RoadSafety",
                first_name="Initial",
                last_name="Administrator",
                login="Administrator@idir")
    database.session.add(user)
    roles = [
        UserRole(user_guid=Config.ADMIN_USERNAME, role_name='officer', submitted_dt=current_dt, approved_dt=current_dt),
        UserRole(user_guid=Config.ADMIN_USERNAME, role_name='administrator', submitted_dt=current_dt, approved_dt=current_dt)
    ]
    database.session.bulk_save_objects(roles)
    database.session.commit()
    logging.warning("seed initial administrator: " + Config.ADMIN_USERNAME)
    return
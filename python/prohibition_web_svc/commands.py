import logging
from python.prohibition_web_svc.config import Config
from python.prohibition_web_svc.models import db, migrate, Form, UserRole, User

def register_commands(app):
    @app.cli.command()
    def seed_form_numbers_for_dev():
        if Config.ENVIRONMENT in ('dev', 'pr'):
            seed_records = []
            prefix = ["JZ", "VZ", "40", "22"]
            for idx, form_type in enumerate(["12Hour", "24Hour", "IRP", "VI"]):
                for x in range(110000, 111000):
                    unique_id = '{}{}'.format(prefix[idx], str(x))
                    seed_records.append(Form(
                        form_id=unique_id,
                        form_type=form_type))
            db.session.bulk_save_objects(seed_records)
            db.session.commit()
            db.warning("seed temporary unique form_ids")
        return

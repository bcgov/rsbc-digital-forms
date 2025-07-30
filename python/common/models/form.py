from dataclasses import dataclass
from datetime import datetime, timedelta
from .base import db

@dataclass
class Form(db.Model):
    id: str
    form_type: str
    lease_expiry: datetime
    printed_timestamp: datetime
    spoiled_timestamp: datetime
    user_guid: str
    
    id = db.Column('id', db.String(20), primary_key=True)
    form_type = db.Column(db.String(20), nullable=False)
    lease_expiry = db.Column(db.Date, nullable=True)
    printed_timestamp = db.Column(db.DateTime, nullable=True)
    spoiled_timestamp = db.Column(db.DateTime, nullable=True)
    user_guid = db.Column(db.String(80), db.ForeignKey('user.user_guid'), nullable=True)

    def __init__(self, form_id, form_type, printed=None, spoiled=None, lease_expiry=None, user_guid=None):
        self.id = form_id
        self.form_type = form_type
        self.printed_timestamp = printed
        self.spoiled_timestamp = spoiled
        self.lease_expiry = lease_expiry
        self.user_guid = user_guid

    def lease(self, user_guid):
        today = datetime.now()
        lease_expiry = today + timedelta(days=30)
        self.lease_expiry = lease_expiry
        self.user_guid = user_guid
        import logging
        logging.info(f"{self.user_guid} leased {self.id} until {self.lease_expiry.strftime('%Y-%m-%d')}")

    @staticmethod
    def _format_lease_expiry(lease_expiry):
        if lease_expiry is None:
            return ''
        else:
            return datetime.strftime(lease_expiry, "%Y-%m-%d")

    @staticmethod
    def collection_to_dict(all_rows):
        result_list = []
        for row in all_rows:
            result_list.append(Form.serialize(row))
        return result_list

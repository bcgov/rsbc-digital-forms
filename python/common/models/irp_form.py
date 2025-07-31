from dataclasses import dataclass
from datetime import datetime
from .base import db

@dataclass
class IRPForm(db.Model):
    __tablename__ = 'irp_form'

    form_id: int
    event_id: int
    created_dt: datetime
    updated_dt: datetime

    form_id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.event_id'))
    created_dt = db.Column(db.DateTime)
    updated_dt = db.Column(db.DateTime)

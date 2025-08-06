from dataclasses import dataclass
from datetime import datetime
from .base import db

@dataclass
class TwelveHourForm(db.Model):
    __tablename__ = 'twelve_hour_form'

    form_id: int
    event_id: int
    created_dt: datetime
    updated_dt: datetime
    driver_phone: str
    twelve_hour_number: str
    vehicle_location: str

    form_id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.event_id'))
    created_dt = db.Column(db.DateTime)
    updated_dt = db.Column(db.DateTime)
    driver_phone = db.Column(db.String)
    twelve_hour_number = db.Column(db.String)
    vehicle_location = db.Column(db.String)

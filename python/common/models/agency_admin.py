from dataclasses import dataclass
from datetime import datetime, timezone
from .base import db

@dataclass
class AgencyAdmin(db.Model):
    __tablename__ = 'agency_admin'

    id: int
    agency_id: int
    email: str
    name: str
    created_dt: datetime
    updated_dt: datetime
    created_by: str
    updated_by: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    agency_id = db.Column(db.Integer, db.ForeignKey('agency.id'), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100))
    created_dt = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_dt = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    created_by = db.Column(db.String(120), db.ForeignKey('user.user_guid'), nullable=False)
    updated_by = db.Column(db.String(120), db.ForeignKey('user.user_guid'))

    agency = db.relationship('Agency', back_populates='admins')
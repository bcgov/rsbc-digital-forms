from dataclasses import dataclass
from .base import db

@dataclass
class VehicleStyle(db.Model):
    __tablename__ = 'vehicle_style'

    code: str
    name: str

    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)

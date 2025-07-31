from dataclasses import dataclass
from .base import db

@dataclass
class VehicleType(db.Model):
    __tablename__ = 'vehicle_type'

    type_cd: int
    description: str

    type_cd = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)

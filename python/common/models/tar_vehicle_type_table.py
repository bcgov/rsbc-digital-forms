from dataclasses import dataclass
from .base import db

@dataclass
class TarVehicleTypeTable(db.Model):
    __tablename__ = 'vehicle_type_table'
    code: str
    description: str
    code = db.Column(db.String(2), primary_key=True)
    description = db.Column(db.String(120))

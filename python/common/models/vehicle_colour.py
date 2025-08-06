from dataclasses import dataclass
from .base import db

@dataclass
class VehicleColour(db.Model):
    __tablename__ = 'vehicle_colour'

    code: str
    display_name: str
    colour_class: str

    code = db.Column(db.String, primary_key=True)
    display_name = db.Column(db.String)
    colour_class = db.Column(db.String)

from dataclasses import dataclass
from .base import db

@dataclass
class TarTrafficControl(db.Model):
    __tablename__ = 'traffic_control'
    code: str
    description: str
    code = db.Column(db.String(2), primary_key=True)
    description = db.Column(db.String(50))

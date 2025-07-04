from dataclasses import dataclass
from .base import db

@dataclass
class TarSpeedZone(db.Model):
    __tablename__ = 'speed_zone'
    code: str
    description: str
    code = db.Column(db.String(3), primary_key=True)
    description = db.Column(db.String(50))

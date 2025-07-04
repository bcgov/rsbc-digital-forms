from dataclasses import dataclass
from .base import db

@dataclass
class TarRoadType(db.Model):
    __tablename__ = 'road_type'
    code: str
    description: str
    code = db.Column(db.String(2), primary_key=True)
    description = db.Column(db.String(50))

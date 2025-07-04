from dataclasses import dataclass
from .base import db

@dataclass
class TarTrafficFlow(db.Model):
    __tablename__ = 'traffic_flow'
    code: str
    description: str
    code = db.Column(db.String(2), primary_key=True)
    description = db.Column(db.String(50))

from dataclasses import dataclass
from .base import db

@dataclass
class TarPedestrianAction(db.Model):
    __tablename__ = 'tar_pedestrian_action'
    code: str
    description: str
    code = db.Column(db.String(2), primary_key=True)
    description = db.Column(db.String(50))

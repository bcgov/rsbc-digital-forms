from dataclasses import dataclass
from .base import db

@dataclass
class TarPrimaryCollisionOccurrence(db.Model):
    __tablename__ = 'tar_primary_collision_occurrence'
    code: str
    description: str
    code = db.Column(db.String(2), primary_key=True)
    description = db.Column(db.String(50))

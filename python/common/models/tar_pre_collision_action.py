from dataclasses import dataclass
from .base import db

@dataclass
class TarPreCollisionAction(db.Model):
    __tablename__ = 'pre_collision_action'
    code: str
    description: str
    code = db.Column(db.String(2), primary_key=True)
    description = db.Column(db.String(50))

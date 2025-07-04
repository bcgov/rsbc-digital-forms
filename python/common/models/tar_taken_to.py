from dataclasses import dataclass
from .base import db

@dataclass
class TakenTo(db.Model):
    __tablename__ = 'taken_to'
    code: str
    description: str
    code = db.Column(db.String(4), primary_key=True)
    description = db.Column(db.String(50))

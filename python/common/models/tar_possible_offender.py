from dataclasses import dataclass
from .base import db

@dataclass
class TarPossibleOffender(db.Model):
    __tablename__ = 'possible_offender'
    code: str
    description: str
    code = db.Column(db.String(1), primary_key=True)
    description = db.Column(db.String(50))

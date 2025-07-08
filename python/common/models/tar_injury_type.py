from dataclasses import dataclass
from .base import db

@dataclass
class TarInjuryType(db.Model):
    __tablename__ = 'tar_injury_type'
    code: str
    description: str
    code = db.Column(db.String(2), primary_key=True)
    description = db.Column(db.String(50))

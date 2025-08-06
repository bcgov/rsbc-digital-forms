from dataclasses import dataclass
from ..base import db

@dataclass
class TarTakenTo(db.Model):
    __tablename__ = 'taken_to'
    __table_args__ = {'schema': 'TAR'}
    code: str
    description: str
    code = db.Column(db.String(4), primary_key=True)
    description = db.Column(db.String(50))

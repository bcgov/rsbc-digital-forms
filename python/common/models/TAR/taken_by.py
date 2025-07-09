from dataclasses import dataclass
from ..base import db

@dataclass
class TarTakenBy(db.Model):
    __tablename__ = 'taken_by'
    __table_args__ = {'schema': 'TAR'}
    code: str
    description: str
    code = db.Column(db.String(4), primary_key=True)
    description = db.Column(db.String(50))

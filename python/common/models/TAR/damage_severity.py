from dataclasses import dataclass
from ..base import db

@dataclass
class TarDamageSeverity(db.Model):
    __tablename__ = 'damage_severity'
    __table_args__ = {'schema': 'TAR'}
    code: str
    description: str
    code = db.Column(db.String(2), primary_key=True)
    description = db.Column(db.String(60))

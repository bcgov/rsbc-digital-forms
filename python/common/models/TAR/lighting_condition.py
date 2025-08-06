from dataclasses import dataclass
from ..base import db

@dataclass
class TarLightingCondition(db.Model):
    __tablename__ = 'lighting_condition'
    __table_args__ = {'schema': 'TAR'}
    code: str
    description: str
    code = db.Column(db.String(2), primary_key=True)
    description = db.Column(db.String(50))

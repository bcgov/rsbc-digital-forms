from dataclasses import dataclass
from ..base import db

@dataclass
class TarEntityType(db.Model):
    __tablename__ = 'entity_type'
    __table_args__ = {'schema': 'TAR'}
    code: str
    description: str
    code = db.Column(db.String(1), primary_key=True)
    description = db.Column(db.String(50))

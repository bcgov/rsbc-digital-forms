from dataclasses import dataclass
from ..base import db

@dataclass
class TarContributingFactors(db.Model):
    __tablename__ = 'contributing_factors'
    __table_args__ = {'schema': 'TAR'}
    code: str
    description: str
    type: str
    code = db.Column(db.String(2), primary_key=True)
    description = db.Column(db.String(60))
    type = db.Column(db.String(30))

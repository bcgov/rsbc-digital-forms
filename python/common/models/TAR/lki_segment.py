from dataclasses import dataclass
from ..base import db

@dataclass
class TarLkiSegment(db.Model):
    __tablename__ = 'lki_segment'
    __table_args__ = {'schema': 'TAR'}
    
    code: str
    hwy_code: str
    description: str
    direction: str
    length_km: float

    code = db.Column(db.String(4), primary_key=True)
    hwy_code = db.Column(db.String(4), db.ForeignKey('TAR.lki_highway.code'), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    direction = db.Column(db.String(1), nullable=False)
    length_km = db.Column(db.Float, nullable=False)

from dataclasses import dataclass
from ..base import db

@dataclass
class TarPoliceDistrict(db.Model):
    __tablename__ = 'police_district'
    __table_args__ = {'schema': 'TAR'}
    id: int
    district_name: str
    prefix: str
    id = db.Column(db.Integer, primary_key=True)
    district_name = db.Column(db.String(30), nullable=False)
    prefix = db.Column(db.String(1), nullable=False)

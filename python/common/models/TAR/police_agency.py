from dataclasses import dataclass
from ..base import db

@dataclass
class TarPoliceAgency(db.Model):
    __tablename__ = 'police_agency'
    __table_args__ = {'schema': 'TAR'}
    code: int
    district_id: int
    agency_name: str
    vjur_agency: int
    icbc_prefix: str

    code = db.Column(db.Integer, primary_key=True)
    district_id = db.Column(db.Integer, db.ForeignKey('TAR.police_district.id'), nullable=False)
    agency_name = db.Column(db.String(60), nullable=False)
    vjur_agency = db.Column(db.Integer, db.ForeignKey('agency.id'))
    icbc_prefix = db.Column(db.String(1))

from dataclasses import dataclass
from .base import db

@dataclass
class AgencyCrossref(db.Model):
    __tablename__ = 'agency_cross_refs'

    agency_name: str
    agency_id: int
    agency_city: str
    prime_vjur: str
    icbc_detachment_name: str
    icbc_city_name: str
    vips_policedetachments_agency_id: str
    vips_policedetachments_agency_nm: str
    prime_agency: str
    hidden_tf: bool = False
    hidden_reason: str
    
    agency_name = db.Column(db.String, nullable=False)
    agency_id = db.Column(db.Integer, db.ForeignKey('agency.id'), primary_key=True, nullable=False)
    agency_city = db.Column(db.String)
    prime_vjur = db.Column(db.String)
    icbc_detachment_name = db.Column(db.String)
    icbc_city_name = db.Column(db.String)
    vips_policedetachments_agency_id = db.Column(db.String)
    vips_policedetachments_agency_nm = db.Column(db.String)
    prime_agency = db.Column(db.String(50))
    hidden_tf = db.Column(db.Boolean, default=False)
    hidden_reason = db.Column(db.String(50))


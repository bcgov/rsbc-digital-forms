from dataclasses import dataclass
from .base import db

@dataclass
class AgencyCrossref(db.Model):
    __tablename__ = 'agency_cross_refs'

    agency_name: str
    agency_id: str
    agency_city: str
    prime_vjur: str
    icbc_detachment_name: str
    icbc_city_name: str
    vips_policedetachments_agency_id: str
    vips_policedetachments_agency_nm: str

    agency_name = db.Column(db.String, primary_key=True)
    agency_id = db.Column(db.String)
    agency_city = db.Column(db.String)
    prime_vjur = db.Column(db.String)
    icbc_detachment_name = db.Column(db.String)
    icbc_city_name = db.Column(db.String)
    vips_policedetachments_agency_id = db.Column(db.String)
    vips_policedetachments_agency_nm = db.Column(db.String)

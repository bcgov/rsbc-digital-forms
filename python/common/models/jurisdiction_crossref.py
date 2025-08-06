from dataclasses import dataclass
from .base import db

@dataclass
class JurisdictionCrossRef(db.Model):
    __tablename__ = 'jurisdiction_cross_ref'

    jurisdiction_name: str
    jurisdiction_code: str
    prime_jurisdiction_code: str
    prime_jurisdiction_name: str
    icbc_jurisdiction_code: str
    icbc_jurisdiction: str
    vips_jurisdictions_objectCd: str
    vips_jurisdictions_objectDsc: str

    jurisdiction_name = db.Column(db.String)
    jurisdiction_code = db.Column(db.String, primary_key=True)
    prime_jurisdiction_code = db.Column(db.String)
    prime_jurisdiction_name = db.Column(db.String)
    icbc_jurisdiction_code = db.Column(db.String)
    icbc_jurisdiction = db.Column(db.String)
    vips_jurisdictions_objectCd = db.Column(db.String)
    vips_jurisdictions_objectDsc = db.Column(db.String)

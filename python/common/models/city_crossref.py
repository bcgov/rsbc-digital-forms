from dataclasses import dataclass
from .base import db

@dataclass
class CityCrossRef(db.Model):
    __tablename__ = 'city_cross_ref'

    city_code: str
    city_name: str
    icbc_city_code: str
    icbc_city_name: str
    icbc_city_name_legacy: str
    vips_city_name: str

    city_code = db.Column(db.String, primary_key=True)
    city_name = db.Column(db.String)
    icbc_city_code = db.Column(db.String)
    icbc_city_name = db.Column(db.String)
    icbc_city_name_legacy = db.Column(db.String)
    vips_city_name = db.Column(db.String)

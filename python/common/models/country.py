from dataclasses import dataclass
from .base import db

@dataclass
class Country(db.Model):
    __tablename__ = 'country'

    id: int
    objectCd: str
    objectDsc: str

    id = db.Column(db.Integer, primary_key=True)
    objectCd = db.Column(db.String)
    objectDsc = db.Column(db.String)

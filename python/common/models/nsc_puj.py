from dataclasses import dataclass
from .base import db

@dataclass
class NSCPuj(db.Model):
    __tablename__ = 'nsc_puj'

    id: int
    objectCd: str
    objectDsc: str

    id = db.Column(db.Integer, primary_key=True)
    objectCd = db.Column(db.String)
    objectDsc = db.Column(db.String)

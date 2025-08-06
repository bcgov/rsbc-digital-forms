from dataclasses import dataclass
from .base import db

@dataclass
class Jurisdiction(db.Model):
    __tablename__ = 'jurisdiction'

    id: int
    objectCd: str
    objectDsc: str

    id = db.Column(db.Integer, primary_key=True)
    objectCd = db.Column(db.String)
    objectDsc = db.Column(db.String)

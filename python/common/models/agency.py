from dataclasses import dataclass
from .base import db

@dataclass
class Agency(db.Model):
    __tablename__ = 'agency'

    id: int
    vjur: str
    agency_name: str

    id = db.Column(db.Integer, primary_key=True)
    vjur = db.Column(db.String)
    agency_name = db.Column(db.String)

from dataclasses import dataclass
from .base import db

@dataclass
class Vehicle(db.Model):
    __tablename__ = 'vehicle'

    id: int
    mk: str
    search: str
    md: str

    id = db.Column(db.Integer, primary_key=True)
    mk = db.Column(db.String)
    search = db.Column(db.String)
    md = db.Column(db.String)

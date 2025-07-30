from dataclasses import dataclass
from .base import db

@dataclass
class ImpoundLotOperator(db.Model):
    __tablename__ = 'impound_lot_operator'

    id: int
    name: str
    name_print: str
    lot_address: str
    city: str
    phone: str

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    name_print = db.Column(db.String)
    lot_address = db.Column(db.String)
    city = db.Column(db.String)
    phone = db.Column(db.String)

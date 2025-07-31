from dataclasses import dataclass
from .base import db

@dataclass
class IloIdCrossRef(db.Model):
    __tablename__ = 'ilo_cross_ref'

    ilo_name: str
    vips_impound_lot_operator_id: int

    ilo_name = db.Column(db.String, primary_key=True)
    vips_impound_lot_operator_id = db.Column(db.Integer)

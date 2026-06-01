
from dataclasses import dataclass
from decimal import Decimal
from .base import db

@dataclass
class IRPProhibitionType(db.Model):
    __tablename__ = 'irp_prohibition_type'

    id: int
    code: str
    prohibition_period: int
    breath_result: str
    monetary_penalty: Decimal
    prohibition_reason: str
    active: bool
    display_order: int

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(20), nullable=False)
    prohibition_period = db.Column(db.Integer, nullable=False)
    breath_result = db.Column(db.String(20), nullable=False)
    monetary_penalty = db.Column(db.Numeric, nullable=False)
    prohibition_reason = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean, nullable=False, default=True)
    display_order = db.Column(db.Integer, nullable=False)


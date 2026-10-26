from dataclasses import dataclass
from sqlalchemy import ForeignKeyConstraint
from ..base import db
from .collision import ORIGINAL_REVISION

@dataclass
class TarWitnessInfo(db.Model):
    __tablename__ = 'witness_info'
    __table_args__ = (
        ForeignKeyConstraint(
            ['collision_case_num', 'revision'],
            ['TAR.collision.collision_case_num', 'TAR.collision.revision'],
            name='witness_info_collision_revision_fkey'
        ),
        {'schema': 'TAR'},
    )

    id: int
    collision_case_num: str
    revision: int
    witness_name: str
    address: str
    contact_phn_num: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    collision_case_num = db.Column(db.String(10), nullable=False)
    revision = db.Column(db.Integer, nullable=False, default=ORIGINAL_REVISION)
    witness_name = db.Column(db.String(100))
    address = db.Column(db.String(255))
    contact_phn_num = db.Column(db.String(100))

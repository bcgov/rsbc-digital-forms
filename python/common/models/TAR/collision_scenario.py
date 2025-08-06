from dataclasses import dataclass
from ..base import db

@dataclass
class TarCollisionScenario(db.Model):
    __tablename__ = 'collision_scenario'
    __table_args__ = {'schema': 'TAR'}

    code: str
    description: str

    code = db.Column(db.String(2), primary_key=True, nullable=False)
    description = db.Column(db.String(100), nullable=False)

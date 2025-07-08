from dataclasses import dataclass
from .base import db

@dataclass
class TarTypeOfCollision(db.Model):
    __tablename__ = 'tar_type_of_collision'
    code: str
    description: str
    type: str
    code = db.Column(db.String(2), primary_key=True)
    description = db.Column(db.String(50))
    type = db.Column(db.String(20))

from dataclasses import dataclass
from .base import db

@dataclass
class Permission(db.Model):
    __tablename__ = 'permission'

    id: int
    role: str
    permission: str

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String)
    permission = db.Column(db.String)

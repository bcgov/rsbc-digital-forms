from dataclasses import dataclass
from datetime import datetime, timezone
from ..base import db


@dataclass
class FormsflowOfflineSubmission(db.Model):
    __tablename__ = 'offline_submission'
    __table_args__ = (
        db.UniqueConstraint('local_submission_id', 'created_by', name='uq_local_submission_id_created_by'),
        {'schema': 'formsflow'}
    )


    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    local_submission_id: str = db.Column(db.String(100), nullable=False)
    payload: dict = db.Column(db.JSON, nullable=False)
    status: str = db.Column(db.String(50), default='pending', nullable=False)
    submission_id: str = db.Column(db.String(100))
    form_id: str = db.Column(db.String(100))
    created_dt: datetime = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_dt: datetime = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    created_by: str = db.Column(db.String(120), nullable=False)
    updated_by: str = db.Column(db.String(120))

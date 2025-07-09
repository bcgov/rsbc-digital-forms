from dataclasses import dataclass
from datetime import datetime, timezone
from .base import db

@dataclass
class Submission(db.Model):
    __tablename__ = 'submission'

    submission_id: int
    ff_application_id: int
    created_dt: datetime
    updated_dt: datetime
    created_by: str
    updated_by: str
    task_processing_status: str

    submission_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ff_application_id = db.Column(db.Integer, nullable=False)
    created_dt = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_dt = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    created_by = db.Column(db.String(120), db.ForeignKey('user.user_guid'), nullable=False)
    updated_by = db.Column(db.String(120))
    task_processing_status = db.Column(db.String(30), default='pending', nullable=False)

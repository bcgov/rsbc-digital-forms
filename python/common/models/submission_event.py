from dataclasses import dataclass
from datetime import datetime, timezone
from .base import db

@dataclass
class SubmissionEvent(db.Model):
    __tablename__ = 'submission_events'

    submission_event_id: int
    form_ref_id: int
    destination: str
    status: str
    created_at: datetime
    updated_at: datetime

    submission_event_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    form_ref_id = db.Column(db.Integer, db.ForeignKey('submission_form_refs.form_ref_id'), nullable=False)
    destination = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False, default='pending')
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, onupdate=lambda: datetime.now(timezone.utc))

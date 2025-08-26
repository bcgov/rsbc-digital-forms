from dataclasses import dataclass
from datetime import datetime, timezone
from .base import db

@dataclass
class SubmissionFormRef(db.Model):
    __tablename__ = 'submission_form_refs'

    form_ref_id: int
    submission_id: int
    form_type: str
    form_id: str
    form_version: str
    storage_key: str
    created_at: datetime
    updated_at: datetime

    form_ref_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    submission_id = db.Column(db.Integer, db.ForeignKey('submission.submission_id'), nullable=False)
    form_type = db.Column(db.String(50), nullable=False)
    form_id = db.Column(db.String(50), nullable=False)
    form_version = db.Column(db.String(50), nullable=False)
    storage_key = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, onupdate=lambda: datetime.now(timezone.utc))

    events = db.relationship('SubmissionEvent', backref='submission_form_ref', uselist=True)

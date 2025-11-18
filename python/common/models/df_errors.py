from dataclasses import dataclass
from datetime import datetime
from python.common.enums import ErrorStatus
from .base import db

@dataclass
class DFErrors(db.Model):
    __tablename__ = 'df_errors'

    error_id: int = db.Column(db.Integer, primary_key=True)
    error_cd: str = db.Column(db.String(5), nullable=False)
    error_cd_desc: str = db.Column(db.String(200), nullable=False)
    error_resolution: str = db.Column(db.Text)
    error_category_cd: str = db.Column(db.String(10), nullable=False)
    error_severity_level_cd: str = db.Column(db.String(10), nullable=False)
    error_details: str = db.Column(db.Text)
    error_path: str = db.Column(db.String(200))
    event_id: int = db.Column(db.Integer, db.ForeignKey('event.event_id'), nullable=True)
    submission_id: int = db.Column(db.Integer, db.ForeignKey('submission.submission_id'), nullable=True)
    event_type: str = db.Column(db.String(30), nullable=True)
    ticket_no: str = db.Column(db.String(50), nullable=True)
    received_dt: datetime = db.Column(db.DateTime, default=datetime.now())
    error_status_cd: str = db.Column(db.String(200), default=ErrorStatus.NEW)
    req_payload: str = db.Column(db.Text)
    created_by: str = db.Column(db.String(150))
    created_dt: datetime = db.Column(db.DateTime, default=datetime.now())
    updated_by: str = db.Column(db.String(150))
    updated_dt: datetime = db.Column(db.DateTime, onupdate=datetime.now())

    def __repr__(self):
        return f'<DF_Error {self.error_id}: {self.error_category_cd} - {self.error_severity_level_cd}>'

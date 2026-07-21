from datetime import datetime
from .base import db


VALID_CHANGE_REASONS = {
    'OVERTIME_ASSIGNMENT',
    'TRANSFER',
    'TEMPORARY_COVERAGE',
    'OPERATIONAL_REQUIREMENT',
    'OTHER',
}


class DetachmentChangeRequest(db.Model):
    __tablename__ = 'detachment_change_request'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    officer_id = db.Column(db.String(120), db.ForeignKey('user.user_guid'), nullable=False)
    previous_agency_id = db.Column(db.Integer, db.ForeignKey('agency.id'), nullable=True)
    new_agency_id = db.Column(db.Integer, db.ForeignKey('agency.id'), nullable=False)
    reason = db.Column(db.String(50), nullable=False)
    comments = db.Column(db.Text, nullable=True)
    created_dt = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.String(120), nullable=True)

    previous_agency = db.relationship('Agency', foreign_keys=[previous_agency_id], lazy='select')
    new_agency_ref = db.relationship('Agency', foreign_keys=[new_agency_id], lazy='select')

    def __init__(self, officer_id, new_agency_id, reason, created_dt, created_by,
                 previous_agency_id=None, comments=None):
        self.officer_id = officer_id
        self.previous_agency_id = previous_agency_id
        self.new_agency_id = new_agency_id
        self.reason = reason
        self.comments = comments
        self.created_dt = created_dt
        self.created_by = created_by

    @staticmethod
    def serialize(record):
        return {
            'id': record.id,
            'officer_id': record.officer_id,
            'previous_agency_id': record.previous_agency_id,
            'new_agency_id': record.new_agency_id,
            'reason': record.reason,
            'comments': record.comments,
            'created_dt': record.created_dt.isoformat() if record.created_dt else None,
            'created_by': record.created_by,
        }

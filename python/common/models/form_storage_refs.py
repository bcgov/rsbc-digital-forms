from dataclasses import dataclass
from datetime import datetime
from .base import db

@dataclass
class FormStorageRefs(db.Model):
    __tablename__ = 'form_storage_refs'

    form_id_24h: int
    form_id_irp: int
    form_id_vi: int
    form_id_12h: int
    event_id: int
    form_type: str
    storage_key: str
    encryptiv: str
    created_dt: datetime
    updated_dt: datetime

    storage_key = db.Column(db.String, primary_key=True)
    form_id_24h = db.Column(db.Integer, db.ForeignKey('twenty_four_hour_form.form_id'))
    form_id_irp = db.Column(db.Integer, db.ForeignKey('irp_form.form_id'))
    form_id_vi = db.Column(db.Integer, db.ForeignKey('vi_form.form_id'))
    form_id_12h = db.Column(db.Integer, db.ForeignKey('twelve_hour_form.form_id'))
    event_id = db.Column(db.Integer, db.ForeignKey('event.event_id'))
    form_type = db.Column(db.String)
    encryptiv = db.Column(db.String)
    created_dt = db.Column(db.DateTime)
    updated_dt = db.Column(db.DateTime)

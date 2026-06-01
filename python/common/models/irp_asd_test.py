
from dataclasses import dataclass
from datetime import time
from .base import db

@dataclass
class IRPASDTest(db.Model):
    __tablename__ = 'irp_asd_test'
    __table_args__ = (
        db.UniqueConstraint('irp_form_id', 'test_number', name='irp_asd_test_form_testnumber_uq'),
    )

    id: int
    irp_form_id: int
    test_number: int
    asd_identification: str
    serial_number: str
    test_time: str
    result: str
    result_shown_to_driver: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    irp_form_id = db.Column(db.Integer, db.ForeignKey('irp_form.form_id'), nullable=False)
    test_number = db.Column(db.Integer, nullable=False)
    asd_identification = db.Column(db.String(20), nullable=False)
    serial_number = db.Column(db.String(20), nullable=False)
    test_time = db.Column(db.String(5), nullable=False)
    result = db.Column(db.String(20), nullable=False)
    result_shown_to_driver = db.Column(db.String(5), nullable=False)

    

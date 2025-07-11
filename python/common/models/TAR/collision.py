from dataclasses import dataclass
from datetime import date, datetime, time
from ..base import db

@dataclass
class TarCollision(db.Model):
    __tablename__ = 'collision'
    __table_args__ = {'schema': 'TAR'}

    submission_id: int
    collision_case_num: str
    collision_scenario: str
    police_file_num: str
    prime_file_vjur: str
    police_file_prefix: str
    date_collision: date
    time_collision: time
    reported_same_day: bool
    time_collision_unknown: bool
    date_reported: date
    hit_and_run: str
    police_attended: str
    police_agency_type_district: str
    police_agency_code: int
    police_zone: str
    primary_collision_occ_code: str
    first_contact_event: str
    first_contact_loc: str
    has_countable_fatal: str
    countable_fatal_total: int
    completed_by_name: str
    completed_by_id: str
    detachment_unit: str
    icbc_submission_date: datetime
    reviewed_by: str
    investigated_by_traffic_analyst: str

    submission_id = db.Column(db.Integer, db.ForeignKey('submission.submission_id'), nullable=False)
    collision_case_num = db.Column(db.String(10), primary_key=True, nullable=False)
    collision_scenario = db.Column(db.String(2), db.ForeignKey('TAR.collision_scenario.code'), nullable=False)
    police_file_num = db.Column(db.String(18), nullable=False)
    prime_file_vjur = db.Column(db.Integer, db.ForeignKey('agency.id'), nullable=False)
    police_file_prefix = db.Column(db.String(15))
    date_collision = db.Column(db.Date, nullable=False)
    time_collision = db.Column(db.Time, nullable=False)
    reported_same_day = db.Column(db.Boolean, nullable=False)
    time_collision_unknown = db.Column(db.Boolean, nullable=False)
    date_reported = db.Column(db.Date, nullable=False)
    hit_and_run = db.Column(db.String(1), nullable=False)
    police_attended = db.Column(db.String(1), nullable=False)
    police_agency_type_district = db.Column(db.String(30), nullable=False)   # Check if needed
    police_agency_code = db.Column(db.Integer, db.ForeignKey('agency.id'), nullable=False)
    police_zone = db.Column(db.String(22))
    primary_collision_occ_code = db.Column(db.String(2), db.ForeignKey('TAR.primary_collision_occurrence.code'), nullable=False)
    first_contact_event = db.Column(db.String(2), db.ForeignKey('TAR.type_of_collision.code'), nullable=False)
    first_contact_loc = db.Column(db.String(2), db.ForeignKey('TAR.location_of_first_contact.code'), nullable=False)
    has_countable_fatal = db.Column(db.String(2), nullable=False)
    countable_fatal_total = db.Column(db.Integer, nullable=False, default=0)
    completed_by_name = db.Column(db.String(35), nullable=False)
    completed_by_id = db.Column(db.String(40), db.ForeignKey('user.user_guid'), nullable=False)
    detachment_unit = db.Column(db.String(30), nullable=False)
    icbc_submission_date = db.Column(db.DateTime, nullable=True)
    reviewed_by = db.Column(db.String(40))
    investigated_by_traffic_analyst = db.Column(db.String(1), nullable=False)

    additional_details = db.relationship('TarAdditionalCollisionDetails', backref='collision', uselist=False, lazy='select')
    location = db.relationship('TarLocation', backref='collision', uselist=False, lazy='select')
    witnesses = db.relationship('TarWitnessInfo', backref='collision', lazy='select')
    entity = db.relationship('TarEntity', backref='collision', lazy='select')
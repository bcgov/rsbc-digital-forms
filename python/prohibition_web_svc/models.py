from datetime import datetime, timedelta
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging

db = SQLAlchemy()
migrate = Migrate()

@dataclass
class Form(db.Model):
    id: str
    form_type: str
    lease_expiry: datetime
    printed_timestamp: datetime
    spoiled_timestamp: datetime
    user_guid: str
    
    id = db.Column('id', db.String(20), primary_key=True)
    form_type = db.Column(db.String(20), nullable=False)
    lease_expiry = db.Column(db.Date, nullable=True)
    printed_timestamp = db.Column(db.DateTime, nullable=True)
    spoiled_timestamp = db.Column(db.DateTime, nullable=True)
    user_guid = db.Column(db.String(80), db.ForeignKey(
        'user.user_guid'), nullable=True)

    # Note: The printed timestamp prior to v0.4.17 was saved in local Pacific time instead of GMT

    def __init__(self, form_id, form_type, printed=None, spoiled=None, lease_expiry=None, user_guid=None):
        self.id = form_id
        self.form_type = form_type
        self.printed_timestamp = printed
        self.spoiled_timestamp = spoiled
        self.lease_expiry = lease_expiry
        self.user_guid = user_guid

    def lease(self, user_guid):
        today = datetime.now()
        lease_expiry = today + timedelta(days=30)
        self.lease_expiry = lease_expiry
        self.user_guid = user_guid
        logging.info("{} leased {} until {}".format(
            self.user_guid, self.id, self.lease_expiry.strftime("%Y-%m-%d")))

    @staticmethod
    def _format_lease_expiry(lease_expiry):
        if lease_expiry is None:
            return ''
        else:
            return datetime.strftime(lease_expiry, "%Y-%m-%d")

    @staticmethod
    def collection_to_dict(all_rows):
        result_list = []
        for row in all_rows:
            result_list.append(Form.serialize(row))
        return result_list


class User(db.Model):
    user_guid = db.Column(db.String(120), primary_key=True)
    business_guid = db.Column(db.String(120), nullable=True)
    username = db.Column(db.String(80), nullable=False)
    agency = db.Column(db.String(120), nullable=False)
    badge_number = db.Column(db.String(12), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    first_name = db.Column(db.String(40), nullable=True)
    display_name = db.Column(db.String(80), nullable=True)
    login = db.Column(db.String(80), nullable=False)

    def __init__(self, username, user_guid, agency, badge_number, last_name, login, business_guid='', display_name='', first_name=''):
        self.username = username
        self.user_guid = user_guid
        self.agency = agency
        self.badge_number = badge_number
        self.last_name = last_name
        self.first_name = first_name
        self.business_guid = business_guid
        self.display_name = display_name
        self.login = login

    @staticmethod
    def serialize(user):
        return {
            "username": user.username,
            "user_guid": user.user_guid,
            "agency": user.agency,
            "badge_number": user.badge_number,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "display_name": user.display_name,
            "login": user.login
        }


class UserRole(db.Model):
    role_name = db.Column(db.String(20), primary_key=True)
    user_guid = db.Column(db.String(80), db.ForeignKey(
        'user.user_guid'), primary_key=True)
    submitted_dt = db.Column(db.DateTime, nullable=True)
    approved_dt = db.Column(db.DateTime, nullable=True)

    def __init__(self, role_name, user_guid, submitted_dt=None, approved_dt=None):
        self.role_name = role_name
        self.user_guid = user_guid
        self.submitted_dt = submitted_dt
        self.approved_dt = approved_dt

    @staticmethod
    def serialize(role):
        return {
            "role_name": role.role_name,
            "user_guid": role.user_guid,
            "submitted_dt": role.submitted_dt,
            "approved_dt": role.approved_dt
        }

    @staticmethod
    def serialize_all_users(rows):
        return {
            "agency": rows.agency,
            "approved_dt": rows.approved_dt,
            "badge_number": rows.badge_number,
            "first_name": rows.first_name,
            "last_name": rows.last_name,
            "role_name": rows.role_name,
            "submitted_dt": rows.submitted_dt,
            "user_guid": rows.user_guid,
            "username": rows.username,
            "login": rows.login,
        }

    @staticmethod
    def collection_to_dict(all_rows, serialization_method: str):
        result_list = []
        for row in all_rows:
            method = getattr(UserRole, serialization_method)
            result_list.append(method(row))
        return result_list

    @staticmethod
    def collection_to_list_roles(all_rows):
        result_list = []
        for row in all_rows:
            result_list.append(row.role_name)
        return result_list

    @staticmethod
    def get_roles(user_guid):
        rows = db.session.query(UserRole) \
            .filter(UserRole.user_guid == user_guid) \
            .filter(UserRole.approved_dt != None) \
            .all()
        return UserRole.collection_to_list_roles(rows)


@dataclass 
class Agency(db.Model):
    __tablename__ = 'agency'

    id: int
    vjur: str
    agency_name: str

    id = db.Column(db.Integer, primary_key=True)
    vjur = db.Column(db.String)
    agency_name = db.Column(db.String)


@dataclass
class City(db.Model):
    __tablename__ = 'city'

    id: int
    objectCd: str
    objectDsc: str

    id = db.Column(db.Integer, primary_key=True)
    objectCd = db.Column(db.String)
    objectDsc = db.Column(db.String)


@dataclass
class Country(db.Model):
    __tablename__ = 'country'

    id: int
    objectCd: str
    objectDsc: str

    id = db.Column(db.Integer, primary_key=True)
    objectCd = db.Column(db.String)
    objectDsc = db.Column(db.String)


@dataclass
class ImpoundLotOperator(db.Model):
    __tablename__ = 'impound_lot_operator'

    id: int
    name: str
    name_print: str
    lot_address: str
    city: str
    phone: str

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    name_print = db.Column(db.String)
    lot_address = db.Column(db.String)
    city = db.Column(db.String)
    phone = db.Column(db.String)


@dataclass
class Jurisdiction(db.Model):
    __tablename__ = 'jurisdiction'

    id: int
    objectCd: str
    objectDsc: str

    id = db.Column(db.Integer, primary_key=True)
    objectCd = db.Column(db.String)
    objectDsc = db.Column(db.String)
    
@dataclass
class JurisdictionCountry(db.Model):
    __tablename__ = 'jurisdiction_country'

    id: int
    objectCd: str
    objectDsc: str

    id = db.Column(db.Integer, primary_key=True)
    objectCd = db.Column(db.String)
    objectDsc = db.Column(db.String)
    
@dataclass
class NSCPuj(db.Model):
    __tablename__ = 'nsc_puj'

    id: int
    objectCd: str
    objectDsc: str

    id = db.Column(db.Integer, primary_key=True)
    objectCd = db.Column(db.String)
    objectDsc = db.Column(db.String)


@dataclass
class Permission(db.Model):
    __tablename__ = 'permission'

    id: int
    role: str
    permission: str

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String)
    permission = db.Column(db.String)


@dataclass
class Province(db.Model):
    __tablename__ = 'province'

    id: int
    objectCd: str
    objectDsc: str

    id = db.Column(db.Integer, primary_key=True)
    objectCd = db.Column(db.String)
    objectDsc = db.Column(db.String)


@dataclass
class VehicleStyle(db.Model):
    __tablename__ = 'vehicle_style'

    code: str
    name: str

    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    
@dataclass
class VehicleType(db.Model):
    __tablename__ = 'vehicle_type'

    type_cd: int
    description: str

    type_cd = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)


@dataclass
class Vehicle(db.Model):
    __tablename__ = 'vehicle'

    id: int
    mk: str
    search: str
    md: str

    id = db.Column(db.Integer, primary_key=True)
    mk = db.Column(db.String)
    search = db.Column(db.String)
    md = db.Column(db.String)


@dataclass
class VehicleColour(db.Model):
    __tablename__ = 'vehicle_colour'

    code: str
    display_name: str
    colour_class: str

    code = db.Column(db.String, primary_key=True)
    display_name = db.Column(db.String)
    colour_class = db.Column(db.String)


@dataclass
class Event(db.Model):
    __tablename__ = 'event'

    event_id: int
    icbc_sent_status: str
    vi_sent_status: str
    icbc_retry_count: int
    vi_retry_count: int
    driver_licence_no: str
    driver_jurisdiction: str
    driver_last_name: str
    driver_given_name: str
    driver_dob: datetime
    driver_address: str
    driver_city: str
    driver_prov: str
    driver_postal: str
    driver_phone: str
    date_of_driving: datetime
    time_of_driving: str
    vehicle_jurisdiction: str
    vehicle_plate_no: str
    vehicle_registration_no: str
    vehicle_year: str
    vehicle_mk_md: str
    vehicle_style: str
    vehicle_type: int
    vehicle_colour: str
    vehicle_vin_no: str
    nsc_prov_state: str
    location_of_keys: str
    nsc_no: str
    type_of_prohibition: str
    owned_by_corp: bool
    vehicle_released_to: str
    date_released: datetime
    time_released: str
    intersection_or_address_of_offence: str
    offence_city: str
    corporation_name: str
    regist_owner_last_name: str
    regist_owner_first_name: str
    regist_owner_address: str
    regist_owner_dob: datetime
    regist_owner_city: str
    regist_owner_prov: str
    regist_owner_postal: str
    regist_owner_phone: str
    regist_owner_email: str
    agency_file_no: str
    submitted: bool
    confirmation_of_service: bool
    confirmation_of_service_date: datetime
    impound_lot_operator: int
    task_processing_status: str
    created_dt: datetime
    updated_dt: datetime
    created_by: str
    updated_by: str

    event_id = db.Column(db.Integer, primary_key=True)
    icbc_sent_status = db.Column(db.String)
    vi_sent_status = db.Column(db.String)
    icbc_retry_count = db.Column(db.Integer)
    vi_retry_count = db.Column(db.Integer)
    type_of_prohibition = db.Column(db.String)
    driver_licence_no = db.Column(db.String)
    driver_jurisdiction = db.Column(db.String)
    driver_last_name = db.Column(db.String)
    driver_given_name = db.Column(db.String)
    driver_dob = db.Column(db.DateTime)
    driver_address = db.Column(db.String)
    driver_city = db.Column(db.String)
    driver_prov = db.Column(db.String)
    driver_postal = db.Column(db.String)
    driver_phone = db.Column(db.String)
    agency_file_no = db.Column(db.String)
    date_of_driving = db.Column(db.DateTime)
    time_of_driving = db.Column(db.String)
    vehicle_jurisdiction = db.Column(db.String)
    vehicle_plate_no = db.Column(db.String)
    vehicle_registration_no = db.Column(db.String)
    vehicle_year = db.Column(db.String)
    vehicle_mk_md = db.Column(db.String)
    vehicle_style = db.Column(db.String)
    vehicle_type = db.Column(db.Integer, db.ForeignKey('vehicle_type.type_cd'))
    vehicle_colour = db.Column(db.String)
    vehicle_vin_no = db.Column(db.String)
    nsc_prov_state = db.Column(db.String)
    location_of_keys = db.Column(db.String)
    nsc_no = db.Column(db.String)
    submitted = db.Column(db.Boolean)
    owned_by_corp = db.Column(db.Boolean)
    vehicle_released_to = db.Column(db.String)
    date_released = db.Column(db.DateTime)
    time_released = db.Column(db.String)
    intersection_or_address_of_offence = db.Column(db.String)
    offence_city = db.Column(db.String)
    corporation_name = db.Column(db.String)
    regist_owner_last_name = db.Column(db.String)
    regist_owner_first_name = db.Column(db.String)
    regist_owner_address = db.Column(db.String)
    regist_owner_dob = db.Column(db.DateTime)
    regist_owner_city = db.Column(db.String)
    regist_owner_prov = db.Column(db.String)
    regist_owner_postal = db.Column(db.String)
    regist_owner_phone = db.Column(db.String)
    regist_owner_email = db.Column(db.String)
    impound_lot_operator = db.Column(
        db.Integer, db.ForeignKey('impound_lot_operator.id'))
    confirmation_of_service = db.Column(db.Boolean)
    confirmation_of_service_date = db.Column(db.DateTime)
    task_processing_status = db.Column(db.String)
    created_by = db.Column(db.String, db.ForeignKey('user.user_guid'))
    updated_by = db.Column(db.String)
    created_dt = db.Column(db.DateTime)
    updated_dt = db.Column(db.DateTime)

    twenty_four_hour_form = db.relationship(
        'TwentyFourHourForm',
        backref='event',
        lazy='joined',
        uselist=False)

    twelve_hour_form = db.relationship(
        'TwelveHourForm',
        backref='event',
        lazy='joined',
        uselist=False)

    vi_form = db.relationship(
        'VIForm',
        backref='event',
        lazy='joined',
        uselist=False)

    irp_form = db.relationship(
        'IRPForm',
        backref='event',
        lazy='joined',
        uselist=False)


@dataclass
class TwentyFourHourForm(db.Model):
    __tablename__ = 'twenty_four_hour_form'

    form_id: int
    event_id: int
    vehicle_impounded: str
    reason_for_not_impounding: str
    reasonable_ground_other_reason: str
    prescribed_test_used: str
    reasonable_date_of_test: datetime
    reasonable_time_of_test: str
    reason_for_not_using_prescribed_test: str
    resonable_test_used_alcohol: str
    reasonable_asd_expiry_date: datetime
    reasonable_result_alcohol: str
    reasonable_bac_result_mg: str
    resonable_approved_instrument_used: str
    reasonable_test_used_drugs: str
    reasonable_can_drive_drug: bool
    reasonable_can_drive_alcohol: bool
    requested_can_drive_alcohol: bool
    requested_can_drive_drug: bool
    requested_approved_instrument_used: str
    requested_BAC_result: str
    requested_alcohol_test_result: str
    requested_ASD_expiry_date: datetime
    time_of_requested_test: str
    requested_test_used_alcohol: str
    requested_test_used_drug: str
    requested_prescribed_test: str
    witnessed_by_officer: bool
    admission_by_driver: bool
    independent_witness: bool
    reasonable_ground_other: bool
    twenty_four_hour_number: str
    created_dt: datetime
    updated_dt: datetime

    form_id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.event_id'))
    vehicle_impounded = db.Column(db.String)
    reason_for_not_impounding = db.Column(db.String)
    reasonable_ground_other_reason = db.Column(db.String)
    prescribed_test_used = db.Column(db.String)
    reasonable_date_of_test = db.Column(db.DateTime)
    reasonable_time_of_test = db.Column(db.String)
    reason_for_not_using_prescribed_test = db.Column(db.String)
    resonable_test_used_alcohol = db.Column(db.String)
    reasonable_asd_expiry_date = db.Column(db.DateTime)
    reasonable_result_alcohol = db.Column(db.String)
    reasonable_bac_result_mg = db.Column(db.String)
    resonable_approved_instrument_used = db.Column(db.String)
    reasonable_test_used_drugs = db.Column(db.String)
    reasonable_can_drive_drug = db.Column(db.Boolean)
    reasonable_can_drive_alcohol = db.Column(db.Boolean)
    requested_can_drive_alcohol = db.Column(db.Boolean)
    requested_can_drive_drug = db.Column(db.Boolean)
    requested_approved_instrument_used = db.Column(db.String)
    requested_BAC_result = db.Column(db.String)
    requested_alcohol_test_result = db.Column(db.String)
    requested_ASD_expiry_date = db.Column(db.DateTime)
    time_of_requested_test = db.Column(db.String)
    requested_test_used_alcohol = db.Column(db.String)
    requested_test_used_drug = db.Column(db.String)
    requested_prescribed_test = db.Column(db.String)
    witnessed_by_officer = db.Column(db.Boolean)
    admission_by_driver = db.Column(db.Boolean)
    independent_witness = db.Column(db.Boolean)
    reasonable_ground_other = db.Column(db.Boolean)
    twenty_four_hour_number = db.Column(db.String)
    created_dt = db.Column(db.DateTime)
    updated_dt = db.Column(db.DateTime)


@dataclass
class TwelveHourForm(db.Model):
    __tablename__ = 'twelve_hour_form'

    form_id: int
    event_id: int
    created_dt: datetime
    updated_dt: datetime
    driver_phone: str
    twelve_hour_number: str
    vehicle_location: str

    form_id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.event_id'))
    created_dt = db.Column(db.DateTime)
    updated_dt = db.Column(db.DateTime)
    driver_phone = db.Column(db.String)
    twelve_hour_number = db.Column(db.String)
    vehicle_location = db.Column(db.String)


@dataclass
class IRPForm(db.Model):
    __tablename__ = 'irp_form'

    form_id: int
    event_id: int
    created_dt: datetime
    updated_dt: datetime

    form_id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.event_id'))
    created_dt = db.Column(db.DateTime)
    updated_dt = db.Column(db.DateTime)


@dataclass
class VIForm(db.Model):
    __tablename__ = 'vi_form'

    form_id: int
    event_id: int
    created_dt: datetime
    updated_dt: datetime
    gender: str
    driver_is_regist_owner: bool
    driver_licence_expiry: datetime
    driver_licence_class: str
    unlicenced_prohibition_number: str
    belief_driver_bc_resident: str
    out_of_province_dl: str
    out_of_province_dl_number: str
    out_of_province_dl_expiry: str
    out_of_province_dl_jurisdiction: str
    date_of_impound: datetime
    irp_impound: str
    irp_impound_duration: str
    IRP_number: str
    VI_number: str
    excessive_speed: str
    prohibited: bool
    suspended: bool
    street_racing: bool
    stunt_driving: bool
    motorcycle_seating: bool
    motorcycle_restrictions: bool
    unlicensed: bool
    linkage_location_of_keys: bool
    linkage_location_of_keys_explanation: str
    linkage_driver_principal: bool
    linkage_owner_in_vehicle: bool
    linkage_owner_aware_possesion: bool
    linkage_vehicle_transfer_notice: bool
    linkage_other: bool
    speed_limit: str
    vehicle_speed: str
    speed_estimation_technique: str
    speed_confirmation_technique: str
    incident_details: str
    incident_details_extra_page: bool

    form_id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.event_id'))
    gender = db.Column(db.String)
    driver_is_regist_owner = db.Column(db.String)
    driver_licence_expiry = db.Column(db.DateTime)
    driver_licence_class = db.Column(db.String)
    unlicenced_prohibition_number = db.Column(db.String)
    belief_driver_bc_resident = db.Column(db.String)
    out_of_province_dl = db.Column(db.String)
    out_of_province_dl_number = db.Column(db.String)
    out_of_province_dl_expiry = db.Column(db.String)
    out_of_province_dl_jurisdiction = db.Column(db.String)
    date_of_impound = db.Column(db.DateTime)
    irp_impound = db.Column(db.String)
    irp_impound_duration = db.Column(db.String)
    IRP_number = db.Column(db.String)
    VI_number = db.Column(db.String)
    excessive_speed = db.Column(db.Boolean)
    prohibited = db.Column(db.Boolean)
    suspended = db.Column(db.Boolean)
    street_racing = db.Column(db.Boolean)
    stunt_driving = db.Column(db.Boolean)
    motorcycle_seating = db.Column(db.Boolean)
    motorcycle_restrictions = db.Column(db.Boolean)
    unlicensed = db.Column(db.Boolean)
    linkage_location_of_keys = db.Column(db.Boolean)
    linkage_location_of_keys_explanation = db.Column(db.String)
    linkage_driver_principal = db.Column(db.Boolean)
    linkage_owner_in_vehicle = db.Column(db.Boolean)
    linkage_owner_aware_possesion = db.Column(db.Boolean)
    linkage_vehicle_transfer_notice = db.Column(db.Boolean)
    linkage_other = db.Column(db.Boolean)
    speed_limit = db.Column(db.String)
    vehicle_speed = db.Column(db.String)
    speed_estimation_technique = db.Column(db.String)
    speed_confirmation_technique = db.Column(db.String)
    incident_details = db.Column(db.String)
    incident_details_extra_page = db.Column(db.Boolean)
    created_dt = db.Column(db.DateTime)
    updated_dt = db.Column(db.DateTime)


@dataclass
class FormStorageRefs(db.Model):
    __tablename__ = 'form_storage_refs'

    form_id_24h: int
    form_id_irp: int
    form_id_vi: int
    form_id_12h: int
    event_id: int
    form_type: str
    # vi, irp, 24h, 12h
    storage_key: str
    encryptiv: str
    created_dt: datetime
    updated_dt: datetime

    storage_key = db.Column(db.String, primary_key=True)
    form_id_24h = db.Column(db.Integer, db.ForeignKey(
        'twenty_four_hour_form.form_id'))
    form_id_irp = db.Column(db.Integer, db.ForeignKey('irp_form.form_id'))
    form_id_vi = db.Column(db.Integer, db.ForeignKey('vi_form.form_id'))
    form_id_12h = db.Column(
        db.Integer, db.ForeignKey('twelve_hour_form.form_id'))
    event_id = db.Column(db.Integer, db.ForeignKey('event.event_id'))
    form_type = db.Column(db.String)
    encryptiv = db.Column(db.String)
    created_dt = db.Column(db.DateTime)
    updated_dt = db.Column(db.DateTime)



@dataclass
class AgencyCrossref(db.Model):
    __tablename__ = 'agency_cross_refs'

    agency_name: str
    agency_id: str
    agency_city: str
    prime_vjur: str
    icbc_detachment_name: str
    icbc_city_name: str
    vips_policedetachments_agency_id: str
    vips_policedetachments_agency_nm: str

    agency_name = db.Column(db.String, primary_key=True)
    agency_id = db.Column(db.String)
    agency_city = db.Column(db.String)
    prime_vjur = db.Column(db.String)
    icbc_detachment_name = db.Column(db.String)
    icbc_city_name = db.Column(db.String)
    vips_policedetachments_agency_id = db.Column(db.String)
    vips_policedetachments_agency_nm = db.Column(db.String)

@dataclass
class JurisdictionCrossRef(db.Model):
    __tablename__ = 'jurisdiction_cross_ref'

    jurisdiction_name: str
    jurisdiction_code: str
    prime_jurisdiction_code: str
    prime_jurisdiction_name: str
    icbc_jurisdiction_code: str
    icbc_jurisdiction: str
    vips_jurisdictions_objectCd: str
    vips_jurisdictions_objectDsc: str

    jurisdiction_name = db.Column(db.String)
    jurisdiction_code = db.Column(db.String, primary_key=True)
    prime_jurisdiction_code = db.Column(db.String)
    prime_jurisdiction_name = db.Column(db.String)
    icbc_jurisdiction_code = db.Column(db.String)
    icbc_jurisdiction = db.Column(db.String)
    vips_jurisdictions_objectCd = db.Column(db.String)
    vips_jurisdictions_objectDsc = db.Column(db.String)

@dataclass
class CityCrossRef(db.Model):
    __tablename__ = 'city_cross_ref'

    city_code: str
    city_name: str
    icbc_city_code: str
    icbc_city_name: str
    icbc_city_name_legacy: str
    vips_city_name: str

    city_code = db.Column(db.String, primary_key=True)
    city_name = db.Column(db.String)
    icbc_city_code = db.Column(db.String)
    icbc_city_name = db.Column(db.String)
    icbc_city_name_legacy = db.Column(db.String)
    vips_city_name = db.Column(db.String)

@dataclass
class ImpoundReasonCodes(db.Model):
    __tablename__ = 'impound_reason_codes'

    df_unique_code: str
    impound_reason_name: str
    vips_value_cd: str
    vips_value_dsc: str
    vips_value_abbreviated_dsc: str  

    df_unique_code = db.Column(db.String, primary_key=True)
    impound_reason_name = db.Column(db.String)
    vips_value_cd = db.Column(db.String)
    vips_value_dsc = db.Column(db.String)
    vips_value_abbreviated_dsc = db.Column(db.String)

@dataclass
class IloIdCrossRef(db.Model):
    __tablename__ = 'ilo_cross_ref'

    ilo_name: str
    vips_impound_lot_operator_id: int

    ilo_name = db.Column(db.String, primary_key=True)
    vips_impound_lot_operator_id = db.Column(db.Integer)
    
    

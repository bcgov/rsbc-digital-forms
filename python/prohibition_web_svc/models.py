from datetime import datetime, timedelta
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging

db = SQLAlchemy()
migrate = Migrate()

class Form(db.Model):
    id = db.Column('id', db.String(20), primary_key=True)
    form_type = db.Column(db.String(20), nullable=False)
    lease_expiry = db.Column(db.Date, nullable=True)
    printed_timestamp = db.Column(db.DateTime, nullable=True)
    user_guid = db.Column(db.String(80), db.ForeignKey('user.user_guid'), nullable=True)

    # Note: The printed timestamp prior to v0.4.17 was saved in local Pacific time instead of GMT

    def __init__(self, form_id, form_type, printed=None, lease_expiry=None, user_guid=None):
        self.id = form_id
        self.form_type = form_type
        self.printed_timestamp = printed
        self.lease_expiry = lease_expiry
        self.user_guid = user_guid

    @staticmethod
    def serialize(form):
        return {
            "id": form.id,
            "form_type": form.form_type,
            "lease_expiry": Form._format_lease_expiry(form.lease_expiry),
            "printed_timestamp": form.printed_timestamp,
            "user_guid": form.user_guid
        }

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
    user_guid = db.Column(db.String(80), db.ForeignKey('user.user_guid'), primary_key=True)
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
    
    id:int
    vjur:str
    agency_name:str
    
    id = db.Column(db.Integer, primary_key=True)
    vjur = db.Column(db.String)
    agency_name = db.Column(db.String)
    
@dataclass
class City(db.Model):
    __tablename__ = 'city'
    
    id:int
    objectCd:str
    objectDsc:str
    
    id = db.Column(db.Integer, primary_key=True)
    objectCd = db.Column(db.String)
    objectDsc = db.Column(db.String)

@dataclass    
class Country(db.Model):
    __tablename__ = 'country'
    
    id:int
    objectCd:str
    objectDsc:str
    
    id = db.Column(db.Integer, primary_key=True)
    objectCd = db.Column(db.String)
    objectDsc = db.Column(db.String)

@dataclass    
class ImpoundLotOperator(db.Model):
    __tablename__ = 'impound_lot_operator'
    
    id:int
    name:str
    lot_address:str
    city:str
    phone:str
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    lot_address = db.Column(db.String)
    city = db.Column(db.String)
    phone = db.Column(db.String)

@dataclass    
class Jurisdiction(db.Model):
    __tablename__ = 'jurisdiction'
    
    id:int
    objectCd:str
    objectDsc:str
    
    id = db.Column(db.Integer, primary_key=True)
    objectCd = db.Column(db.String)
    objectDsc = db.Column(db.String)

@dataclass    
class Permission(db.Model):
    __tablename__ = 'permission'
    
    id:int
    role:str
    permission:str
    
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String)
    permission = db.Column(db.String)

@dataclass
class Province(db.Model):
    __tablename__ = 'province'
    
    id:int
    objectCd:str
    objectDsc:str
    
    id = db.Column(db.Integer, primary_key=True)
    objectCd = db.Column(db.String)
    objectDsc = db.Column(db.String)

@dataclass    
class VehicleStyle(db.Model):
    __tablename__ = 'vehicle_style'
    
    code:str
    name:str
    
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)

@dataclass
class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    
    id:int
    mk:str
    search:str
    md:str
    
    id = db.Column(db.Integer, primary_key=True)
    mk = db.Column(db.String)
    search = db.Column(db.String)
    md = db.Column(db.String)
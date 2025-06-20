from datetime import datetime
from .base import db

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
    last_active = db.Column(db.DateTime, nullable=True)

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
        self.last_active = datetime.now()

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
            "login": user.login,
            "last_active": user.last_active,
        }

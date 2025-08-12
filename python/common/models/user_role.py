from .base import db

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
            "agency_id": rows.agency_id,
            "agency": rows.agency_name,
            "approved_dt": rows.approved_dt,
            "badge_number": rows.badge_number,
            "first_name": rows.first_name,
            "last_name": rows.last_name,
            "role_name": rows.role_name,
            "submitted_dt": rows.submitted_dt,
            "user_guid": rows.user_guid,
            "username": rows.username,
            "login": rows.login,
            "last_active": rows.last_active,
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

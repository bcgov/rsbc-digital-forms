import datetime
import json
import os
import pytest
import responses
from flask_api import FlaskAPI

os.environ['TESTING'] = 'true'

import python.common.ride_actions as ride_actions
from python.common.models.base import db
from python.common.models.df_errors import DFErrors
from python.common.models.province import Province
from python.common.models.jurisdiction_crossref import JurisdictionCrossRef
from python.common.models.vehicle import Vehicle
from python.common.models.vehicle_style import VehicleStyle
from python.common.models.vehicle_type import VehicleType
from python.common.models.city import City
from python.form_handler.config import Config
from python.common.config import Config as CommonConfig

application = FlaskAPI(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config['TESTING'] = True
db.init_app(application)

@pytest.fixture
def event_data():
  return {
    'created_dt': datetime.datetime(2021, 1, 1, 16 ,00, 00),
    'type_of_prohibition': 'alcohol',
    'driver_licence_no': '01234567',
    'driver_city': 'VANCOUVER',
    'driver_prov': 'CA_BC',
    'driver_postal': 'V6B1A1',
    'driver_jurisdiction': 'CA_BC',
    'driver_dob': datetime.datetime(1990, 1, 1, 8, 0, 0),
    'vehicle_jurisdiction': 'CA_BC',
    'vehicle_plate_no': 'ABC123',
    'vehicle_registration_no': '879665',
    'vehicle_year': '2010',
    'vehicle_mk_md': 'FORD-MUST',
    'vehicle_style': '3DR',
    'owned_by_corp': False,
    'corporation_name': '',
    'date_of_driving': datetime.datetime(2021, 1, 1, 8, 0, 0),
    'time_of_driving': '12:00',
    'agency_file_no': 'Ag456',
    'date_released': datetime.datetime(2021, 1, 1, 8, 0, 0),
    'time_released': '12:30',
    'vehicle_type': 1,
    'intersection_or_address_of_offence': 'Main St',
    'offence_city': 'VAN',
  }

@pytest.fixture
def form_data():
  return {
    'twelve_hour_number': 'VZ3456',
  }

@pytest.fixture
def user_data():
  return {
    'display_name': 'John Doe',
    'badge_number': '123456',
    'agency_ref': {
      'id': 1,
      'agency_name': 'Vancouver Police Dept.',
      'vjur': 'VA'
    }
  }

@pytest.fixture
def app():    
    with application.app_context():
        # Only create the specific table we need for testing
        DFErrors.__table__.create(db.engine, checkfirst=True)
        Province.__table__.create(db.engine, checkfirst=True)
        JurisdictionCrossRef.__table__.create(db.engine, checkfirst=True)
        Vehicle.__table__.create(db.engine, checkfirst=True)
        VehicleStyle.__table__.create(db.engine, checkfirst=True)
        VehicleType.__table__.create(db.engine, checkfirst=True)
        City.__table__.create(db.engine, checkfirst=True)
        # Add necessary reference data
        db.session.add(Province(id=1, objectDsc='BRITISH COLUMBIA', objectCd='CA_BC'))
        db.session.add(JurisdictionCrossRef(jurisdiction_code='CA_BC', jurisdiction_name='BRITISH COLUMBIA'))
        db.session.add(Vehicle(id=1, mk='FORD', md='MUST', search='FORD - MUSTANG'))
        db.session.add(VehicleStyle(name='3-DOOR HATCH', code='3DR'))
        db.session.add(VehicleType(description='PASSENGER', type_cd=1))
        db.session.add(City(id=1, objectCd='VAN', objectDsc='VANCOUVER'))
        db.session.commit()
        yield application
        # Clean up
        DFErrors.__table__.drop(db.engine, checkfirst=True)
        Province.__table__.drop(db.engine, checkfirst=True)
        JurisdictionCrossRef.__table__.drop(db.engine, checkfirst=True)
        Vehicle.__table__.drop(db.engine, checkfirst=True)
        VehicleStyle.__table__.drop(db.engine, checkfirst=True)
        VehicleType.__table__.drop(db.engine, checkfirst=True)
        City.__table__.drop(db.engine, checkfirst=True)

@responses.activate
def test_twelve_hours_event_valid_input(app, event_data, form_data, user_data):
  responses.add(responses.POST, 
                f'{CommonConfig.RIDE_API_URL}/dfV2events/12hrsubmitted', 
                json={'status': 'success', 'message': 'Event created successfully'}, status=200)
  
  flag, args = ride_actions.twelve_hours_event(
     message={'event_id': 123},
     event_data=event_data, 
     form_data=form_data, 
     user_data=user_data, 
     db=db,
     app=app)
  
  assert flag == True
  assert len(responses.calls) == 1
  assert responses.calls[0].request.body.decode() == json.dumps({
     'typeofevent': '12hr_submitted',
     'twelveHoursPayload': {
          'eventType': '12hr_submitted',
          'twelveHourNumber': 'VZ3456',
          'typeOfProhibition': 'alcohol',
          'eventID': 123,
          'eventVersion': 1.0,
          'eventDtm': '2021-01-01 08:00:00',
          'driverLicenceNumber': '01234567',
          'driverCityTown': 'VANCOUVER',
          'driverProvince': 'BRITISH COLUMBIA',
          'driverPostalCode': 'V6B1A1',
          'driverJurisdiction': 'BRITISH COLUMBIA',
          'driverDateOfBirth': '1990-01-01',
          'vehicleJurisdiction': 'BRITISH COLUMBIA',
          'vehiclePlateNumber': 'ABC123',
          'vehicleRegistrationNumber': '879665',
          'vehicleYear': '2010',
          'vehicleMakeModel': 'FORD - MUSTANG',
          'vehicleStyle': '3-DOOR HATCH',
          'ownedByCorp': False,
          'corporationName': '',
          'dateOfDriving': '2021-01-01',
          'timeOfDriving': '12:00',
          'agencyFileNumber': 'Ag456',
          'dateReleased': '2021-01-01',
          'timeReleased': '12:30',
          'vehicleTypeDesc': 'PASSENGER',
          'addressOfOffence': 'Main St',
          'offenceCity': 'VANCOUVER',
          'officerDisplayName': 'John Doe',
          'officerBadgeNumber': '123456',
          'enforcementAgencyName': 'Vancouver Police Dept.',
          'vjurCde': 'VA',
      }
  })

@responses.activate
def test_twelve_hours_event_invalid_input(app, user_data):
  # Test with invalid input data
  responses.add(responses.POST, 
              f'{CommonConfig.RIDE_API_URL}/dfV2events/12hrsubmitted', 
              json={'status': 'success', 'message': 'Event created successfully'}, status=200)
    
  flag, args = ride_actions.twelve_hours_event(
     message={'event_id': 123},
     event_data={}, 
     form_data={}, 
     user_data=user_data, 
     db=db,
     app=app)
  
  assert flag == False
  assert len(responses.calls) == 0

@responses.activate
def test_twelve_hours_event_invalid_response(app, event_data, form_data, user_data):
  # Test with invalid response from RIDE API
  responses.add(responses.POST, 
              f'{CommonConfig.RIDE_API_URL}/dfV2events/12hrsubmitted', 
              json={'status': 'failed', 'message': 'Event creation failed'}, status=400)
    
  flag, args = ride_actions.twelve_hours_event(
     message={'event_id': 123},
     event_data=event_data, 
     form_data=form_data, 
     user_data=user_data, 
     db=db,
     app=app)
  
  assert flag == False
  assert len(responses.calls) == 1


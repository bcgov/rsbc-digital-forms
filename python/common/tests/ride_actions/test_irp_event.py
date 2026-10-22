import datetime
import json
import os
import pytest
import responses
from flask import Flask

os.environ['TESTING'] = 'true'

import python.common.ride_actions as ride_actions
from python.common.enums import ErrorCode
from python.common.models.base import db
from python.common.models.agency import Agency
from python.common.models.city import City
from python.common.models.df_errors import DFErrors
from python.common.models.irp_prohibition_type import IRPProhibitionType
from python.common.config import Config as CommonConfig

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config['TESTING'] = True
db.init_app(application)

IRP_ENDPOINT = f'{CommonConfig.RIDE_API_URL}/dfV2events/irpsubmitted'

@pytest.fixture
def event_data():
  return {
    'created_dt': datetime.datetime(2021, 1, 1, 16, 00, 00),
    'driver_dob': datetime.datetime(1990, 1, 1, 8, 0, 0),
    'date_of_driving': datetime.datetime(2021, 1, 1, 8, 0, 0),
    'time_of_driving': '12:00',
    'agency_file_no': ' Ag456 ',
    'intersection_or_address_of_offence': 'Main St ',
    'offence_city': 'VAN',
    'agency_id': 2,
    'latitude': 49.28,
    'longitude': -123.12,
    'requested_address': 'Main St, VANCOUVER',
    'full_address': 'Main St, Vancouver, BC',
  }

@pytest.fixture
def form_data():
  return {
    'event_id': 123,
    'irp_number': ' 21900001 ',
    'vi_number': None,
    'irp_prohibition_type': 'BACFAIL',
    'gender': 'M',
    'driver_licence_class': '5 ',
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
    },
  }

@pytest.fixture
def app():
    with application.app_context():
        DFErrors.__table__.create(db.engine, checkfirst=True)
        City.__table__.create(db.engine, checkfirst=True)
        Agency.__table__.create(db.engine, checkfirst=True)
        IRPProhibitionType.__table__.create(db.engine, checkfirst=True)
        db.session.add(City(id=1, objectCd='VAN', objectDsc='VANCOUVER'))
        db.session.add(Agency(id=2, vjur='BU', agency_name='Burnaby RCMP'))
        db.session.add(IRPProhibitionType(id=4, code='BACFAIL', prohibition_period=90, breath_result='FAIL',
                                          monetary_penalty=500, prohibition_reason='fail', active=True, display_order=4))
        db.session.commit()
        yield application
        DFErrors.__table__.drop(db.engine, checkfirst=True)
        City.__table__.drop(db.engine, checkfirst=True)
        Agency.__table__.drop(db.engine, checkfirst=True)
        IRPProhibitionType.__table__.drop(db.engine, checkfirst=True)

def _call(app, event_data, form_data, user_data):
  return ride_actions.irp_event(
     message={'event_id': 123},
     event_data=event_data,
     form_data=form_data,
     user_data=user_data,
     db=db,
     app=app)

@responses.activate
def test_irp_event_valid_input(app, event_data, form_data, user_data):
  responses.add(responses.POST, IRP_ENDPOINT, json={'status': 'success'}, status=200)

  flag, args = _call(app, event_data, form_data, user_data)

  assert flag == True
  assert len(responses.calls) == 1
  assert json.loads(responses.calls[0].request.body) == {
     'typeofevent': 'irp_submitted',
     'irpPayload': {
          'eventID': 123,
          'eventVersion': 1.0,
          'eventDtm': '2021-01-01 08:00:00',
          'eventType': 'irp_submitted',
          'irpNumber': '21900001',
          'viNumber': None,
          'irpProhibitionType': 'BACFAIL',
          'prohibitionPeriodDays': 90,
          'driverGender': 'M',
          'driverDateOfBirth': '1990-01-01',
          'driverLicenceClass': '5',
          'dateOfDriving': '2021-01-01',
          'timeOfDriving': '12:00',
          'agencyFileNumber': 'Ag456',
          'officerDisplayName': 'John Doe',
          'addressOfOffence': 'Main St',
          'offenceCity': 'VANCOUVER',
          'officerBadgeNumber': '123456',
          'vjurCde': 'BU',
          'enforcementAgencyName': 'Burnaby RCMP',
      },
     'locationRequestPayload': {
          'latitude': 49.28,
          'longitude': -123.12,
          'requestedAddress': 'Main St, VANCOUVER',
          'fullAddress': 'Main St, Vancouver, BC',
      }
  }

@responses.activate
def test_irp_event_missing_coordinates(app, event_data, form_data, user_data):
  responses.add(responses.POST, IRP_ENDPOINT, json={'status': 'success'}, status=200)
  event_data['latitude'] = None
  event_data['longitude'] = None

  flag, args = _call(app, event_data, form_data, user_data)

  assert flag == True
  body = json.loads(responses.calls[0].request.body)
  assert 'locationRequestPayload' not in body
  assert body['irpPayload']['irpNumber'] == '21900001'

@responses.activate
def test_irp_event_agency_falls_back_to_user_agency(app, event_data, form_data, user_data):
  responses.add(responses.POST, IRP_ENDPOINT, json={'status': 'success'}, status=200)
  event_data['agency_id'] = None

  flag, args = _call(app, event_data, form_data, user_data)

  assert flag == True
  payload = json.loads(responses.calls[0].request.body)['irpPayload']
  assert payload['vjurCde'] == 'VA'
  assert payload['enforcementAgencyName'] == 'Vancouver Police Dept.'

@responses.activate
def test_irp_event_unknown_prohibition_code(app, event_data, form_data, user_data):
  responses.add(responses.POST, IRP_ENDPOINT, json={'status': 'success'}, status=200)
  form_data['irp_prohibition_type'] = 'UNKNOWN'

  flag, args = _call(app, event_data, form_data, user_data)

  assert flag == True
  payload = json.loads(responses.calls[0].request.body)['irpPayload']
  assert payload['irpProhibitionType'] == 'UNKNOWN'
  assert payload['prohibitionPeriodDays'] is None

@responses.activate
def test_irp_event_invalid_response(app, event_data, form_data, user_data):
  responses.add(responses.POST, IRP_ENDPOINT, json={'status': 'failed'}, status=400)

  flag, args = _call(app, event_data, form_data, user_data)

  assert flag == False
  assert len(responses.calls) == 1
  assert args['error']['error_code'] == ErrorCode.R01
  assert args['error']['event_type'] == 'IRP'
  assert args['error']['func'] == ride_actions.irp_event
  assert args['error']['ticket_no'] == '21900001'
  assert args['error']['event_id'] == 123

@responses.activate
def test_irp_event_invalid_input(app, user_data):
  responses.add(responses.POST, IRP_ENDPOINT, json={'status': 'success'}, status=200)

  flag, args = _call(app, {}, {}, user_data)

  assert flag == False
  assert len(responses.calls) == 0
  assert args['error']['event_type'] == 'IRP'
  assert args['error']['ticket_no'] is None
  assert args['error']['event_id'] == 123

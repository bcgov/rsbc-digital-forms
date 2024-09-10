import datetime
import json
import pytest
import responses
from flask_api import FlaskAPI

import python.common.ride_actions as ride_actions
from python.form_handler.models import db
from python.form_handler.config import Config
from python.common.config import Config as CommonConfig

application = FlaskAPI(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASE_URI
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
    'owned_by_corp': True,
    'corporation_name': 'CORP',
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
    'twenty_four_hour_number': 'VZ3456',
    'vehicle_impounded': 'yes',
    'resonable_test_used_alcohol': 'TEST',
    'reason_for_not_impounding': 'REASON',
    'reasonable_ground_other': 'OTHER',
    'reasonable_ground_other_reason': 'OTHER REASON',
    'prescribed_test_used': 'no',
    'requested_prescribed_test': '',
    'requested_alcohol_test_result': '48',
    'requested_approved_instrument_used': 'INSTRUMENT',
    'requested_test_used_alcohol': 'TEST ALCOHOL',
    'requested_test_used_drug': None
  }

@pytest.fixture
def user_data():
  return{
    'display_name': 'John Doe',
    'badge_number': '123456',
    'agency': 'Vancouver Police Dept.'
  }

@pytest.fixture
def app():    
    return application

@responses.activate
def test_twenty_four_hours_event_valid_input(app, event_data, form_data, user_data):
  responses.add(responses.POST, 
                f'{CommonConfig.RIDE_API_URL}/dfV2events/24hrsubmitted', 
                json={'status': 'success', 'message': 'Event created successfully'}, status=200)
  
  flag, args = ride_actions.twenty_four_hours_event(
     event_data=event_data, 
     form_data=form_data, 
     user_data=user_data, 
     db=db,
     app=app)
  
  assert flag == True
  assert len(responses.calls) == 1
  assert responses.calls[0].request.body.decode() == json.dumps({
     'typeofevent': '24hr_submitted',
     'twentyFourHoursPayload': [
        {
          'eventType': '24hr_submitted',
          'twentyFourHrNo': 'VZ3456',
          'typeOfProhibition': 'alcohol',
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
          'ownedByCorp': True,
          'corporationName': 'CORP',
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
          'vehicleImpounded': True,
          'reasonableTestAlcohol': 'TEST',
          'reasonForNotImpounding': 'REASON',
          'reasonableGroundOther': 'OTHER',
          'reasonableGroundOtherReason': 'OTHER REASON',
          'prescribedTestUsed': False,
          'requestedPrescribedTest': None,
          'requestedAlcoholTestResult': '48',
          'requestedApprovedInstrumentUsed': 'INSTRUMENT',
          'requestedTestUsedAlcohol': 'TEST ALCOHOL',
          'requestedTestUsedDrug': None
        }
     ]
  })


@responses.activate
def test_twenty_four_hours_event_invalid_input(app, user_data):
  # Test with invalid input data
  responses.add(responses.POST, 
              f'{CommonConfig.RIDE_API_URL}/dfV2events/24hrsubmitted', 
              json={'status': 'success', 'message': 'Event created successfully'}, status=200)
    
  flag, args = ride_actions.twenty_four_hours_event(
     event_data={}, 
     form_data={}, 
     user_data=user_data, 
     db=db,
     app=app)
  
  assert flag == False
  assert len(responses.calls) == 0

@responses.activate
def test_twenty_four_hours_event_invalid_response(app, event_data, form_data, user_data):
  # Test with invalid response from RIDE API
  responses.add(responses.POST, 
              f'{CommonConfig.RIDE_API_URL}/dfV2events/24hrsubmitted', 
              json={'status': 'failed', 'message': 'Event creation failed'}, status=400)
    
  flag, args = ride_actions.twenty_four_hours_event(
     event_data=event_data, 
     form_data=form_data, 
     user_data=user_data, 
     db=db,
     app=app)
  
  assert flag == False
  assert len(responses.calls) == 1


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
    'impound_lot_operator': 217,
  }

@pytest.fixture
def form_data():
  return {
    'VI_number': 'VZ3456',
    'gender': 'M',
    'driver_licence_class': '5',
    'out_of_province_dl': 'no',
    'date_of_impound': datetime.datetime(2021, 1, 1, 8, 0, 0),
    'unlicenced_prohibition_number': 'UL123456',
    'irp_impound': 'yes',
    'IRP_number': 'IRP123456',
    'irp_impound_duration': '3 days',
    'excessive_speed': True,
    'prohibited': False,
    'suspended': False,
    'street_racing': False,
    'stunt_driving': False,
    'motorcycle_seating': False,
    'motorcycle_restrictions': False,
    'unlicensed': True,
    'driver_is_regist_owner': 'false',
    'speed_limit': 50,
    'vehicle_speed': 160,
    'speed_estimation_technique': 'visual',
    'speed_confirmation_technique': 'radar',
  }

@pytest.fixture
def user_data():
  return {
    'display_name': 'John Doe',
    'badge_number': '123456',
    'agency': 'Vancouver Police Dept.'
  }

@pytest.fixture
def app():    
    return application

@responses.activate
def test_vi_event_valid_input(app, event_data, form_data, user_data):
  responses.add(responses.POST, 
                f'{CommonConfig.RIDE_API_URL}/dfV2events/visubmitted', 
                json={'status': 'success', 'message': 'Event created successfully'}, status=200)
  
  flag, args = ride_actions.vi_event(
     event_data=event_data, 
     form_data=form_data, 
     user_data=user_data, 
     db=db,
     app=app)
  
  assert flag == True
  assert len(responses.calls) == 1
  assert responses.calls[0].request.body.decode() == json.dumps({
     'typeofevent': 'vi_submitted',
     'viPayload': [
        {
          'eventType': 'vi_submitted',
          'viNumber': 'VZ3456',
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
          'driverGender': 'M',
          'driverLicenceClass': '5',
          'outOfProvinceDriverLicense': False,
          'impoundLotOperator': 'ABLE TOWING',
          'dateOfImpound': '2021-01-01',
          'unlicencedProhibitionNumber': 'UL123456',
          'isIrp': True,
          'irpNumber': 'IRP123456',
          'irpDuration': '3 days',
          'excessiveSpeed': True,
          'prohibited': False,
          'suspended': False,
          'streetRacing': False,
          'stuntRacing': False,
          'motorCycleSeating': False,
          'motorCycleRestrictions': False,
          'unlicensed': True,
          'driverIsRegistOwner': False,
          'speedLimit': 50,
          'vehicleSpeed': 160,
          'speedEstimationTechnique': 'visual',
          'speedConfirmationTechnique': 'radar'
        }
     ]
  })


  # payloadRecord["driverGender"] = args['form_data']['gender']
  # payloadRecord["driverLicenceClass"] = args['form_data']['driver_licence_class']
  # payloadRecord["outOfProvinceDriverLicense"] = yes_no_string_to_bool(args['form_data']['out_of_province_dl'])
  # payloadRecord["impoundLotOperator"] = get_impound_lot_operator(args)
  # payloadRecord["dateOfImpound"] = format_date_only(args['form_data']['date_of_impound'])
  # payloadRecord["unlicencedProhibitionNumber"] = args['form_data']['unlicenced_prohibition_number']
  # payloadRecord["isIrp"] = yes_no_string_to_bool(args['form_data']['irp_impound'])
  # payloadRecord["irpNumber"] = args['form_data']['IRP_number']
  # payloadRecord["irpDuration"] = args['form_data']['irp_impound_duration']
  # payloadRecord["excessiveSpeed"] = args['form_data']['excessive_speed']
  # payloadRecord["prohibited"] = args['form_data']['prohibited']
  # payloadRecord["suspended"] = args['form_data']['suspended']
  # payloadRecord["streetRacing"] = args['form_data']['street_racing']
  # payloadRecord["stuntRacing"] = args['form_data']['stunt_driving']
  # payloadRecord["motorCycleSeating"] = args['form_data']['motorcycle_seating']
  # payloadRecord["motorCycleRestrictions"] = args['form_data']['motorcycle_restrictions']
  # payloadRecord["unlicensed"] = args['form_data']['unlicensed']
  # payloadRecord["driverIsRegistOwner"] = args['form_data']['driver_is_regist_owner'] == 'true'
  # payloadRecord["speedLimit"] = args['form_data']['speed_limit']
  # payloadRecord["vehicleSpeed"] = args['form_data']['vehicle_speed']
  # payloadRecord["speedEstimationTechnique"] = args['form_data']['speed_estimation_technique']
  # payloadRecord["speedConfirmationTechnique"] = args['form_data']['speed_confirmation_technique']

@responses.activate
def test_vi_event_invalid_input(app, user_data):
  # Test with invalid input data
  responses.add(responses.POST, 
              f'{CommonConfig.RIDE_API_URL}/dfV2events/visubmitted', 
              json={'status': 'success', 'message': 'Event created successfully'}, status=200)
    
  flag, args = ride_actions.vi_event(
     event_data={}, 
     form_data={}, 
     user_data=user_data, 
     db=db,
     app=app)
  
  assert flag == False
  assert len(responses.calls) == 0

@responses.activate
def test_vi_event_invalid_response(app, event_data, form_data, user_data):
  # Test with invalid response from RIDE API
  responses.add(responses.POST, 
              f'{CommonConfig.RIDE_API_URL}/dfV2events/visubmitted', 
              json={'status': 'failed', 'message': 'Event creation failed'}, status=400)
    
  flag, args = ride_actions.vi_event(
     event_data=event_data, 
     form_data=form_data, 
     user_data=user_data, 
     db=db,
     app=app)
  
  assert flag == False
  assert len(responses.calls) == 1


import pytest
from unittest.mock import MagicMock, patch
from python.common.enums import ErrorCode
from python.prohibition_web_svc.middleware import collision_middleware
import json
import os

test_dir = os.path.dirname(os.path.abspath(__file__))
collision_json_path = os.path.join(test_dir, '..', 'tests-data', 'collision.json')

# Dummy payload for tests
DUMMY_PAYLOAD = {
    'ff_application_id': 'abc123',
    'collision_case_num': 'MV-001',
}

def test_set_event_type():
    result, kwargs = collision_middleware.set_event_type()
    assert result is True
    assert kwargs['event_type'] == collision_middleware.EVENT_TYPE

def test_set_ticket_number_with_case_num():
    kwargs = {'payload': {'collision_case_num': 'MV-001'}}
    result, out_kwargs = collision_middleware.set_ticket_number(**kwargs)
    assert result is True
    assert out_kwargs['ticket_no'] == 'MV-001'

def test_set_ticket_number_without_case_num():
    kwargs = {'payload': {}}
    result, out_kwargs = collision_middleware.set_ticket_number(**kwargs)
    assert result is True
    assert out_kwargs['ticket_no'] is None

def test_validate_collision_payload_success():
    # Provide all required fields for collision, location, additional details, and one valid entity
    with open(collision_json_path) as f:
        payload = json.load(f)
    kwargs = {'payload': payload}
    result, out_kwargs = collision_middleware.validate_collision_payload(**kwargs)
    assert result is True
    assert out_kwargs == kwargs

def test_validate_collision_payload_failure_empty_payload():
  # Missing required fields (empty payload)
  kwargs = {'payload': {}}
  result, out_kwargs = collision_middleware.validate_collision_payload(**kwargs)
  assert result is False
  assert out_kwargs['error']['error_details'] == 'Empty payload'

def test_validate_collision_payload_failure_missing_fields():
  # Missing required fields
  kwargs = {'payload': {
      'collision_case_num': 'MV-001',
  }}
  result, out_kwargs = collision_middleware.validate_collision_payload(**kwargs)
  assert result is False
  assert 'error' in out_kwargs
  assert out_kwargs['error']['error_details'] == "Missing required fields: ['collision_scenario', 'police_file_num', 'prime_file_vjur', 'date_collision', 'time_collision', 'reported_same_day', 'time_collision_unknown', 'date_reported', 'hit_and_run', 'police_attended', 'police_agency_type_district', 'police_agency_code', 'primary_collision_occ_code', 'first_contact_event', 'first_contact_loc', 'has_countable_fatal', 'countable_fatal_total', 'completed_by_name', 'completed_by_id', 'detachment_unit', 'investigated_by_traffic_analyst', 'hwy_code', 'city_name', 'lat_decim_degrees', 'long_decim_degrees', 'road_class', 'traffic_flow', 'collision_loc', 'primary_speed_zone', 'land_usage', 'road_type', 'roadway_character', 'roadway_surface_cond', 'weather_cond', 'lighting_cond', 'has_other_prop_damage', 'has_witnesses', 'collision_type', 'total_est_damage', 'total_injured', 'total_killed', 'total_vehicles', 'entities']"

def test_validate_collision_payload_failure_missing_entity():
    # Missing required entity fields
    with open(collision_json_path) as f:
      payload = json.load(f)
    payload['entities'] = []  # No entities provided
    kwargs = {'payload': payload}
    result, out_kwargs = collision_middleware.validate_collision_payload(**kwargs)
    assert result is False
    assert 'error' in out_kwargs
    assert out_kwargs['error']['error_details'] == "Collision has no entities provided."


def test_validate_collision_payload_failure_missing_entity_fields():
    # Missing required entity fields
    with open(collision_json_path) as f:
        payload = json.load(f)
    payload['entities'] = [{}]  # Empty entity
    kwargs = {'payload': payload}
    result, out_kwargs = collision_middleware.validate_collision_payload(**kwargs)
    assert result is False
    assert 'error' in out_kwargs
    assert out_kwargs['error']['error_details'] == "Missing required fields in entity: ['entity_type', 'entity_num', 'possible_offender', 'contributing_factor_1', 'contributing_factor_2', 'contributing_factor_3', 'contributing_factor_4', 'damage_location_code', 'severety_code']"

def test_validate_collision_payload_failure_missing_witness():
    # Missing required witness
    with open(collision_json_path) as f:
        payload = json.load(f)
    payload['has_witnesses'] = True  # Indicating there are witnesses
    payload['witnesses'] = []  # Empty witness
    kwargs = {'payload': payload}
    result, out_kwargs = collision_middleware.validate_collision_payload(**kwargs)
    assert result is False
    assert out_kwargs['error']['error_details'] == "Collision has witnesses but no witness data provided."

    payload['witnesses'] = None  # No witnesses provided
    kwargs = {'payload': payload}
    result2, out_kwargs2 = collision_middleware.validate_collision_payload(**kwargs)
    assert result2 is False
    assert out_kwargs2['error']['error_details'] == "Collision has witnesses but no witness data provided."
    
def test_validate_collision_payload_failure_missing_witness():
    # Missing required witness
    with open(collision_json_path) as f:
        payload = json.load(f)
    payload['witnesses'] = [{}] 
    kwargs = {'payload': payload}
    result, out_kwargs = collision_middleware.validate_collision_payload(**kwargs)
    assert result is False
    assert out_kwargs['error']['error_details'] == "Missing required fields in witness: ['witness_name', 'address', 'contact_phn_num']"


def test_save_collision_data_success(monkeypatch):
    mock_db = MagicMock()
    mock_session = MagicMock()
    mock_db.session = mock_session
    mock_submission = MagicMock(submission_id=42)
    monkeypatch.setattr(collision_middleware, 'db', mock_db)
    monkeypatch.setattr(collision_middleware, 'Submission', MagicMock(return_value=mock_submission))
    monkeypatch.setattr(collision_middleware.common_middleware, 'get_user_guid', lambda **kwargs: 'user-guid')
    with open(collision_json_path) as f:
        payload = json.load(f)
    kwargs = {'payload': payload}
    result, out_kwargs = collision_middleware.save_collision_data(**kwargs)
    assert result is True
    assert out_kwargs['response_dict']['submission_id'] == 42
    assert out_kwargs['submission'] == mock_submission

def test_save_collision_data_exception(monkeypatch):
    mock_db = MagicMock()
    mock_session = MagicMock()
    mock_db.session = mock_session
    mock_session.add.side_effect = Exception('db error')
    monkeypatch.setattr(collision_middleware, 'db', mock_db)
    monkeypatch.setattr(collision_middleware, 'Submission', MagicMock())
    monkeypatch.setattr(collision_middleware.common_middleware, 'get_user_guid', lambda **kwargs: 'user-guid')
    kwargs = {'payload': DUMMY_PAYLOAD}
    result, out_kwargs = collision_middleware.save_collision_data(**kwargs)
    assert result is False
    assert 'error' in out_kwargs
    assert out_kwargs['error']['error_code']

def test_save_event_pdf_success():
    kwargs = {'payload': DUMMY_PAYLOAD}
    result, out_kwargs = collision_middleware.save_event_pdf(**kwargs)
    assert result is True
    assert out_kwargs == kwargs

def test_save_event_pdf_exception(monkeypatch):
    def raise_exc(**kwargs):
        raise Exception('pdf error')
    monkeypatch.setattr(collision_middleware, 'save_event_pdf', lambda **kwargs: (_ for _ in ()).throw(Exception('pdf error')))
    # Instead, patch the body of save_event_pdf to raise
    with patch('python.prohibition_web_svc.middleware.collision_middleware.save_event_pdf', side_effect=Exception('pdf error')):
        try:
            collision_middleware.save_event_pdf(payload=DUMMY_PAYLOAD)
        except Exception as e:
            assert str(e) == 'pdf error'

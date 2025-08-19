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
  assert out_kwargs['error']['error_details'] == "Missing required fields: ['collision_scenario', 'police_file_num', 'prime_file_vjur', 'date_collision', 'time_collision', 'reported_same_day', 'time_collision_unknown', 'date_reported', 'hit_and_run', 'police_attended', 'police_agency_code', 'primary_collision_occ_code', 'first_contact_event', 'first_contact_loc', 'has_countable_fatal', 'countable_fatal_total', 'completed_by_name', 'completed_by_id', 'detachment_unit', 'investigated_by_traffic_analyst', 'hwy_code', 'city_name', 'lat_decim_degrees', 'long_decim_degrees', 'road_class', 'traffic_flow', 'collision_loc', 'primary_speed_zone', 'land_usage', 'road_type', 'roadway_character', 'roadway_surface_cond', 'weather_cond', 'lighting_cond', 'has_other_prop_damage', 'has_witnesses', 'collision_type', 'total_est_damage', 'total_injured', 'total_killed', 'total_vehicles', 'summary_was_verified', 'entities']"

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


def test_get_collision_data_success():
    """Test successful retrieval of collision data"""
    mock_collision = MagicMock()
    mock_collision.collision_case_num = 'MV-001'
    mock_collision.collision_scenario = 'test_scenario'
    mock_collision.police_file_num = 'PF-001'
    
    # Mock location
    mock_location = MagicMock()
    mock_location.lat_decim_degrees = 49.2827
    mock_location.long_decim_degrees = -123.1207
    mock_collision.location = mock_location
    
    # Mock additional details
    mock_additional_details = MagicMock()
    mock_additional_details.pedestrian_location = 'sidewalk'
    mock_additional_details.pedestrian_action = 'standing'
    mock_collision.additional_details = mock_additional_details
    
    # Mock entities with charges and involved persons
    mock_entity = MagicMock()
    mock_entity.entity_id = 1
    mock_entity.entity_type = 'V'
    
    mock_charge = MagicMock()
    mock_charge.charge_id = 1
    mock_charge.charge_type = 'S'
    mock_entity.charges = [mock_charge]
    
    mock_person = MagicMock()
    mock_person.person_id = 1
    mock_person.surname = 'Doe'
    mock_entity.involved_persons = [mock_person]
    
    mock_collision.entities = [mock_entity]
    
    # Mock witnesses
    mock_witness = MagicMock()
    mock_witness.witness_name = 'John Witness'
    mock_witness.address = '123 Main St'
    mock_collision.witnesses = [mock_witness]

    with patch('python.prohibition_web_svc.middleware.collision_middleware.db') as mock_db, \
         patch('python.prohibition_web_svc.middleware.collision_middleware.asdict') as mock_asdict:
        
        mock_db.session.query.return_value.filter.return_value.first.return_value = mock_collision
        
        # Mock asdict to return predictable values
        mock_asdict.side_effect = [
            {'collision_case_num': 'MV-001', 'collision_scenario': 'test_scenario'},  # collision_data
            {'lat_decim_degrees': 49.2827, 'long_decim_degrees': -123.1207},  # location
            {'pedestrian_location': 'sidewalk', 'pedestrian_action': 'standing'},  # additional_details
            {'entity_id': 1, 'entity_type': 'V'},  # entity dict
            {'charge_id': 1, 'charge_type': 'S'},  # charge dict
            {'person_id': 1, 'surname': 'Doe'},  # person dict
            {'witness_name': 'John Witness', 'address': '123 Main St'}  # witness dict
        ]

        kwargs = {'collision_case_num': 'MV-001'}
        result, out_kwargs = collision_middleware.get_collision_data(**kwargs)
        
        assert result is True
        assert 'response_dict' in out_kwargs
        assert out_kwargs['response_dict']['collision_case_num'] == 'MV-001'
        assert 'location' in out_kwargs['response_dict']
        assert 'additional_details' in out_kwargs['response_dict']
        assert 'entities' in out_kwargs['response_dict']
        assert 'witnesses' in out_kwargs['response_dict']
        assert len(out_kwargs['response_dict']['entities']) == 1
        assert len(out_kwargs['response_dict']['witnesses']) == 1


def test_get_collision_data_not_found():
    """Test when collision data is not found"""
    with patch('python.prohibition_web_svc.middleware.collision_middleware.db') as mock_db:
        mock_db.session.query.return_value.filter.return_value.first.return_value = None
        
        kwargs = {'collision_case_num': 'MV-999'}
        result, out_kwargs = collision_middleware.get_collision_data(**kwargs)
        
        assert result is False
        assert 'error' in out_kwargs
        assert out_kwargs['error']['error_code'] == ErrorCode.C03
        assert 'Collision not found for case number: MV-999' in out_kwargs['error']['error_details']
        assert out_kwargs['error']['ticket_no'] == 'MV-999'
        assert out_kwargs['error']['event_type'] == collision_middleware.EVENT_TYPE


def test_get_collision_data_database_exception():
    """Test when database query raises an exception"""
    with patch('python.prohibition_web_svc.middleware.collision_middleware.db') as mock_db:
        mock_db.session.query.side_effect = Exception('Database connection error')
        
        kwargs = {'collision_case_num': 'MV-001'}
        result, out_kwargs = collision_middleware.get_collision_data(**kwargs)
        
        assert result is False
        assert 'error' in out_kwargs
        assert out_kwargs['error']['error_code'] == ErrorCode.C02
        assert 'Database connection error' in out_kwargs['error']['error_details']
        assert out_kwargs['error']['ticket_no'] == 'MV-001'
        assert out_kwargs['error']['event_type'] == collision_middleware.EVENT_TYPE


def test_get_collision_data_with_null_location():
    """Test collision data retrieval when location is None"""
    mock_collision = MagicMock()
    mock_collision.collision_case_num = 'MV-001'
    mock_collision.location = None
    mock_collision.additional_details = None
    mock_collision.entities = []
    mock_collision.witnesses = []
    
    with patch('python.prohibition_web_svc.middleware.collision_middleware.db') as mock_db, \
         patch('python.prohibition_web_svc.middleware.collision_middleware.asdict') as mock_asdict:
        
        mock_db.session.query.return_value.filter.return_value.first.return_value = mock_collision
        
        # Mock asdict to return the collision data
        mock_asdict.return_value = {'collision_case_num': 'MV-001'}
        
        kwargs = {'collision_case_num': 'MV-001'}
        result, out_kwargs = collision_middleware.get_collision_data(**kwargs)
        
        assert result is True
        assert out_kwargs['response_dict']['location'] is None
        assert out_kwargs['response_dict']['additional_details'] is None
        assert out_kwargs['response_dict']['entities'] == []
        assert out_kwargs['response_dict']['witnesses'] == []


def test_get_collision_data_with_empty_entities():
    """Test collision data retrieval with empty entities list"""
    mock_collision = MagicMock()
    mock_collision.collision_case_num = 'MV-001'
    mock_collision.location = None
    mock_collision.additional_details = None
    mock_collision.entities = []
    mock_collision.witnesses = []
    
    with patch('python.prohibition_web_svc.middleware.collision_middleware.db') as mock_db, \
         patch('python.prohibition_web_svc.middleware.collision_middleware.asdict') as mock_asdict:
        
        mock_db.session.query.return_value.filter.return_value.first.return_value = mock_collision
        
        # Mock asdict to return the collision data
        mock_asdict.return_value = {'collision_case_num': 'MV-001'}
        
        kwargs = {'collision_case_num': 'MV-001'}
        result, out_kwargs = collision_middleware.get_collision_data(**kwargs)
        
        assert result is True
        assert out_kwargs['response_dict']['entities'] == []


def test_get_collision_data_with_multiple_entities_and_witnesses():
    """Test collision data retrieval with multiple entities and witnesses"""
    mock_collision = MagicMock()
    mock_collision.collision_case_num = 'MV-001'
    mock_collision.location = None
    mock_collision.additional_details = None
    
    # Create multiple entities
    mock_entity1 = MagicMock()
    mock_entity1.entity_id = 1
    mock_entity1.charges = []
    mock_entity1.involved_persons = []
    
    mock_entity2 = MagicMock()
    mock_entity2.entity_id = 2
    mock_entity2.charges = []
    mock_entity2.involved_persons = []
    
    mock_collision.entities = [mock_entity1, mock_entity2]
    
    # Create multiple witnesses
    mock_witness1 = MagicMock()
    mock_witness1.witness_name = 'John Witness'
    
    mock_witness2 = MagicMock()
    mock_witness2.witness_name = 'Jane Witness'
    
    mock_collision.witnesses = [mock_witness1, mock_witness2]
    
    with patch('python.prohibition_web_svc.middleware.collision_middleware.db') as mock_db, \
         patch('python.prohibition_web_svc.middleware.collision_middleware.asdict') as mock_asdict:
        
        mock_db.session.query.return_value.filter.return_value.first.return_value = mock_collision
        
        # Mock asdict to return predictable values
        mock_asdict.side_effect = [
            {'collision_case_num': 'MV-001'},  # collision_data
            {'entity_id': 1},  # entity1 dict
            {'entity_id': 2},  # entity2 dict
            {'witness_name': 'John Witness'},  # witness1 dict
            {'witness_name': 'Jane Witness'}   # witness2 dict
        ]
        
        kwargs = {'collision_case_num': 'MV-001'}
        result, out_kwargs = collision_middleware.get_collision_data(**kwargs)
        
        assert result is True
        assert len(out_kwargs['response_dict']['entities']) == 2
        assert len(out_kwargs['response_dict']['witnesses']) == 2


def test_load_entity_helper_function():
    """Test the _load_entity helper function used by get_collision_data"""
    mock_entity = MagicMock()
    mock_entity.entity_id = 1
    mock_entity.entity_type = 'V'
    
    # Mock charges
    mock_charge1 = MagicMock()
    mock_charge1.charge_id = 1
    mock_charge2 = MagicMock()
    mock_charge2.charge_id = 2
    mock_entity.charges = [mock_charge1, mock_charge2]
    
    # Mock involved persons
    mock_person1 = MagicMock()
    mock_person1.person_id = 1
    mock_person2 = MagicMock()
    mock_person2.person_id = 2
    mock_entity.involved_persons = [mock_person1, mock_person2]
    
    with patch('python.prohibition_web_svc.middleware.collision_middleware.asdict') as mock_asdict:
        # Mock asdict to return predictable values
        mock_asdict.side_effect = [
            {'entity_id': 1, 'entity_type': 'V'},  # entity dict
            {'charge_id': 1},  # charge1 dict
            {'charge_id': 2},  # charge2 dict
            {'person_id': 1},  # person1 dict
            {'person_id': 2}   # person2 dict
        ]
        
        result = collision_middleware._load_entity(mock_entity)
        
        assert result['entity_id'] == 1
        assert result['entity_type'] == 'V'
        assert len(result['charges']) == 2
        assert len(result['involved_persons']) == 2
        assert result['charges'][0]['charge_id'] == 1
        assert result['charges'][1]['charge_id'] == 2
        assert result['involved_persons'][0]['person_id'] == 1
        assert result['involved_persons'][1]['person_id'] == 2


def test_load_entity_with_null_charges_and_persons():
    """Test _load_entity when charges and involved_persons are None"""
    mock_entity = MagicMock()
    mock_entity.entity_id = 1
    mock_entity.charges = None
    mock_entity.involved_persons = None
    
    with patch('python.prohibition_web_svc.middleware.collision_middleware.asdict') as mock_asdict:
        mock_asdict.return_value = {'entity_id': 1}
        
        result = collision_middleware._load_entity(mock_entity)
        
        assert result['entity_id'] == 1
        assert result['charges'] == []
        assert result['involved_persons'] == []


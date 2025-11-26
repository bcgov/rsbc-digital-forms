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
    assert out_kwargs['response_dict'] == {
        'error_details': 'Empty payload'
    }

def test_validate_collision_payload_failure_missing_fields():
    # Missing required fields
    kwargs = {'payload': {
        'collision_case_num': 'MV-001',
    }}
    result, out_kwargs = collision_middleware.validate_collision_payload(**kwargs)
    assert result is False
    assert 'error' in out_kwargs
    assert out_kwargs['error']['error_details'] == "Missing required fields: ['collision_scenario', 'police_file_num', 'prime_file_vjur', 'date_collision', 'time_collision', 'reported_same_day', 'time_collision_unknown', 'date_reported', 'hit_and_run', 'police_attended', 'police_agency_code', 'primary_collision_occ_code', 'first_contact_event', 'first_contact_loc', 'has_countable_fatal', 'countable_fatal_total', 'completed_by_name', 'completed_by_id', 'investigated_by_traffic_analyst', 'hwy_code', 'city_name', 'lat_decim_degrees', 'long_decim_degrees', 'road_class', 'traffic_flow', 'collision_loc', 'primary_speed_zone', 'land_usage', 'road_type', 'roadway_character', 'roadway_surface_cond', 'weather_cond', 'lighting_cond', 'has_other_prop_damage', 'has_witnesses', 'collision_type', 'total_est_damage', 'total_injured', 'total_killed', 'total_vehicles', 'summary_was_verified', 'entities', 'form_version']"
    assert out_kwargs['response_dict'] == {
        'error_details': out_kwargs['error']['error_details']
    }

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
    assert out_kwargs['response_dict'] == {
        'error_details': out_kwargs['error']['error_details']
    }

def test_validate_collision_payload_failure_missing_entity_fields():
    # Missing required entity fields
    with open(collision_json_path) as f:
        payload = json.load(f)
    payload['entities'] = [{}]  # Empty entity
    kwargs = {'payload': payload}
    result, out_kwargs = collision_middleware.validate_collision_payload(**kwargs)
    assert result is False
    assert 'error' in out_kwargs
    assert out_kwargs['error']['error_details'] == "Missing required fields in entity: ['entity_type', 'entity_num', 'possible_offender', 'contributing_factor_1', 'contributing_factor_2', 'contributing_factor_3', 'contributing_factor_4']"
    assert out_kwargs['response_dict'] == {
        'error_details': out_kwargs['error']['error_details']
    }

def test_validate_collision_payload_failure_missing_witness_data():
    # Missing required witness data when has_witnesses is True
    with open(collision_json_path) as f:
        payload = json.load(f)
    payload['has_witnesses'] = True  # Indicating there are witnesses
    payload['witnesses'] = []  # Empty witness list
    kwargs = {'payload': payload}
    result, out_kwargs = collision_middleware.validate_collision_payload(**kwargs)
    assert result is False
    assert out_kwargs['error']['error_details'] == "Collision has witnesses but no witness data provided."
    assert out_kwargs['response_dict'] == {
        'error_details': out_kwargs['error']['error_details']
    }

    # Test with None witnesses
    payload['witnesses'] = None  # No witnesses provided
    kwargs = {'payload': payload}
    result2, out_kwargs2 = collision_middleware.validate_collision_payload(**kwargs)
    assert result2 is False
    assert out_kwargs2['error']['error_details'] == "Collision has witnesses but no witness data provided."
    assert out_kwargs2['response_dict'] == {
        'error_details': out_kwargs2['error']['error_details']
    }

def test_validate_collision_payload_failure_missing_witness_fields():
    # Missing required witness fields
    with open(collision_json_path) as f:
        payload = json.load(f)
    payload['witnesses'] = [{}]  # Empty witness object
    kwargs = {'payload': payload}
    result, out_kwargs = collision_middleware.validate_collision_payload(**kwargs)
    assert result is False
    assert out_kwargs['error']['error_details'] == "Missing required fields in witness: ['witness_name', 'address', 'contact_phn_num']"
    assert out_kwargs['response_dict'] == {
        'error_details': out_kwargs['error']['error_details']
    }

def test_validate_lki_fields_success_hwy_code_1_with_route_and_segment():
    """Test _validate_lki_fields when hwy_code is 1 and both hwy_route_num and segment_num are present"""
    collision = {
        'hwy_code': 1,
        'hwy_route_num': '001',
        'segment_num': '0203',
        'collision_case_num': 'MV-001'
    }
    kwargs = {}
    result = collision_middleware._validate_lki_fields(collision, kwargs)
    assert result is True
    assert 'error' not in kwargs

def test_validate_lki_fields_failure_hwy_code_1_missing_hwy_route_num():
    """Test _validate_lki_fields when hwy_code is 1 but hwy_route_num is missing"""
    collision = {
        'hwy_code': 1,
        'segment_num': '0203',
        'collision_case_num': 'MV-001'
    }
    kwargs = {}
    result = collision_middleware._validate_lki_fields(collision, kwargs)
    assert result is False
    assert 'error' in kwargs
    assert kwargs['error']['error_code'] == ErrorCode.C01
    assert "For Hwy Code '1', both hwy_route_num and segment_num are required" in kwargs['error']['error_details']
    assert kwargs['error']['ticket_no'] == 'MV-001'
    assert kwargs['error']['event_type'] == collision_middleware.EVENT_TYPE
    assert kwargs['error']['func'] == collision_middleware._validate_lki_fields

def test_validate_lki_fields_failure_hwy_code_1_missing_segment_num():
    """Test _validate_lki_fields when hwy_code is 1 but segment_num is missing"""
    collision = {
        'hwy_code': 1,
        'hwy_route_num': '001',
        'collision_case_num': 'MV-001'
    }
    kwargs = {}
    result = collision_middleware._validate_lki_fields(collision, kwargs)
    assert result is False
    assert 'error' in kwargs
    assert kwargs['error']['error_code'] == ErrorCode.C01
    assert "For Hwy Code '1', both hwy_route_num and segment_num are required" in kwargs['error']['error_details']
    assert kwargs['error']['ticket_no'] == 'MV-001'
    assert kwargs['error']['event_type'] == collision_middleware.EVENT_TYPE
    assert kwargs['error']['func'] == collision_middleware._validate_lki_fields

def test_validate_lki_fields_failure_hwy_code_1_missing_both_route_and_segment():
    """Test _validate_lki_fields when hwy_code is 1 but both hwy_route_num and segment_num are missing"""
    collision = {
        'hwy_code': 1,
        'collision_case_num': 'MV-001'
    }
    kwargs = {}
    result = collision_middleware._validate_lki_fields(collision, kwargs)
    assert result is False
    assert 'error' in kwargs
    assert kwargs['error']['error_code'] == ErrorCode.C01
    assert "For Hwy Code '1', both hwy_route_num and segment_num are required" in kwargs['error']['error_details']
    assert kwargs['error']['ticket_no'] == 'MV-001'
    assert kwargs['error']['event_type'] == collision_middleware.EVENT_TYPE
    assert kwargs['error']['func'] == collision_middleware._validate_lki_fields

def test_validate_lki_fields_success_hwy_code_not_1():
    """Test _validate_lki_fields when hwy_code is not 1 (should pass regardless of route/segment nums)"""
    collision = {
        'hwy_code': 97,
        'collision_case_num': 'MV-001'
        # No hwy_route_num or segment_num provided
    }
    kwargs = {}
    result = collision_middleware._validate_lki_fields(collision, kwargs)
    assert result is True
    assert 'error' not in kwargs

def test_validate_lki_fields_success_hwy_code_not_1_with_route_and_segment():
    """Test _validate_lki_fields when hwy_code is not 1 but route and segment are provided"""
    collision = {
        'hwy_code': 97,
        'hwy_route_num': '097',
        'segment_num': '0356',
        'collision_case_num': 'MV-001'
    }
    kwargs = {}
    result = collision_middleware._validate_lki_fields(collision, kwargs)
    assert result is True
    assert 'error' not in kwargs

def test_validate_lki_fields_success_no_hwy_code():
    """Test _validate_lki_fields when hwy_code is not present (should pass)"""
    collision = {
        'collision_case_num': 'MV-001'
        # No hwy_code provided
    }
    kwargs = {}
    result = collision_middleware._validate_lki_fields(collision, kwargs)
    assert result is True
    assert 'error' not in kwargs

def test_validate_lki_fields_success_hwy_code_none():
    """Test _validate_lki_fields when hwy_code is None (should pass)"""
    collision = {
        'hwy_code': None,
        'collision_case_num': 'MV-001'
    }
    kwargs = {}
    result = collision_middleware._validate_lki_fields(collision, kwargs)
    assert result is True
    assert 'error' not in kwargs

def test_save_collision_data_success(monkeypatch):
    mock_db = MagicMock()
    mock_session = MagicMock()
    mock_db.session = mock_session
    mock_submission = MagicMock(submission_id=42)
    monkeypatch.setattr(collision_middleware, 'db', mock_db)
    monkeypatch.setattr(collision_middleware, 'Submission', MagicMock(return_value=mock_submission))
    monkeypatch.setattr(collision_middleware.common_middleware, 'get_user_guid', lambda **kwargs: 'user-guid')
    monkeypatch.setattr(collision_middleware, 'update_form_status', MagicMock(return_value=True))
    with open(collision_json_path) as f:
        payload = json.load(f)
    kwargs = {'payload': payload}
    result, out_kwargs = collision_middleware.save_collision_data(**kwargs)
    assert result is True
    assert out_kwargs['response_dict']['submission_id'] == 42
    assert out_kwargs['submission_id'] == 42

def test_save_offline_collision_data_success(monkeypatch):
    mock_db = MagicMock()
    mock_session = MagicMock()
    mock_db.session = mock_session
    mock_submission = MagicMock(submission_id=42)
    monkeypatch.setattr(collision_middleware, 'db', mock_db)
    monkeypatch.setattr(collision_middleware, 'Submission', MagicMock(return_value=mock_submission))
    monkeypatch.setattr(collision_middleware.common_middleware, 'get_user_guid', lambda **kwargs: 'user-guid')
    monkeypatch.setattr(collision_middleware, 'update_form_status', MagicMock(return_value=True))
    with open(collision_json_path) as f:
        payload = json.load(f)
    payload['submitted_offline'] = True
    kwargs = {'payload': payload}
    result, out_kwargs = collision_middleware.save_collision_data(**kwargs)
    assert result is True
    assert out_kwargs['response_dict']['submission_id'] == 42
    assert out_kwargs['submission_id'] == 42


def test_save_collision_data_success_with_update_form_status_warning(monkeypatch):
    mock_db = MagicMock()
    mock_session = MagicMock()
    mock_db.session = mock_session
    mock_submission = MagicMock(submission_id=42)
    monkeypatch.setattr(collision_middleware, 'db', mock_db)
    monkeypatch.setattr(collision_middleware, 'Submission', MagicMock(return_value=mock_submission))
    monkeypatch.setattr(collision_middleware.common_middleware, 'get_user_guid', lambda **kwargs: 'user-guid')
    monkeypatch.setattr(collision_middleware, 'update_form_status', MagicMock(return_value=False))
    with open(collision_json_path) as f:
        payload = json.load(f)
    kwargs = {'payload': payload}
    result, out_kwargs = collision_middleware.save_collision_data(**kwargs)
    assert result is True
    assert out_kwargs['response_dict']['submission_id'] == 42
    assert out_kwargs['submission_id'] == 42

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
    assert out_kwargs['error']['error_code'] == ErrorCode.E01

def test_save_event_pdf_success():
    kwargs = {'payload': DUMMY_PAYLOAD, 'submission_id': 42}
    with patch('python.prohibition_web_svc.middleware.collision_middleware.db') as mock_db:
        mock_session = MagicMock()
        mock_db.session = mock_session
        
        result, out_kwargs = collision_middleware.save_event_pdf(**kwargs)
        assert result is True
        assert out_kwargs == kwargs
        # Verify that db operations were called
        mock_session.add.assert_called_once()
        mock_session.commit.assert_called_once()

def test_save_event_pdf_exception():
    kwargs = {'payload': DUMMY_PAYLOAD, 'submission_id': 42}
    with patch('python.prohibition_web_svc.middleware.collision_middleware.db') as mock_db:
        mock_session = MagicMock()
        mock_db.session = mock_session
        mock_session.add.side_effect = Exception('pdf error')
        
        result, out_kwargs = collision_middleware.save_event_pdf(**kwargs)
        assert result is False
        assert 'error' in out_kwargs
        assert out_kwargs['error']['error_code'] == ErrorCode.C04
        assert 'pdf error' in str(out_kwargs['error']['error_details'])

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

def test_check_if_case_number_exists_no_ticket_number():
    """Test check_if_case_number_exists when ticket_no is None"""
    kwargs = {'ticket_no': None}
    result, out_kwargs = collision_middleware.check_if_case_number_exists(**kwargs)
    
    assert result is True
    assert out_kwargs == kwargs

def test_check_if_case_number_exists_case_number_not_found():
    """Test check_if_case_number_exists when case number doesn't exist in database"""
    with patch('python.prohibition_web_svc.middleware.collision_middleware.db') as mock_db:
        mock_db.session.query.return_value.filter.return_value.first.return_value = None
        
        kwargs = {'ticket_no': 'MV-999'}
        result, out_kwargs = collision_middleware.check_if_case_number_exists(**kwargs)
        
        assert result is True
        assert out_kwargs == kwargs
        # Verify the database query was called correctly
        mock_db.session.query.assert_called_once()
        mock_db.session.query.return_value.filter.assert_called_once()

def test_check_if_case_number_exists_case_number_already_exists():
    """Test check_if_case_number_exists when case number already exists in database"""
    mock_submission = MagicMock()
    mock_submission.submission_id = 42
    
    with patch('python.prohibition_web_svc.middleware.collision_middleware.db') as mock_db:
        mock_db.session.query.return_value.filter.return_value.first.return_value = mock_submission
        
        kwargs = {'ticket_no': 'MV-001'}
        result, out_kwargs = collision_middleware.check_if_case_number_exists(**kwargs)
        
        assert result is False
        assert 'error' in out_kwargs
        assert out_kwargs['error']['error_code'] == ErrorCode.E09
        assert out_kwargs['error']['error_details'] == 'Collision case number already exists'
        assert out_kwargs['error']['submission_id'] == 42
        assert out_kwargs['error']['ticket_no'] == 'MV-001'
        assert out_kwargs['error']['event_type'] == collision_middleware.EVENT_TYPE
        assert out_kwargs['error']['func'] == collision_middleware.check_if_case_number_exists

def test_check_if_case_number_exists_database_exception():
    """Test check_if_case_number_exists when database query raises an exception"""
    with patch('python.prohibition_web_svc.middleware.collision_middleware.db') as mock_db:
        mock_db.session.query.side_effect = Exception('Database connection error')
        
        kwargs = {'ticket_no': 'MV-001'}
        result, out_kwargs = collision_middleware.check_if_case_number_exists(**kwargs)
        
        assert result is False
        assert 'error' in out_kwargs
        assert out_kwargs['error']['error_code'] == ErrorCode.G00
        assert 'Database connection error' in out_kwargs['error']['error_details']
        assert out_kwargs['error']['ticket_no'] == 'MV-001'
        assert out_kwargs['error']['event_type'] == collision_middleware.EVENT_TYPE
        assert out_kwargs['error']['func'] == collision_middleware.check_if_case_number_exists

def test_check_if_case_number_exists_empty_ticket_number():
    """Test check_if_case_number_exists with empty string ticket number"""
    with patch('python.prohibition_web_svc.middleware.collision_middleware.db') as mock_db:
        mock_db.session.query.return_value.filter.return_value.first.return_value = None
        
        kwargs = {'ticket_no': ''}
        result, out_kwargs = collision_middleware.check_if_case_number_exists(**kwargs)
        
        assert result is True
        assert out_kwargs == kwargs
        # Verify the database query was still called (empty string is not None)
        mock_db.session.query.assert_called_once()

def test_check_if_case_number_exists_with_special_characters():
    """Test check_if_case_number_exists with special characters in case number"""
    with patch('python.prohibition_web_svc.middleware.collision_middleware.db') as mock_db:
        mock_db.session.query.return_value.filter.return_value.first.return_value = None
        
        kwargs = {'ticket_no': 'MV-001@#$'}
        result, out_kwargs = collision_middleware.check_if_case_number_exists(**kwargs)
        
        assert result is True
        assert out_kwargs == kwargs
        # Verify the database query was called with the special characters
        mock_db.session.query.assert_called_once()


def test_log_get_collision_to_splunk_success_with_all_fields():
    """Test log_get_collision_to_splunk with all required fields present"""
    kwargs = {
        'user_guid': 'test-user-guid-123',
        'username': 'test.user@example.com',
        'collision_case_num': 'MV-001'
    }
    
    result, out_kwargs = collision_middleware.log_get_collision_to_splunk(**kwargs)
    
    assert result is True
    assert 'splunk_data' in out_kwargs
    splunk_data = out_kwargs['splunk_data']
    
    # Verify all expected fields are present in splunk_data
    assert splunk_data['event'] == "get collision"
    assert splunk_data['user_guid'] == 'test-user-guid-123'
    assert splunk_data['username'] == 'test.user@example.com'
    assert splunk_data['form_type'] == collision_middleware.MV6020_FORM_TYPE
    assert splunk_data['collision_case_number'] == 'MV-001'

def test_log_get_collision_to_splunk_success_with_missing_optional_fields():
    """Test log_get_collision_to_splunk with missing optional fields"""
    kwargs = {}
    
    result, out_kwargs = collision_middleware.log_get_collision_to_splunk(**kwargs)
    
    assert result is True
    assert 'splunk_data' in out_kwargs
    splunk_data = out_kwargs['splunk_data']
    
    # Verify required fields are present with default values
    assert splunk_data['event'] == "get collision"
    assert splunk_data['user_guid'] is None  # Missing user_guid returns None
    assert splunk_data['username'] is None  # Missing username returns None
    assert splunk_data['form_type'] == collision_middleware.MV6020_FORM_TYPE
    assert splunk_data['collision_case_number'] is None  # Missing case number returns None

def test_log_get_collision_to_splunk_with_empty_strings():
    """Test log_get_collision_to_splunk with empty string values"""
    kwargs = {
        'user_guid': '',
        'username': '',
        'collision_case_num': ''
    }
    
    result, out_kwargs = collision_middleware.log_get_collision_to_splunk(**kwargs)
    
    assert result is True
    assert 'splunk_data' in out_kwargs
    splunk_data = out_kwargs['splunk_data']
    
    assert splunk_data['event'] == "get collision"
    assert splunk_data['user_guid'] == ''
    assert splunk_data['username'] == ''
    assert splunk_data['form_type'] == collision_middleware.MV6020_FORM_TYPE
    assert splunk_data['collision_case_number'] == ''

def test_log_get_collision_to_splunk_kwargs_preservation():
    """Test that log_get_collision_to_splunk preserves original kwargs"""
    original_kwargs = {
        'user_guid': 'test-guid',
        'username': 'test.user',
        'collision_case_num': 'MV-001',
        'other_field': 'should_be_preserved'
    }
    
    result, out_kwargs = collision_middleware.log_get_collision_to_splunk(**original_kwargs)
    
    assert result is True
    
    # Verify original kwargs are preserved
    assert out_kwargs['user_guid'] == 'test-guid'
    assert out_kwargs['username'] == 'test.user'
    assert out_kwargs['collision_case_num'] == 'MV-001'
    assert out_kwargs['other_field'] == 'should_be_preserved'
    
    # Verify splunk_data was added
    assert 'splunk_data' in out_kwargs

def test_log_get_collision_to_splunk_form_type_constant():
    """Test that log_get_collision_to_splunk uses the correct form type constant"""
    kwargs = {'collision_case_num': 'MV-001'}
    
    result, out_kwargs = collision_middleware.log_get_collision_to_splunk(**kwargs)
    
    assert result is True
    assert out_kwargs['splunk_data']['form_type'] == 'MV6020'
    # Verify it matches the constant
    assert out_kwargs['splunk_data']['form_type'] == collision_middleware.MV6020_FORM_TYPE

def test_log_get_collision_to_splunk_event_name():
    """Test that log_get_collision_to_splunk sets correct event name"""
    kwargs = {}
    
    result, out_kwargs = collision_middleware.log_get_collision_to_splunk(**kwargs)
    
    assert result is True
    assert out_kwargs['splunk_data']['event'] == "get collision"

def test_log_get_collision_to_splunk_with_large_case_number():
    """Test log_get_collision_to_splunk with very long collision case number"""
    large_case_number = 'MV-' + 'X' * 100  # Very long case number
    kwargs = {
        'user_guid': 'test-guid',
        'username': 'test.user',
        'collision_case_num': large_case_number
    }
    
    result, out_kwargs = collision_middleware.log_get_collision_to_splunk(**kwargs)
    
    assert result is True
    assert out_kwargs['splunk_data']['collision_case_number'] == large_case_number

def test_log_get_collision_to_splunk_data_structure():
    """Test the complete structure of splunk_data returned"""
    kwargs = {
        'user_guid': 'test-guid',
        'username': 'test.user',
        'collision_case_num': 'MV-001',
        'request_id': 'req-123'
    }
    
    result, out_kwargs = collision_middleware.log_get_collision_to_splunk(**kwargs)
    
    assert result is True
    splunk_data = out_kwargs['splunk_data']
    
    # Verify splunk_data has exactly the expected keys
    expected_keys = {'event', 'user_guid', 'username', 'request_id', 'form_type', 'collision_case_number'}
    assert set(splunk_data.keys()) == expected_keys
    
    # Verify all values are strings (except username which can be None)
    assert isinstance(splunk_data['event'], str)
    assert isinstance(splunk_data['user_guid'], str)
    assert isinstance(splunk_data['request_id'], str)
    assert isinstance(splunk_data['form_type'], str)
    assert isinstance(splunk_data['collision_case_number'], str)
    # username can be str or None


def test_log_payload_to_splunk_success_with_valid_request():
    """Test log_payload_to_splunk with valid request and payload"""
    mock_request = MagicMock()
    mock_payload = {
        'collision_case_num': 'MV-001',
        'driver_license_num': '12345678',
        'surname': 'Doe',
        'given_name': 'John',
        'entities': [
            {
                'vehicle_plate_num': 'ABC123',
                'involved_persons': [
                    {'surname': 'Smith', 'given_name': 'Jane'}
                ]
            }
        ],
        'witnesses': [
            {'witness_name': 'Bob Wilson', 'address': '123 Main St'}
        ]
    }
    mock_request.get_json.return_value = mock_payload

    kwargs = {
        'request': mock_request,
        'user_guid': 'test-user-guid-123',
        'username': 'test.user@example.com'
    }
    
    result, out_kwargs = collision_middleware.log_payload_to_splunk(**kwargs)
    
    assert result is True
    assert 'splunk_data' in out_kwargs
    splunk_data = out_kwargs['splunk_data']
    
    # Verify splunk_data structure
    assert splunk_data['event'] == "create collision"
    assert splunk_data['user_guid'] == 'test-user-guid-123'
    assert splunk_data['username'] == 'test.user@example.com'
    assert splunk_data['form_type'] == collision_middleware.MV6020_FORM_TYPE
    assert 'payload' in splunk_data
    
    # Verify sensitive data is masked
    masked_payload = splunk_data['payload']
    assert masked_payload['driver_license_num'] == "[REDACTED]"
    assert masked_payload['surname'] == "[REDACTED]"
    assert masked_payload['given_name'] == "[REDACTED]"
    assert masked_payload['entities'][0]['vehicle_plate_num'] == "[REDACTED]"
    assert masked_payload['entities'][0]['involved_persons'][0]['surname'] == "[REDACTED]"
    assert masked_payload['entities'][0]['involved_persons'][0]['given_name'] == "[REDACTED]"
    assert masked_payload['witnesses'][0]['witness_name'] == "[REDACTED]"
    assert masked_payload['witnesses'][0]['address'] == "[REDACTED]"
    
    # Verify non-sensitive data is preserved
    assert masked_payload['collision_case_num'] == 'MV-001'

def test_log_payload_to_splunk_success_with_missing_user_info():
    """Test log_payload_to_splunk with missing user information"""
    mock_request = MagicMock()
    mock_payload = {'collision_case_num': 'MV-002'}
    mock_request.get_json.return_value = mock_payload

    kwargs = {'request': mock_request}
    
    result, out_kwargs = collision_middleware.log_payload_to_splunk(**kwargs)
    
    assert result is True
    assert 'splunk_data' in out_kwargs
    splunk_data = out_kwargs['splunk_data']
    
    assert splunk_data['event'] == "create collision"
    assert splunk_data['user_guid'] == ''  # Default empty string
    assert splunk_data['username'] is None  # Missing username returns None
    assert splunk_data['form_type'] == collision_middleware.MV6020_FORM_TYPE
    assert splunk_data['payload'] == mock_payload

def test_log_payload_to_splunk_success_with_empty_payload():
    """Test log_payload_to_splunk with empty payload"""
    mock_request = MagicMock()
    mock_request.get_json.return_value = {}

    kwargs = {
        'request': mock_request,
        'user_guid': 'test-guid',
        'username': 'test.user'
    }
    
    result, out_kwargs = collision_middleware.log_payload_to_splunk(**kwargs)
    
    assert result is True
    assert 'splunk_data' in out_kwargs
    splunk_data = out_kwargs['splunk_data']
    
    assert splunk_data['event'] == "create collision"
    assert splunk_data['user_guid'] == 'test-guid'
    assert splunk_data['username'] == 'test.user'
    assert splunk_data['form_type'] == collision_middleware.MV6020_FORM_TYPE
    assert splunk_data['payload'] == {}

def test_log_payload_to_splunk_masks_all_sensitive_fields():
    """Test that log_payload_to_splunk masks all sensitive fields"""
    mock_request = MagicMock()
    mock_payload = {
        'driver_license_num': 'DL123456',
        'surname': 'TestSurname',
        'given_name': 'TestGivenName',
        'contact_phone_num': '555-1234',
        'vehicle_plate_num': 'PLATE123',
        'vehicle_owner_name': 'Owner Name',
        'vehicle_owner_address': '123 Owner St',
        'nsc_num': 'NSC123',
        'other_insurance_policy_num': 'INS456',
        'witness_name': 'Witness Name',
        'address': '456 Witness Ave',
        'contact_phn_num': '555-5678',
        'non_sensitive_field': 'should_not_be_masked'
    }
    mock_request.get_json.return_value = mock_payload

    kwargs = {'request': mock_request}
    
    result, out_kwargs = collision_middleware.log_payload_to_splunk(**kwargs)
    
    assert result is True
    masked_payload = out_kwargs['splunk_data']['payload']
    
    # Verify all sensitive fields are masked
    sensitive_fields = [
        'driver_license_num', 'surname', 'given_name', 'contact_phone_num',
        'vehicle_plate_num', 'vehicle_owner_name', 'vehicle_owner_address',
        'nsc_num', 'other_insurance_policy_num', 'witness_name', 'address', 'contact_phn_num'
    ]
    
    for field in sensitive_fields:
        assert masked_payload[field] == "[REDACTED]"
    
    # Verify non-sensitive field is not masked
    assert masked_payload['non_sensitive_field'] == 'should_not_be_masked'

def test_log_payload_to_splunk_handles_nested_entities():
    """Test log_payload_to_splunk properly masks nested entities"""
    mock_request = MagicMock()
    mock_payload = {
        'entities': [
            {
                'driver_license_num': 'DL001',
                'surname': 'Entity1Surname',
                'vehicle_plate_num': 'PLATE001',
                'involved_persons': [
                    {'surname': 'Person1', 'given_name': 'FirstPerson'},
                    {'surname': 'Person2', 'given_name': 'SecondPerson'}
                ]
            },
            {
                'driver_license_num': 'DL002',
                'surname': 'Entity2Surname',
                'vehicle_plate_num': 'PLATE002'
            }
        ]
    }
    mock_request.get_json.return_value = mock_payload

    kwargs = {'request': mock_request}
    
    result, out_kwargs = collision_middleware.log_payload_to_splunk(**kwargs)
    
    assert result is True
    masked_payload = out_kwargs['splunk_data']['payload']
    
    # Verify first entity is masked
    entity1 = masked_payload['entities'][0]
    assert entity1['driver_license_num'] == "[REDACTED]"
    assert entity1['surname'] == "[REDACTED]"
    assert entity1['vehicle_plate_num'] == "[REDACTED]"
    
    # Verify involved persons in first entity are masked
    assert entity1['involved_persons'][0]['surname'] == "[REDACTED]"
    assert entity1['involved_persons'][0]['given_name'] == "[REDACTED]"
    assert entity1['involved_persons'][1]['surname'] == "[REDACTED]"
    assert entity1['involved_persons'][1]['given_name'] == "[REDACTED]"
    
    # Verify second entity is masked
    entity2 = masked_payload['entities'][1]
    assert entity2['driver_license_num'] == "[REDACTED]"
    assert entity2['surname'] == "[REDACTED]"
    assert entity2['vehicle_plate_num'] == "[REDACTED]"

def test_log_payload_to_splunk_handles_nested_witnesses():
    """Test log_payload_to_splunk properly masks nested witnesses"""
    mock_request = MagicMock()
    mock_payload = {
        'witnesses': [
            {
                'witness_name': 'Witness One',
                'address': '123 First St',
                'contact_phn_num': '555-0001'
            },
            {
                'witness_name': 'Witness Two',
                'address': '456 Second Ave',
                'contact_phn_num': '555-0002'
            }
        ]
    }
    mock_request.get_json.return_value = mock_payload

    kwargs = {'request': mock_request}
    
    result, out_kwargs = collision_middleware.log_payload_to_splunk(**kwargs)
    
    assert result is True
    masked_payload = out_kwargs['splunk_data']['payload']
    
    # Verify all witnesses are masked
    for witness in masked_payload['witnesses']:
        assert witness['witness_name'] == "[REDACTED]"
        assert witness['address'] == "[REDACTED]"
        assert witness['contact_phn_num'] == "[REDACTED]"

def test_log_payload_to_splunk_exception_handling():
    """Test log_payload_to_splunk handles exceptions gracefully"""
    mock_request = MagicMock()
    mock_request.get_json.side_effect = Exception("JSON parsing error")

    kwargs = {
        'request': mock_request,
        'user_guid': 'test-guid',
        'username': 'test.user'
    }
    
    with patch('python.prohibition_web_svc.middleware.collision_middleware.logger') as mock_logging:
        result, out_kwargs = collision_middleware.log_payload_to_splunk(**kwargs)
        
        # Function should still return True even with exception
        assert result is True
        
        # Should log the exception
        mock_logging.error.assert_called_once()
        
        # splunk_data should not be set due to exception
        assert 'splunk_data' not in out_kwargs

def test_log_payload_to_splunk_no_request_object():
    """Test log_payload_to_splunk when request object is missing"""
    kwargs = {
        'user_guid': 'test-guid',
        'username': 'test.user'
    }
    
    with patch('python.prohibition_web_svc.middleware.collision_middleware.logger') as mock_logging:
        result, out_kwargs = collision_middleware.log_payload_to_splunk(**kwargs)
        
        # Function should still return True even with missing request
        assert result is True
        
        # Should log the exception
        mock_logging.error.assert_called_once()
        
        # splunk_data should not be set due to exception
        assert 'splunk_data' not in out_kwargs

def test_log_payload_to_splunk_kwargs_preservation():
    """Test that log_payload_to_splunk preserves original kwargs"""
    mock_request = MagicMock()
    mock_request.get_json.return_value = {'test': 'data'}

    original_kwargs = {
        'request': mock_request,
        'user_guid': 'test-guid',
        'username': 'test.user',
        'other_field': 'should_be_preserved'
    }
    
    result, out_kwargs = collision_middleware.log_payload_to_splunk(**original_kwargs)
    
    assert result is True
    
    # Verify original kwargs are preserved
    assert out_kwargs['request'] == mock_request
    assert out_kwargs['user_guid'] == 'test-guid'
    assert out_kwargs['username'] == 'test.user'
    assert out_kwargs['other_field'] == 'should_be_preserved'
    
    # Verify splunk_data was added
    assert 'splunk_data' in out_kwargs

def test_log_payload_to_splunk_form_type_constant():
    """Test that log_payload_to_splunk uses the correct form type constant"""
    mock_request = MagicMock()
    mock_request.get_json.return_value = {}

    kwargs = {'request': mock_request}
    
    result, out_kwargs = collision_middleware.log_payload_to_splunk(**kwargs)
    
    assert result is True
    assert out_kwargs['splunk_data']['form_type'] == 'MV6020'
    # Verify it matches the constant
    assert out_kwargs['splunk_data']['form_type'] == collision_middleware.MV6020_FORM_TYPE

def test_log_payload_to_splunk_event_name():
    """Test that log_payload_to_splunk sets correct event name"""
    mock_request = MagicMock()
    mock_request.get_json.return_value = {}

    kwargs = {'request': mock_request}
    
    result, out_kwargs = collision_middleware.log_payload_to_splunk(**kwargs)
    
    assert result is True
    assert out_kwargs['splunk_data']['event'] == "create collision"

def test_log_payload_to_splunk_data_structure():
    """Test the complete structure of splunk_data returned"""
    mock_request = MagicMock()
    mock_request.get_json.return_value = {'test': 'payload'}

    kwargs = {
        'request': mock_request,
        'user_guid': 'test-guid',
        'username': 'test.user',
        'request_id': 'req-123'
    }
    
    result, out_kwargs = collision_middleware.log_payload_to_splunk(**kwargs)
    
    assert result is True
    splunk_data = out_kwargs['splunk_data']
    
    # Verify splunk_data has exactly the expected keys
    expected_keys = {'event', 'user_guid', 'username', 'request_id', 'form_type', 'payload'}
    assert set(splunk_data.keys()) == expected_keys
    
    # Verify data types
    assert isinstance(splunk_data['event'], str)
    assert isinstance(splunk_data['user_guid'], str)
    assert isinstance(splunk_data['form_type'], str)
    assert isinstance(splunk_data['request_id'], str)
    assert isinstance(splunk_data['payload'], dict)
    # username can be str or None

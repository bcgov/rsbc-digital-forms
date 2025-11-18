import json
import os
from python.prohibition_web_svc.mappers.collision_mapper import CollisionMapper
from python.common.models import TarCollision, TarLocation, TarAdditionalCollisionDetails, TarWitnessInfo, TarEntity, TarInvolvedPerson, TarCharges

def get_payload():
    test_dir = os.path.dirname(os.path.abspath(__file__))
    collision_json_path = os.path.join(test_dir, '..', 'tests-data', 'collision.json')
    with open(collision_json_path) as f:
        payload = json.load(f)
    return payload

def test_map_to_tar_collision():
    payload = get_payload()
    result = CollisionMapper.map_to_tar_collision(payload)
    assert isinstance(result, TarCollision)
    assert result.collision_case_num == 'MV-001'
    assert result.location is not None
    assert result.additional_details is not None
    assert isinstance(result.entities[0], TarEntity)
    assert isinstance(result.entities[0].involved_persons[0], TarInvolvedPerson)
    assert isinstance(result.entities[0].charges[0], TarCharges)
    assert isinstance(result.witnesses[0], TarWitnessInfo)

def test_map_to_tar_location():
    payload = get_payload()
    result = CollisionMapper.map_to_tar_location(payload)
    assert isinstance(result, TarLocation)
    assert result.collision_case_num == 'MV-001'
    assert result.hwy_code == 'HWY'
    assert result.city_name == 'City'
    assert result.lat_decim_degrees == 49.123456
    assert result.long_decim_degrees == -123.123456

def test_map_to_tar_additional_details():
    payload = get_payload()
    result = CollisionMapper.map_to_tar_additional_details(payload)
    assert isinstance(result, TarAdditionalCollisionDetails)
    assert result.has_other_prop_damage == 'Y'
    assert result.has_witnesses is True
    assert result.collision_type == '01'
    assert result.total_vehicles == 1

def test_map_to_tar_witnesses():
    payload = get_payload()
    result = CollisionMapper.map_to_tar_witnesses(payload)
    assert isinstance(result, list)
    assert isinstance(result[0], TarWitnessInfo)
    assert result[0].witness_name == 'John Doe'

def test_map_to_tar_entities():
    payload = get_payload()
    result = CollisionMapper.map_to_tar_entities(payload)
    assert isinstance(result, list)
    assert isinstance(result[0], TarEntity)
    assert result[0].entity_type == 'V'
    assert isinstance(result[0].involved_persons[0], TarInvolvedPerson)
    assert result[0].involved_persons[0].given_name == 'Alice'
    assert result[0].involved_persons[0].surname == 'Smith'
    assert isinstance(result[0].charges[0], TarCharges)
    assert result[0].charges[0].charge_type == 'B'

import json

import pytest
from flask import Flask, make_response

from python.prohibition_web_svc.blueprints import offline_submissions
from python.prohibition_web_svc.config import Config


@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.register_blueprint(offline_submissions.bp)
    return app


@pytest.fixture
def client(app):
    return app.test_client()


def test_create_offline_submission_success_and_middleware_chain(client, monkeypatch):
    auth_step = {'try': lambda **kwargs: (True, kwargs), 'fail': []}
    get_authorized_user = lambda: [auth_step]
    monkeypatch.setattr(
        offline_submissions,
        'get_authorized_keycloak_user',
        get_authorized_user,
    )
    captured = {}

    def mock_middle_logic(chain, **kwargs):
        captured['chain'] = chain
        captured['kwargs'] = kwargs
        captured['payload'] = kwargs['request'].get_json()
        return {'response': make_response({'offline_submission_id': 42}, 201)}

    monkeypatch.setattr(offline_submissions, 'middle_logic', mock_middle_logic)
    payload = {
        'localSubmissionId': 'local-123',
        'formId': 'VI123',
        'answers': [],
    }

    response = client.post(
        Config.URL_PREFIX + '/api/v1/offline_submission',
        data=json.dumps(payload),
        content_type='application/json',
    )

    assert response.status_code == 201
    assert response.get_json() == {'offline_submission_id': 42}
    assert captured['chain'][0] is auth_step
    assert [step['try'].__name__ for step in captured['chain'][1:]] == [
        'request_contains_a_payload',
        'set_local_submission_id',
        'check_if_offline_submission_exists',
        'create_offline_submission',
        'successful_create_response',
    ]
    assert captured['chain'][1]['fail'][0]['try'].__name__ == 'bad_request_response'
    assert captured['chain'][2]['fail'][0]['try'].__name__ == 'bad_request_response'
    assert (
        captured['chain'][3]['fail'][0]['try'].__name__
        == 'offline_submission_already_exists'
    )
    assert captured['chain'][4]['fail'][0]['try'].__name__ == 'record_event_error'
    assert captured['chain'][4]['fail'][1]['try'].__name__ == 'server_error_response'
    assert captured['kwargs']['required_permission'] == 'create_submissions'
    assert captured['payload'] == payload
    assert captured['kwargs']['config'] is Config


@pytest.mark.parametrize(
    ('status_code', 'body'),
    [
        (400, {'error': 'bad request'}),
        (202, {'message': 'offline submission already exists'}),
        (401, {'error': 'unauthorized'}),
        (500, {'error': 'server error'}),
    ],
)
def test_create_offline_submission_returns_middleware_response(
    client, monkeypatch, status_code, body
):
    monkeypatch.setattr(offline_submissions, 'get_authorized_keycloak_user', list)
    monkeypatch.setattr(
        offline_submissions,
        'middle_logic',
        lambda *args, **kwargs: {'response': make_response(body, status_code)},
    )

    response = client.post(
        Config.URL_PREFIX + '/api/v1/offline_submission',
        json={'localSubmissionId': 'local-123', 'answers': []},
    )

    assert response.status_code == status_code
    assert response.get_json() == body


def test_offline_submission_blueprint_route_registration(app):
    rule = next(
        rule for rule in app.url_map.iter_rules()
        if rule.endpoint == 'offline_submission.create_offline_submission'
    )

    assert rule.rule == Config.URL_PREFIX + '/api/v1/offline_submission'
    assert rule.methods == {'OPTIONS', 'POST'}

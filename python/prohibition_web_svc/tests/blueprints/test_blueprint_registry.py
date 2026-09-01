import sys
import types

import pytest
from flask import Flask

if "flask_caching" not in sys.modules:
    flask_caching = types.ModuleType("flask_caching")

    class Cache:
        def __init__(self, *args, **kwargs):
            pass

        def init_app(self, *args, **kwargs):
            return None

        def get(self, *args, **kwargs):
            return None

        def set(self, *args, **kwargs):
            return None

    flask_caching.Cache = Cache
    sys.modules["flask_caching"] = flask_caching

from python.prohibition_web_svc.blueprints import (
    admin_forms,
    admin_users,
    collision,
    detachments,
    email,
    events,
    files,
    forms,
    icbc,
    print as print_blueprint,
    static,
    submissions,
    users,
)


@pytest.mark.parametrize(
    ("module", "bp_name", "expected_rules"),
    [
        (admin_forms, "admin_forms", {"/api/v1/admin/forms", "/api/v1/admin/forms/<string:form_id>"}),
        (admin_users, "admin_users", {"/api/v1/admin/users", "/api/v1/admin/users/<string:username>"}),
        (collision, "collision", {"/api/v1/collision", "/api/v1/collision/<collision_case_num>"}),
        (detachments, "detachments", {"/api/v1/detachments", "/api/v1/detachment-change-request"}),
        (email, "email", {"/api/v1/email"}),
        (events, "event", {"/api/v1/event", "/api/v1/event/irp/<int:event_id>"}),
        (files, "files", {"/api/v1/files", "/api/v1/files/<path:filename>", "/api/v1/files/url/<path:filename>"}),
        (forms, "forms", {"/api/v1/forms", "/api/v1/forms/<string:form_type>/<string:form_id>", "/api/v1/forms/statistics"}),
        (icbc, "icbc", {"/api/v1/icbc/drivers/<string:dl_number>", "/api/v1/icbc/vehicles/<string:plate_number>"}),
        (print_blueprint, "print", {"/api/v1/print"}),
        (static, "static", {"/api/v1/static/<string:resource>", "/api/v1/static/<string:resource>/<string:static_id>", "/api/v1/ping"}),
        (submissions, "submission", {"/api/v1/submission/event/status"}),
        (users, "users", {"/api/v1/users", "/api/v1/users/<string:user_guid>", "/api/v1/users/<string:user_guid>/detachment", "/api/v1/users/<string:user_guid>/update-last-active"}),
    ],
)
def test_blueprint_registration_and_route_contract(module, bp_name, expected_rules):
    app = Flask(__name__)
    app.config["TESTING"] = True
    app.register_blueprint(module.bp)

    assert bp_name in app.blueprints
    blueprint = app.blueprints[bp_name]
    assert blueprint.name == bp_name
    assert blueprint.url_prefix == "/api/v1"

    registered_rules = {
        rule.rule
        for rule in app.url_map.iter_rules()
        if rule.endpoint.startswith(f"{bp_name}.")
    }
    assert expected_rules.issubset(registered_rules)


def test_application_registers_primary_blueprints():
    app = Flask(__name__)
    app.config["TESTING"] = True

    for module in (
        admin_forms,
        admin_users,
        collision,
        detachments,
        email,
        events,
        files,
        forms,
        icbc,
        print_blueprint,
        static,
        submissions,
        users,
    ):
        app.register_blueprint(module.bp)

    assert {
        "admin_forms",
        "admin_users",
        "collision",
        "detachments",
        "email",
        "event",
        "files",
        "forms",
        "icbc",
        "print",
        "static",
        "submission",
        "users",
    }.issubset(set(app.blueprints.keys()))

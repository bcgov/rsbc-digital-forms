import os


class Config():
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'DEBUG').upper()
    ENVIRONMENT = os.getenv('ENVIRONMENT', 'dev').upper()

    # Postgres settings
    DB_HOST = os.environ.get('DB_HOST', 'db')
    DB_USER = os.environ.get('DB_USER', 'testuser')
    DB_PASS = os.environ.get('DB_PASS', 'pass')
    DB_PORT = os.environ.get('DB_PORT', 5432)
    DB_NAME_FF_API = os.environ.get('DB_NAME_FF_API', 'formsflow_api')

    # Keycloak settings
    KEYCLOAK_AUTH_URL = os.environ.get('KEYCLOAK_AUTH_URL', 'http://keycloak:8080/auth/')
    KEYCLOAK_REALM = os.environ.get('KEYCLOAK_REALM', 'master')
    KEYCLOAK_CLIENT_ID = os.environ.get('KEYCLOAK_CLIENT_ID', 'test-client')
    KEYCLOAK_CLIENT_SECRET = os.environ.get('KEYCLOAK_CLIENT_SECRET', 'secret')

    # MongoDB settings
    MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
    MONGO_PORT = int(os.environ.get('MONGO_PORT', 27017))
    MONGO_USER = os.environ.get('MONGO_USER', '')
    MONGO_PASS = os.environ.get('MONGO_PASS', '')
    MONGO_DB_NAME = os.environ.get('MONGO_DB_NAME', 'formio')

    # Splunk settings
    SPLUNK_HOST = os.environ.get('SPLUNK_HOST', 'localhost')
    SPLUNK_PORT = int(os.environ.get('SPLUNK_PORT', 8088))
    SPLUNK_TOKEN = os.environ.get('SPLUNK_TOKEN', 'your-splunk-token')
    OPENSHIFT_PLATE = os.environ.get('OPENSHIFT_PLATE', 'stuck_submissions_monitor_job')

    # Retry submission settings
    RETRY_SUBMISSION_URL = os.environ.get('RETRY_SUBMISSION_URL', 'http://localhost:5009/')
    FORMIO_BASE_URL = os.environ.get('FORMIO_BASE_URL', 'http://10.0.0.155:3001')
    WEB_FORM_BASE_URL = os.environ.get('WEB_FORM_BASE_URL', 'http://10.0.0.155:3009/digitalforms')
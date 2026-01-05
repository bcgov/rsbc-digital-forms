import os


class Config():
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'DEBUG').upper()
    ENVIRONMENT = os.getenv('ENVIRONMENT', 'dev').upper()

    DB_HOST = os.environ.get('DB_HOST', 'db')
    DB_USER = os.environ.get('DB_USER', 'testuser')
    DB_PASS = os.environ.get('DB_PASS', 'pass')
    DB_PORT = os.environ.get('DB_PORT', 5432)
    DB_NAME = os.environ.get('DB_NAME', 'test')
    DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    COMM_SERV_AUTH_URL = os.getenv('COMM_SERV_AUTH_URL', 'http://localhost')
    COMM_SERV_API_ROOT_URL = os.getenv('COMM_SERV_API_ROOT_URL', 'http://localhost')
    COMM_SERV_REALM = os.getenv('COMM_SERV_REALM', 'realm')
    COMM_SERV_CLIENT_ID = os.getenv('COMM_SERV_CLIENT_ID', '')
    COMM_SERV_CLIENT_SECRET = os.getenv('COMM_SERV_CLIENT_SECRET', '')

    RSIOPS_EMAIL_ADDRESS = os.getenv('RSIOPS_EMAIL_ADDRESS')
    REPLY_EMAIL_ADDRESS = os.getenv('REPLY_EMAIL_ADDRESS', 'do-not-reply-rsi@gov.bc.ca')
    BCC_EMAIL_ADDRESSES = os.getenv('BCC_EMAIL_ADDRESSES')

    # Splunk settings
    OPENSHIFT_PLATE                     = os.getenv('OPENSHIFT_PLATE', "be78d6-prod-form-handler")
    SPLUNK_HOST                         = os.getenv('SPLUNK_HOST', 'http://localhost')
    SPLUNK_PORT                         = int(os.getenv('SPLUNK_PORT', '8088'))
    SPLUNK_TOKEN                        = os.getenv('SPLUNK_TOKEN', 'aaaa-bbbb-cccc')
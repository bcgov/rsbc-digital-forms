import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    LOG_LEVEL                           = os.environ.get('LOG_LEVEL', 'DEBUG').upper()
    FLASK_SECRET_KEY                    = os.getenv('FLASK_SECRET_KEY', '12345')
    ICBC_API_USERNAME                   = os.getenv('ICBC_API_USERNAME', 'user')
    ICBC_API_PASSWORD                   = os.getenv('ICBC_API_PASSWORD', 'password')



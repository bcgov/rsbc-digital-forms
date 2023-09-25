import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    LOG_LEVEL                           = os.environ.get('LOG_LEVEL', 'DEBUG').upper()
    FLASK_SECRET_KEY                    = os.getenv('FLASK_SECRET_KEY', '12345')
    API_USERNAME                   = os.getenv('API_USERNAME', 'user')
    API_PASSWORD                   = os.getenv('API_PASSWORD', 'password')



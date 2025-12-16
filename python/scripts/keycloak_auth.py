from logging import Logger
import os
import requests
import datetime

class KeycloakAuth:
    KEYCLOAK_URL = os.getenv('KEYCLOAK_URL', 'https://loginproxy.gov.bc.ca/auth')
    KEYCLOAK_REALM = os.getenv('KEYCLOAK_REALM', 'rsbc-digital-forms')
    KEYCLOAK_CLIENT_ID = os.getenv('KEYCLOAK_CLIENT_ID', 'roadsafety-digital-forms-backend')
    KEYCLOAK_CLIENT_SECRET = os.getenv('KEYCLOAK_CLIENT_SECRET', 'test-secret')
    GUEST_GROUP_ID = os.getenv('GUEST_GROUP_ID', 'b2c3d4e5-f6a7-8901-2345-6789abcdef01')
    OFFICER_GROUP_ID = os.getenv('OFFICER_GROUP_ID', 'd1f1e8b3-5c4a-4e2d-9e2f-5f6e6e6e6e6e')
    MV6020_GROUP_ID = os.getenv('MV6020_GROUP_ID', 'a3b2c1d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d')

    access_token = None
    expires_in = -1000
    expiration = datetime.datetime.now() + datetime.timedelta(seconds=expires_in)
    keycloak_admin_url = f"{KEYCLOAK_URL}/admin/realms/{KEYCLOAK_REALM}"

    def __init__(self, logger: Logger):
      self.logger = logger

    def authenticate(self):
      url = f"{KeycloakAuth.KEYCLOAK_URL}/realms/{KeycloakAuth.KEYCLOAK_REALM}/protocol/openid-connect/token"
      headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
      }
      data = {
        'grant_type': 'client_credentials',
        'client_id': KeycloakAuth.KEYCLOAK_CLIENT_ID,
        'client_secret': KeycloakAuth.KEYCLOAK_CLIENT_SECRET
      }
      response = requests.post(url, headers=headers, data=data)
      if response.status_code == 200:
        return response.json()
      else:
        self.logger.error(f"Failed to retrieve access token. Status code: {response.status_code}, Response: {response.text}")
        raise Exception(f"Failed to retrieve access token. Status code: {response.status_code}, Response: {response.text}")

    def refresh_access_token(self):
      if self.expiration < datetime.datetime.now() or self.access_token is None:
        self.logger.info("Access token expired or not available, authenticating...")
        authSession = self.authenticate()
        self.expires_in = authSession.get('expires_in', 0)
        self.expiration = datetime.datetime.now() + datetime.timedelta(seconds=self.expires_in)
        self.logger.info(f"Access token will expire in {self.expires_in} seconds.")
        self.access_token = authSession.get('access_token')

    def get_header(self):
      self.refresh_access_token()
      return {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {self.access_token}"
      }

    @staticmethod
    def get_identity_provider(username):
      if username.endswith('@idir'):
        return 'azureidir'
      else:
        return 'bceidbusiness'
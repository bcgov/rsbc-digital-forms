import datetime
import os
from sqlalchemy import create_engine, Table, MetaData
import requests
import logging
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# Set up file handler for logging
file_handler = logging.FileHandler('add_users_to_keycloak.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger = logging.getLogger()
logger.addHandler(file_handler)

logger.info("Starting the script to add users to Keycloak")

# Database configuration
# ostgresql://localhost:5434/rsi_df_db
DATABASE_URI = os.getenv('DATABASE_URI', 'postgresql://testuser:pass@db:5432/test')
KEYCLOAK_URL = os.getenv('KEYCLOAK_URL', 'https://loginproxy.gov.bc.ca/auth')
KEYCLOAK_REALM = os.getenv('KEYCLOAK_REALM', 'rsbc-digital-forms')
KEYCLOAK_CLIENT_ID = os.getenv('KEYCLOAK_CLIENT_ID', 'roadsafety-digital-forms-backend')
KEYCLOAK_CLIENT_SECRET = os.getenv('KEYCLOAK_CLIENT_SECRET', 'test-secret')
GUEST_GROUP_ID = os.getenv('GUEST_GROUP_ID', '699f7ab2-6068-4fa2-9e77-0d9110b6395c')

# Create an engine and a metadata object
engine = create_engine(DATABASE_URI)
metadata = MetaData(schema='public')

# Reflect the user table
user_table = Table('user', metadata, autoload_with=engine)

def authenticate():
  url = f"{KEYCLOAK_URL}/realms/{KEYCLOAK_REALM}/protocol/openid-connect/token"
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  data = {
    'grant_type': 'client_credentials',
    'client_id': KEYCLOAK_CLIENT_ID,
    'client_secret': KEYCLOAK_CLIENT_SECRET
  }
  response = requests.post(url, headers=headers, data=data)
  if response.status_code == 200:
    return response.json()
  else:
    logger.error(f"Failed to retrieve access token. Status code: {response.status_code}, Response: {response.text}")
    raise Exception(f"Failed to retrieve access token. Status code: {response.status_code}, Response: {response.text}")

def get_identity_provider(username):
  if username.endswith('@idir'):
    return 'azureidir'
  else:
    return 'bceidbusiness'

expires_in = -1000
expiration = datetime.datetime.now() + datetime.timedelta(seconds=expires_in)
access_token = None

# Connect to the database
with engine.connect() as connection:
    # Execute a raw SQL query to fetch all users
    # result = connection.execute(user_table.select().where(user_table.columns.username.like('000ccfa6f18041f8aad6b0f7e92a3053@bceidbusiness')))
    result = connection.execute(user_table.select())

    # Print the users
    for row in result:
        logger.info(f"Processing user: {row.user_guid}")

        if expiration < datetime.datetime.now() or access_token is None:
          logger.info("Access token expired or not available, authenticating...")
          authSession = authenticate()
          expires_in = authSession.get('expires_in', 0)
          expiration = datetime.datetime.now() + datetime.timedelta(seconds=expires_in)
          logger.info(f"Access token will expire in {expires_in} seconds.")
          access_token = authSession.get('access_token')

        url = f"{KEYCLOAK_URL}/admin/realms/{KEYCLOAK_REALM}/users"
        headers = {
          'Content-Type': 'application/json',
          'Authorization': f"Bearer {access_token}"
        }

        username = row.username.replace('@idir', '@azureidir')

        countUser = requests.get(f'{url}/count', headers=headers, params={'username': username})
        if countUser.status_code != 200:
          logger.error(f"Failed to check user {username}. Status code: {countUser.status_code}, Response: {countUser.text}")
          continue
        if countUser.json() > 0:
          # User already exists, skip adding
          logger.info(f"User {username} already exists in Keycloak, skipping.")
          continue

        payload = {
          "username": username,
          "firstName": row.first_name,
          "lastName": row.last_name,
          "enabled": True,
          "totp": False,
          "federatedIdentities": [
            {
              "identityProvider": get_identity_provider(row.username),
              "userId": username,
              "userName": username
            }
          ],
          "groups": [
            "digitalforms/digitalform-officer"
          ]
        }

        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 201:
          logger.info(f"User {username} added successfully.")
          logger.info(f"location: {response.headers['Location']}")

          # Remove guest group
          delete_response = requests.delete(f"{response.headers['Location']}/groups/{GUEST_GROUP_ID}", headers=headers)
          if delete_response.status_code == 204:
            logger.info("Guest group removed successfully.")
          else:
            logger.error(f"Failed to remove guest group. Status code: {delete_response.status_code}, Response: {delete_response.text}")

        else:
          logger.error(f"Failed to add user {username}. Status code: {response.status_code}, Response: {response.text}")

logger.info("Script finished.")
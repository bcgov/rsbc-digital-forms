import os
import requests
import logging
import csv

from keycloak_auth import KeycloakAuth

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# Set up file handler for logging
file_handler = logging.FileHandler('add_MV6020_role_to_keycloak.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger = logging.getLogger()
logger.addHandler(file_handler)

logger.info("Starting the script to add users to Keycloak")

keycloak_auth = KeycloakAuth(logger)

# Read the mv6020_officers.csv file and store in memory
officers_data = []
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(script_dir, 'mv6020_officers.csv')
with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
  reader = csv.DictReader(file, skipinitialspace=True)
  for row in reader:
    officers_data.append(row)

for officer in officers_data:
  logger.info(f"Checking officer: {officer['first_name']} {officer['last_name']}")

  get_officer_search_response = requests.get(
    f"{keycloak_auth.keycloak_admin_url}/users", 
    headers=keycloak_auth.get_header(), params={
    'firstName': f"{officer['first_name']} {officer['last_name']}",
  })

  if get_officer_search_response.status_code != 200:
    logger.error(f"Failed to search for user {officer['first_name']} {officer['last_name']}. Status code: {get_officer_search_response.status_code}, Response: {get_officer_search_response.text}")
    raise Exception(f"Failed to search for user {officer['first_name']} {officer['last_name']}. Status code: {get_officer_search_response.status_code}, Response: {get_officer_search_response.text}")

  search_results = get_officer_search_response.json()

  if not search_results:
    get_officer_search_response = requests.get(
      f"{keycloak_auth.keycloak_admin_url}/users", 
      headers=keycloak_auth.get_header(), 
      params={
        'firstName': f"{officer['first_name']}",
        'lastName': f"{officer['last_name']}",
      })
    search_results = get_officer_search_response.json()

    if not search_results:
      logger.info(f"No Keycloak user found for officer: {officer['first_name']} {officer['last_name']}")
      continue

  if len(search_results) > 1:
    logger.info(f"Multiple Keycloak users found for officer: {officer['first_name']} {officer['last_name']}, skipping to avoid ambiguity.")
    continue

  member = search_results[0]
  logger.info(f"Adding MV6020 role to Keycloak user: {member['id']} - {officer['first_name']} {officer['last_name']}")

  # Add MV6020 group
  update_response = requests.put(
    f"{keycloak_auth.keycloak_admin_url}/users/{member['id']}/groups/{keycloak_auth.MV6020_GROUP_ID}", 
    headers=keycloak_auth.get_header())
  if update_response.status_code == 204:
    logger.info("Officer group added successfully.")
  else:
    logger.error(f"Failed to add officer group. Status code: {update_response.status_code}, Response: {update_response.text}")

get_mv6020_members_response = requests.get(
  f"{keycloak_auth.keycloak_admin_url}/groups/{keycloak_auth.MV6020_GROUP_ID}/members", 
  headers=keycloak_auth.get_header())

if get_mv6020_members_response.status_code != 200:
  logger.error(f"Failed to retrieve MV6020 group members. Status code: {get_mv6020_members_response.status_code}, Response: {get_mv6020_members_response.text}")
  raise Exception(f"Failed to retrieve MV6020 group members. Status code: {get_mv6020_members_response.status_code}, Response: {get_mv6020_members_response.text}")

with open('mv6020_keycloak_users.csv', mode='a', newline='', encoding='utf-8') as file:
  writer = csv.writer(file)
  writer.writerow(['first_name', 'last_name'])
  for member in get_mv6020_members_response.json():
    writer.writerow([member.get('firstName', ''), member.get('lastName', '')])
  
logger.info("Script finished.")
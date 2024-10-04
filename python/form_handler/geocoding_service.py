import logging
import requests
from python.form_handler.config import Config

geocoding_url = Config.GEOCODING_API_URL
geocoding_key = Config.GEOCODING_API_KEY


def get_coordinates(address: str, city: str)-> tuple:
    logging.debug(f'Getting coordinates for address: {address} and city: {city}')
    
    url = f'{geocoding_url}/coordinates?address={address}&city={city}'
    logging.debug(f'Geocoding API URL: {url}')
    response = requests.get(url, headers={'api-key': geocoding_key})
    if response.status_code == 200:
        get_coordinates_response = response.json()
        if get_coordinates_response['province'] != 'BC':
            logging.warning(f'Coordinates found for address: {address} and city: {city} but not in BC')
            return False, None, None
        return True, get_coordinates_response['latitude'], get_coordinates_response['longitude']
    elif response.status_code == 404:
        logging.warning(f'No coordinates found for address: {address} and city: {city}')
        return False, None, None
    else:
        raise Exception(f'Error getting coordinates for address: {address} and city: {city} -> Status: {response.status_code} Response: {response.text}')

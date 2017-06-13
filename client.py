import json
import requests
from pprint import pprint

API_KEY = 'B36OsDTH0nlOEFvmJ7VTJDzfIYc8qhjMSSlIaGBd'
owner_codes = {
    'P' : 'Privately owned',
    'T' : 'Utility owned',
    'FG' : 'Federal government owned',
    'LG' : 'Local government owned',
    'SG' : 'State government owned',
    'J' : 'Jointly owned (combination of owner types'
}

fuel_type_codes = {
    'BD' : 'Biodiesel',
    'CNG' : 'Compressed Natural Gas',
    'E85' : 'Ethanol',
    'ELEC' : 'Electric',
    'HY' : 'Hydrogen',
    'LNG' : 'Liquefied Natural Gas',
    'LPG' : 'Liquefied Petroleum Gas (Propane)'
}

status_codes = {
    'E' : 'Open',
    'P' : 'Planned',
    'T' : 'Temporarily unavailable'
}

def parse_codes(fuel_list):
    for station in fuel_list:
        for key in owner_codes: 
            if station['owner_type_code'] == key:
                station['owner_type_code'] = owner_codes[key]
        for key in fuel_type_codes:
            if station['fuel_type_code'] == key:
                station['fuel_type_code'] = fuel_type_codes[key]
        for key in status_codes:
            if station['status_code'] == key:
                station['status_code'] = status_codes[key]

    return fuel_list

def get_stations(num):
    url = 'https://developer.nrel.gov/api/alt-fuel-stations/v1.json'
    payload = {
        'api_key' : API_KEY,
    }

    if (num <= 200):
        payload['limit'] = num

    r = requests.get(url, params=payload)
    data = r.json()
    p_data = parse_codes(data['fuel_stations'])
    return p_data

def get_by_location(location):
    url = 'https://developer.nrel.gov/api/alt-fuel-stations/v1/nearest.json'
    payload = {
        'api_key' : API_KEY,
        'location' : location
    }
    r = requests.get(url, params=payload)
    data = r.json()
    p_data = parse_codes(data['fuel_stations'])
    num_results = data['total_results']
    latitude = data['latitude']
    longitude = data['longitude']
    return [p_data, {'num_result' : num_results, 'lat' : latitude, 'long' : longitude}]

def get_by_id(id):
    url = 'https://developer.nrel.gov/api/alt-fuel-stations/v1/{}.json'.format(id)
    payload = {
        'api_key' : API_KEY,
    }
    r = requests.get(url, params=payload)
    data = r.json()
    p_data = parse_codes([data['alt_fuel_station']])
    return p_data
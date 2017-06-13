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
    'BD' : 'Biodiesel (B20 and above)',
    'CNG' : 'Compressed Natural Gas',
    'E85' : 'Ethanol (E85)',
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
        'limit' : num
    }
    r = requests.get(url, params=payload)
    data = r.json()
    s_data = parse_codes(data['fuel_stations'])
    return s_data
import requests
import os

#I chose climateiq.io 's api
#It can tell you how much carbon emission a certain activity produces!

#**api key name is 'seotechdevkey' under climateiq profile
#get encrypted key:
API_KEY = os.environ.get('CLIMATEIQ_API_KEY')

if not API_KEY:
  raise RuntimeError("key not set in environment!")

#post request - get co2 estimate
url = 'https://api.climatiq.io/data/v1/estimate'

header = {'Authorization': f'Bearer {API_KEY}'}

body = {
  "emission_factor": {
    "activity_id": "electricity-supply_grid-source_residual_mix",
    "data_version": "^3",
    "region": "AU"
  },
  "parameters": {
    "energy": 100,
    "energy_unit": "kWh"
  }
}
response = requests.post(url, json=body, headers=header)

print(response.json())
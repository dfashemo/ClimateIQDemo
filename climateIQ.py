import requests
import os

#I chose climateiq.io 's api
#It can tell you how much carbon emission a certain activity produces!

#**api key name is 'seotechdevkey' under climateiq profile
#get encrypted key:
API_KEY = os.environ.get('CLIMATEIQ_API_KEY')

if not API_KEY:
  raise RuntimeError("key not set in environment!")

#base url:
base_url = 'https://api.climatiq.io/data/v1'

#pass in authentication key to header
header = {'Authorization': f'Bearer {API_KEY}'}

#post request - get co2 estimate
estimate_body = {
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
estimate_response = requests.post(base_url + '/estimate', json=estimate_body, headers=header)

print("Post Request - Estimate: ")
print()
print(estimate_response.json())
print()
print()

#get request - search
parameters = {
  "query": "light duty trucks",
  "data_version": "^21",
  "year": 2021,
  "results_per_page": 1 
}

search_response = requests.get(base_url + '/search', headers=header, params=parameters)

print("Get Request - Search: ")
print()
print(search_response.json())




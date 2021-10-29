import json
import urllib
import requests

CITY_FILE = open('cities.csv', 'w')
CITY_FILE.write(f"city;longitude;latitude\n")

where = urllib.parse.quote_plus("""
{
    "population": {
        "$gt": 600000
    }
}
""")
url = 'https://parseapi.back4app.com/classes/City?limit=20&keys=name,country,population,location&where=%s' % where
headers = {
    'X-Parse-Application-Id': '8OqPs7Pwqv4IGArgwPU8NNR2DXazz13rfoLGqPQw', # This is the fake app's application id
    'X-Parse-Master-Key': 'mU0TGsffKRtfn6l9KvLcPykabYyZwnywFUCyGtYv' # This is the fake app's readonly master key
}
data = json.loads(requests.get(url, headers=headers).content.decode('utf-8')) # Here you have the data that you need
print(len(data['results']))

for city_data1 in data['results']:
    coords = (city_data1['location']['longitude'], city_data1['location']['latitude'])
    CITY_FILE.write(f"{city_data1['name']};{coords[0]};{coords[1]}\n")
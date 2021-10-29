import json
import urllib
import requests
import openrouteservice
import time

TOKEN = '5b3ce3597851110001cf6248b143479f474642e0bb01812b54053d4b'

client = openrouteservice.Client(key=TOKEN)
DISTANCE_FILE = open('distances.csv', 'w')
DISTANCE_FILE.write(f"city1;city2;distance\n")

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
    for city_data2 in data['results']:
        time.sleep(10)
        if city_data1['name'] == city_data2['name']:
            continue
        coords = ((city_data1['location']['longitude'], city_data1['location']['latitude']),(city_data2['location']['longitude'], city_data2['location']['latitude']))
        res = client.directions(coords)
        route = res['routes'][0]['summary']['distance']/1000
        print(f" Distance bewteen {city_data1['name']} and {city_data2['name']}: {route}km")
        DISTANCE_FILE.write(f"{city_data1['name']};{city_data2['name']};{route}\n")

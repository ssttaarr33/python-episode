import json
import requests

base_url = 'http://ontariobeerapi.ca/beers/'

r = requests.get(base_url)
beerJson = json.loads(r.text)

beerMap = {}

for beer in beerJson:
    key = beer['country']
    if beer['country'] in beerMap:
        beerMap[beer['country']] = beerMap[beer['country']] + 1
    else:
        beerMap[beer['country']] = 1

print(beerMap)

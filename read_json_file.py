import json
from pprint import pprint

with open('history.json') as json_data:
    d = json.load(json_data)
    print(d)

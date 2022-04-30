import pprint
import requests 

r = requests.get('https://github.com/users/KIMDONGHAHAHA')

if r.status_code == 200:
    json_data = r.json()
    pprint.pprint(json_data)

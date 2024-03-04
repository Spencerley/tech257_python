import requests
import json

json_body = json.dumps({'postcodes': ['PR3 0SG', 'M45 6GN', 'EX165BL']})
headers = {'Content-Type': 'application/json'}
post_code_multi_req = requests.post('https://api.postcodes.io/postcodes', headers=headers, data=json_body)

print(post_code_multi_req.json())

random_postcode = requests.get('https://api.postcodes.io/random/postcodes/')
print(random_postcode.json())

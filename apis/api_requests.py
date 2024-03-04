import requests

post_codes_get_req = requests.get('https://api.postcodes.io/postcodes/se120nb')

# print(post_codes_req)
# print(post_codes_req.status_code)
# print(post_codes_req.headers)
# print(post_codes_req.content)
# print(type(post_codes_req.content))
# print(post_codes_req.json())
# print(type(post_codes_req.json()))

# How to access individual pieces of the dictionary
data_dict = post_codes_get_req.json()['result']
print(data_dict)
print(f"Region {data_dict['region']}")
print(f"Parish {data_dict['parish']}")


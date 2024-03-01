import os
import json

path_to_json = "example.json"

json = json.loads(open(path_to_json).read())

for key in json:
    value = json[key]
    print(f' the key is {key} and the value is {value}')

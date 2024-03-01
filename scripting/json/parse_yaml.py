import os
import yaml

path_to_yaml = "output.yaml"

yaml_file = yaml.full_load(open(path_to_yaml).read())

for key in yaml_file:
    value = yaml_file[key]
    print(f' the key is {key} and the value is {value}')

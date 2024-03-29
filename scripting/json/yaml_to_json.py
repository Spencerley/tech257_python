import json
import os
import sys
import yaml

# Checking if there is a file passed
if len(sys.argv) > 1:
    # Opening the file
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = yaml.safe_load(source_file)
        source_file.close()
    else:
        print(f'ERROR {sys.argv[1]} not found')
        exit(1)
else:
    print(f'Usage: python json_to_yaml.py <source_json_file.json> <target_yaml_file.yaml')

# Process the conversion - use yaml library
json_file = json.dumps(source_content)

# Save the conversion in a new file output.yaml
with open(os.path.join('output.json'), 'w') as file1:
    file1.write(json_file)

import sys
import os
import subprocess
import json

# os
# os.mkdir('test_dir')

# sys
# if len(sys.argv) > 1:
#     print('You gave me an argument')

# subprocess
# subprocess.run(["python", "hello_world.py"])

# json
x = {
    'name': 'Spencer',
    'age': 27,
    'city': 'Birmingham'
}

y = json.dumps(x)

print(type(x))

print(type(y))

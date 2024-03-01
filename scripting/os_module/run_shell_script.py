import os
import subprocess

script_dir = os.path.dirname(__file__)
print(script_dir)

script_absolute_path = os.path.join(script_dir + '/script.sh')

subprocess.call(['sh', script_absolute_path])

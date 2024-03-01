import os

# Directory
directory = 'test_dir'

# Path to parent dir
parent_dir = 'C:/Users/space/Documents'

# path
path = os.path.join(parent_dir, directory)

# Create the dir
os.mkdir(path)

import os

# Directory
directory = 'test_dir'

# Path to parent dir
parent_dir = 'C:/Users/space/Documents'

# path
path = os.path.join(parent_dir, directory)

# File name and path
file_name = 'testfile.txt'
file_path = os.path.join(path, file_name)

with open(os.path.join(path, file_name), 'w') as file1:
    to_file = 'contents of the file are here'
    file1.write(to_file)

print(f'File {file_name} created in {directory}')

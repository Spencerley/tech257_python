# Most important rule of slicing is

hi_str = "Hello World!"
print(hi_str)

print(len(hi_str))

print("get the first character")
print(hi_str[0])  # indexing starts at 0

print("get the last character")
print(hi_str[-1])
print(hi_str[11])

print("get the third to the fifth character")
# formula for slicing: hi_str[starting index:ending index] ending index is where it goes up to but does not include
print(hi_str[2:5])
# If you don't specify an end index it will go to the end
print(hi_str[6:])
# -indexing gives it a place to start from at the end then continues to the end
print(hi_str[-3:])
# prints from the beginning to the end index
print(hi_str[:5])


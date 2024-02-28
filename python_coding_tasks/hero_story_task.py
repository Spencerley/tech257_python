# First part
# print("You are about to create your own epic story... be as creative and imaginative as you'd like")
# Define a dictionary called story1. It should have the following keys:
# 'start', 'middle' and 'end'
# story1 = {
#     'start': input('Write the beginning of your Story: '),
#     'middle': input('Write the middle of your Story: '),
#     'end': input('Write the ending of your Story: ')
# }
#
# Print the entire dictionary
# print(story1)

# Print the type of your dictionary
# print(type(story1))

# Print only the keys
# print(story1.keys())

# Print only the values
# print(story1.values())

# Print the individual values using the keys (individually, lots of print commands)
# print(story1['start'])
# print(story1['middle'])
# print(story1['end'])

# Now, let's add a new key:value pair:
# 'hero': yourSuperHero
# story1['hero'] = 'Spencer'
# print(story1)

# Hints:
# THE MORE CREATIVE THE BETTER

# If time
# Improve the program. For example, can you make it a "Choose your own adventure" story?

print("You are about to create your own epic story... be as creative and imaginative as you'd like")
# Define a dictionary called story1. It should have the following keys:
# 'start', 'middle' and 'end'
story1 = {
    'hero': input('Choose your hero\'s name: '),
    'middle': 'They jump up and defeat all their demons',
    'end': input('Write the ending of your Story: ')
}

story1['start'] = f'{story1['hero']} wakes up after confused before remembering they were hit on the head...'

# Print the entire dictionary
# print(story1)
# Print the type of your dictionary
# print(type(story1))
# Print only the keys
# print(story1.keys())
# Print only the values
# print(story1.values())
# Print the individual values using the keys (individually, lots of print commands)
print(story1['start'])
print(story1['middle'])
print(story1['end'])

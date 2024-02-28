# Follow the instructions below to create various 'for loops'.
#
# Starting code to put at the top:
list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1, 2, 3], [4, 5, 6]]
dict_data = {
    1: {"name": "Bronson", "money": "$0.05"},
    2: {"name": "Masha", "money": "$3.66"},
    3: {"name": "Roscoe", "money": "$1.14"}
}

# Loop through the list Under the starting code,
# write a for loop to print the double of each number in the list 'list_data'.
# It should loop through the numbers in list_data - each item in the list should be called 'num' (for number)
# Inside the loop, it should print out the double of each number in the list.
for num in list_data:
    print(num * 2)

print('')
# Loop through the 'embedded_lists' list
# Write another for loop to print the items inside 'embedded_lists'.
# Each item in the list should be called 'data'
# It should output this to the screen:
# [1, 2, 3]
# [4, 5, 6]
for data in embedded_lists:
    print(data)
    for i in data:
        print(i)

# Loop through the lists embedded inside a list We need to access the data within the lists,
# so now we need an embedded loop.

# Create another loop inside the 'embedded_lists' for loop to list the individual items in the lists.
# You should end up with this output:
# [1, 2, 3]
# 1
# 2
# 3
# [4, 5, 6]
# 4
# 5
# 6

print('')

# Loop through a dictionary Write another for loop to loop through the dictionary 'dict_data'.
# It should print the keys to the screen like this:
# 1
# 2
# 3

for keys in dict_data:
    print(keys)

print('')

# Loop through a dictionary and print its values Write another for loop to loop through the dictionary 'dict_data'.
# Use to the dictionary's value() method to print the value for each key in the dictionary. Output should be:
# {'name': 'Bronson', 'money': '$0.05'}
# {'name': 'Masha', 'money': '$3.66'}
# {'name': 'Roscoe', 'money': '$1.14'}
for values in dict_data.values():
    print(values)

print('')

# Loop to print the values of the dictionary items inside a dictionary
# Copy and paste the last for loop as a starting point for this loop.
for values in dict_data.values():
    for i in values.values():
        print(i)


# Generate an embedded for loop (a loop within a loop) to extract and print the values
# within the dictionary of each item in the dictionary. Output should be:
# Bronson
# $0.05
# Masha
# $3.66
# Roscoe
# $1.14

print('')

# Loop to print specific values of the dictionary items inside a dictionary
# Write another for loop to loop through the dictionary 'dict_data' but this time only print out the money values.
# Output should be:
# $0.05
# $3.66
# $1.14

for values in dict_data.values():
    print(values['money'])

# Loop through a list with a nested if statement Write another loop to loop through the items in 'list_data'
# and include a nested (indented) if statement inside the loop so that when it loops it checks the number/item in list:
# if the number is less than 3, it prints 'less than 3'
# if the number equals 3, it prints 'I found three'
# if the number is greater than 3, it prints 'greater than 3'
# Output should be:
# less than 3
# less than 3
# I found three
# greater than 3
# greater than 3

print('')

for i in list_data:
    if i < 3:
        print('less than 3')
    elif i == 3:
        print('I found 3')
    elif i > 3:
        print('greater than 3')

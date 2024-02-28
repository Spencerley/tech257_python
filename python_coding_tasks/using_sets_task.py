# Explain 2 main ways that sets are different to lists and tuples
# Sets an unordered and unchangeable, value 1 == True and value 0 == False
# Can add and delete from but not replace items
# A set is a collection of unique data, meaning that elements within a set cannot be duplicated.
# Create a set named 'fruits' containing "apple", "banana", and "cherry".
fruits = {'apple', 'banana', 'cherry'}
# Print the set 'fruits'
print(fruits)
# Add "orange" to the fruits set using one of the set's methods.
fruits.add('orange')
# Print the set 'fruits' - check it's added
print(fruits)
# Remove "banana" from the fruits set using one of the set's methods.
fruits.remove('banana')
# Print the set 'fruits' - check it's removed
print(fruits)
# Attempt to add another "apple" to the fruits set. What do you observe? Why does this happen?
fruits.add('apple')
# Print the final fruits set.
print(fruits)
# Print the 2nd item in the set. If there is any problem doing this, explain.
# print(fruits[1])
fruits_list = list(fruits)
print(fruits_list[1])
# You cannot print an item in a set through indexing because sets are unordered.
# Therefore, items in a set do not have an index


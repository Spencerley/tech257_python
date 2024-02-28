# Rationale: To practice lists
# Script should act like a waiter at a restaurant taking orders

# level 1

# Greet the user
print("Hello and welcome to our restaurant")

# Print a list of starters
starters = ["Soup of the day", "Baked Camembert", "Garlic Mushrooms"]
print(starters)

# Take an input for the user for their starter
starter_order = input("What can I get you started with?")

# Print a list of mains
mains = ["Steak", "Chicken", "Pork", "Lamb"]
print(mains)

# Take an input for the user for their main course
main_order = input("What can I get you for your main?")

# Print a list of desserts
desserts = ["Creme Brulee", "Ice Cream", "Chocolate Gateau"]
print(desserts)

# Take an input for the user for their dessert
dessert_order = input("What would you like for dessert?")

# Print all of the user's choices
customer_order_list = [starter_order, main_order, dessert_order]
print(f"Okay so we're starting off with {customer_order_list[0]}, then onto {customer_order_list[1]} and finishing with {customer_order_list[2]}")

# level 2
# Use at least one f-string
# Add each item ordered to a list called 'customer_order_list'

# if time: level 3 (may need research if we have not covered dictionaries yet)
# Use dictionaries and assign prices to the items. Create a bill at the end of the program.
starter_dict = {
    starters[0]: 4.50,
    starters[1]: 6.25,
    starters[2]: 5.00
}

main_dict = {
    mains[0]: 24.99,
    mains[1]: 14.85,
    mains[2]: 18.90,
    mains[3]: 21.50
}

dessert_dict = {
    desserts[0]: 10.89,
    desserts[1]: 8.99,
    desserts[2]: 14.99
}

# print(starter_dict, main_dict, dessert_dict)

for customer_order_list[0] in starter_dict:
    if customer_order_list[0] == starter_dict.get(starters[0]):
        starter_price = 4.50
    elif customer_order_list[0] == starter_dict.get(starters[1]):
        starter_price = 6.25
    else:
        starter_price = 5.00

for customer_order_list[1] in main_dict:
    if customer_order_list[1] == main_dict.get(mains[0]):
        mains_price = 24.99
    elif customer_order_list[1] == main_dict.get(mains[1]):
        mains_price = 14.85
    elif customer_order_list[1] == main_dict.get(mains[2]):
        mains_price = 18.90
    else:
        mains = 21.50

for customer_order_list[2] in dessert_dict:
    if customer_order_list[2] == dessert_dict.get(starters[0]):
        dessert_price = 10.89
    elif customer_order_list[2] == dessert_dict.get(starters[1]):
        dessert_price = 8.99
    else:
        dessert_price = 14.99

bill = [starter_price, mains_price, dessert_price]
print(bill)

# if time: level 4
# Add more to this program. Recommended ways are: Only allow input that is within the list, Add quantities of order etc.

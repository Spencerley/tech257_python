from datetime import date
# Use your code from the "Task: Get name, age and DOB details from a user".
age_int = int(input("What is your age? "))
birth_month_int = int(input("What is your birth month? "))
name_str = str(input("What is your name? "))
today_date = date.today()

year_of_birth = today_date.year - age_int

# Mix the name, age and DOB into one list user_details_list
user_details_list = [name_str, age_int, year_of_birth]
# Print the user's name, age and DOB from the list
print(user_details_list[0])
print(user_details_list[1])
print(user_details_list[2])

# Check the age is saved as an integer in the list. If it's not, work out how to convert it to an integer and add the age integer to the list.
print(type(user_details_list[1]))

# Ask the user for their height in cm and save it to the variable height
height_in_cm = float(input("What is your height in cm? "))

# Save height as a float in the list, and print the height from the list.
user_details_list.append(height_in_cm)
print(user_details_list[3])

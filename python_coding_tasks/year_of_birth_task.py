from datetime import date
from datetime import time
from datetime import datetime

# First part
# define the variables age_int and name_str (set dummy/default/initial values)
age_int = int(input("What is your age? "))
birth_month_int = int(input("What is your birth month? "))
name_str = str(input("What is your name? "))

# make a calculation for the year in which the person was born
today_date = date.today()

year_of_birth = today_date.year - age_int

# print out "OMG , you are years old, so you were born in " with the correct values
print(f"OMG {name_str}, you are {age_int} years old, so you were born in {year_of_birth}")

# Second Part
# prompt the user for inputs and assign the variable age_int and name_str
# remove the initial values set - see above


# Third Part
# calculate and print out the total number of hours this person has lived
todays_timestamp = datetime.now()

birth_data = datetime(year_of_birth, birth_month_int, day=1, hour=0, minute=0, second=0)

hours_lived = todays_timestamp - birth_data

hours = hours_lived.total_seconds() / 3600

print(hours)

# If time
# figure out a way to account for if the persons birthday has already happened this year or not
# go look into the library 'time' to be more accurate with the hours lived
# show in your script that you have evaluated the methods of calculating the hours lived to see which is more accurate


# Acceptance Criteria
# program defines the variable age_int and name_str
# program prints the string "OMG , you are years old, so you were born in "

# Summary
# Print incremented numbers to the screen but substitute multiples of 3 with 'Fizz', multiples of 5 with 'Buzz',
# and multiples of both with 'FizzBuzz'
#
#
# Rationale
# Great to consolidate control flow topic.

# The task
# Core:

# Make a new 'fizzbuzz.py' file
# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz" instead of the number
# For numbers which are multiples of both three and five print "FizzBuzz".

fizz = int(input('What number would you like multiples of to become Fizz? '))
buzz = int(input('What number would you like multiples of to become Buzz? '))


def is_fizz_buzz(number):
    return number % fizz == 0 and number % buzz == 0


def is_fizz(number):
    return number % fizz == 0


def is_buzz(number):
    return number % buzz == 0


for num in range(1, 101):
    if is_fizz_buzz(num):
        print("FizzBuzz")
    elif is_fizz(num):
        print("Fizz")
    elif is_buzz(num):
        print("Buzz")
    else:
        print(num)


# If time:

# Improve the script, so we can decide which numbers to substitute for "Fizz" and "Buzz"
# Refactor using functions

# Acceptance Criteria
# All core task are done
# Core works with no error

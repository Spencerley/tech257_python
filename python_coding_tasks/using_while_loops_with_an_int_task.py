# Create a new file named 'while_loops.py' or similar.
# Initialise x with the value of 0
# Create, a while statement so that it loops while x is less than 10. Everytime it loops it should:
# Print the value of x to the screen in an f-string
# Increment (add 1 to x)
# Running this code should produce:

# If you don't increment x you will have an infinite loop as the statement will never become false.

x = 0
while x < 10:
    print(f'{x}')
    x += 1

# Once your code works, find out what happens when you run the code if you
# comment out the first line which initialises 'x'. It doesn't run because x is undefined.

# Write a brief comment on the line before the code which increments x
# to explain what would happen if you don't increment x.

# Copy and paste your working 'while loop' underneath the 'while loop'.
# Modify the second copy of the 'while loop' so that it breaks out of the loop when x equals 4.
print('')

x = 0

while x < 10:
    print(f'{x}')
    x += 1
    if x == 4:
        print(x)
        break
print('end of loop')

# The output should be:
# print x -> 0
# print x -> 1
# print x -> 2
# print x -> 3
# print x -> 4

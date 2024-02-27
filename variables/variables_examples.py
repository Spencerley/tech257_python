# A variable is a box to store information in
a = 1
b = 2
c = 3.5
hi = "Hello World!"

print(b)
print(type(a))  # Integer
print(type(b))  # Integer
print(type(c))  # Floating point number i.e. has a decimal even if its 3.0 for example
print(type(hi))  # String

# Python is not a strongly typed language you don't have to declare types, so you can reassign types.
# Helpful to use good variable names to identify type of or use for variables

x = 5
y = x
print("before reassignment...")
print("value of x:", x)
print("ID of x:", id(x))
print("value of y:", y)
print("ID of y:", id(y))

x = 10
print("after reassignment...")
print("value of x:", x)
print("ID of x:", id(x))
print("value of y:", y)
print("ID of y:", id(y))

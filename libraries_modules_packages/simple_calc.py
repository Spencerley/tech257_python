# Mini-calculator
from math_operations import add, subtract, multiply, divide

first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the first number: "))

add_result = add(first_num, second_num)
print(f"{first_num} + {second_num} = {add_result}")

sub_result = subtract(first_num, second_num)
print(f"{first_num} - {second_num} = {sub_result}")

multiply_result = multiply(first_num, second_num)
print(f"{first_num} x {second_num} = {multiply_result}")

divide_result = divide(first_num, second_num)
print(f"{first_num} / {second_num} = {divide_result}")

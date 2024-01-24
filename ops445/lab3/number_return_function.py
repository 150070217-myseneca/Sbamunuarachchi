#!/usr/bin/env python3

# number_return_function.py

def return_number_value():
    num1 = 10
    num2 = 5
    num3 = num1 + num2
    return num3

# Call the function and use the returned number
number = return_number_value()
print(number)
print(number + 5)
print(return_number_value() + 10)

# Try to combine numbers and strings
# This will cause an error, and then fix it using str() function
# print('my number is ' + number)  # This line is commented out to avoid an error
print('my number is ', number)
print('my number is ' + str(number))
print('my number is ' + str(return_number_value()))

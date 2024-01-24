#!/usr/bin/env python3
# simple_function.py

def hello():
    print('Hello World')
    print('Inside a Function')

# Call the function three times
hello()
hello()
hello()

# Call the function and check the return value
my_stuff = hello()
print('Stuff return from hello():', my_stuff)
print('The object my_stuff is of type:', type(my_stuff))

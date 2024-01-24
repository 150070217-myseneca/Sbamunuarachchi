#!/usr/bin/env python3

# string_return_function.py

def return_text_value():
    name = 'Terry'
    greeting = 'Good Morning ' + name
    return greeting

# Call the function and assign the returned value to a variable
text = return_text_value()

# Print the returned string
print(text)

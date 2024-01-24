#!/usr/bin/env python3

#Creating Simple Functions

def hello():
    print('Hello World')
    print('Inside a Function')
    return

my_stuff = hello()
print('Stuff return from hello():',my_stuff)
print('the object my_stuff is of type:',type(my_stuff))

#Part 2 - Function that does not take argument but returns a string

def return_text_value():
    name = 'Terry'
    greeting = 'Good morning ' + name
    return greeting

text =return_text_value()

print(text)
print(return_text_value())

#Part 3 - Function that does not take argument but returns an number

def return_number_value():
    num1 = 10
    num2 = 5
    num3 = num1 + num2
    return num3

return_number_value()
print(return_number_value())

number = return_number_value()

print(number)
print(number + 5)
print(return_number_value() + 10 )

print('My number is ' + str(number))

number = return_number_value()
print('my number and is is ', number)
print('my number and is is ' , number)
print('my number is ' + str(number))
print('my number is ' + str(return_number_value()))
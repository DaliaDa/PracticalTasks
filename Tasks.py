#Write a program to print out all the numbers from 0 to 100 that are divisible by 7
for x in range(0, 100, 7):
    print(x)

#Write a program in Python to reverse a word. Words should be provided using input function.
txt = input("Text here: ") [::-1]
print (txt)

#Write a Python program to reverse a string.
string=("1234abcd") [::-1]
print(string)

#Write a Python function to find the Max of three numbers.
def max_of_two( a, b ):
    if a > b:
        return a
    return b
def max_of_three( a, b, c ):
    return max_of_two( a, max_of_two( b, c ) )
print(max_of_three(10, 20, 30))

#DEF, arguments, docstring
def sum_numbers(*numbers: tuple) -> float:
    """Sum numbers"""
    return sum(numbers)

print(sum_numbers(1, 2, 3, 4, 5))

#Write a Python program to subtract five days from the current date.

x = input ("Enter your name: ")
from datetime import date, timedelta
dt = date.today() - timedelta(5)
print('Hello, ', x,',', ' today is: ', date.today(), sep='')
print('5 days ago was:',dt)
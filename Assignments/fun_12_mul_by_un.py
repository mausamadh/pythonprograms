'''
Write a Python program to create a function that takes one argument, and
that argument will be multiplied with an unknown given number.
'''

import random

def mul_unknown(number):
    return number * random.randint(1,1000)

print(mul_unknown(5))
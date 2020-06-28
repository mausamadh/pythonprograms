'''
Write a Python program to check whether a given string is number or not
using Lambda.
'''
str_is_num = lambda string : string.isnumeric()

print(str_is_num('123w'))
'''
Write a Python program to get a string made of the first 2 and the last 2 chars
from a given a string. If the string length is less than 2, return instead of the
empty string.
Sample String : 'Python'
Expected Result : 'Pyon'
Sample String : 'Py'
Expected Result : 'PyPy'
Sample String : ' w'
Expected Result : Empty String
'''


def get_two_from_each_side(passed_string):
    if len(passed_string)<2:
         return " " 
    else:
        return passed_string[:2:]+passed_string[len(passed_string)-2::] 
x=get_two_from_each_side("w")
print(x)

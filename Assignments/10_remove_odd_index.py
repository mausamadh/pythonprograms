'''
Write a Python program to remove the characters which have odd index
values of a given string.
'''

def remove_odd_index(given_string):
    new_string = ""
    for index in range(0,len(given_string),2):
        new_string += given_string[index]
    print(new_string)

remove_odd_index("help me in this")
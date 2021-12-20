'''
Write a Python program to check a list is empty or not.
'''

given_list = ['abc', 'xyz', 'aba', '1221']

def check_this_list(input_list):
    if len(input_list)<=0:
        print('empty list')
    else:
        print(input_list)

check_this_list(given_list)
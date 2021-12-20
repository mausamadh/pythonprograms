'''
Write a Python program to clone or copy a list.
'''

def copy_list(given_list):
    new_list = given_list[:] #we used slicing technique for copying can use copy.copy too
    return new_list

given_list = ['abc', 'xyz', 'aba', '1221']
new_list = copy_list(given_list)
print(new_list)
'''
Write a Python program to change a given string to a new string where the first
and last chars have been exchanged.
'''
def change_first_last_char(my_string):
    return my_string[len(my_string)-1] + my_string[1:len(my_string)-1:] + my_string[0]

dummy_string = "My name is khan"
changed_string = change_first_last_char(dummy_string)
print(changed_string)

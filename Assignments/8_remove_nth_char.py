'''
Write a Python program to remove the n th index character from 
a nonempty string.
'''
string = 'My name is khan'
n_index = 10
def remove_nth_indexed_char(my_string,n_index):
    new_string = my_string[:n_index:]+my_string[n_index+1::]
    return new_string


my_string = remove_nth_indexed_char(string,n_index)
print(my_string)
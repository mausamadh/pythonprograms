'''
Write a Python program to remove a key from a dictionary.
'''

def remove_items_in_dict(dict1:dict,key):
    dict1.pop(key)
    return dict1

dict1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
key = eval(input("enter key to remove from dict:"))
print(remove_items_in_dict(dict1,key))
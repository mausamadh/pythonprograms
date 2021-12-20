'''
Write a Python program to sum all the items in a dictionary.
'''
def sum_all_items_in_dict(dict1:dict):
    return sum(dict1.values())+sum(dict1)

dict1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
print(sum_all_items_in_dict(dict1))
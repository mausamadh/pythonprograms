'''
Write a Python program to multiply all the items in a dictionary.
'''
def mul_all_items_in_dict(dict1:dict):
    result =1
    for items in dict1:
        result*=items #* dict1[items]
    for items in dict1.values():
        result *= items
    return result

dict1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
print(mul_all_items_in_dict(dict1))
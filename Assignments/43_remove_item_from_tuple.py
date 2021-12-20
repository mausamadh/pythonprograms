'''
Write a Python program to remove an item from a tuple.
'''
my_tuple = (1,2,3,4,5,6)

def remove_item_from_tuple(tuple1:tuple,item):
    new_list = list(tuple1)
    new_list.remove(item)
    return tuple(new_list)

print(remove_item_from_tuple(my_tuple,4))
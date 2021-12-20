'''

Write a Python program to find the index of an item of a tuple.
'''
my_tuple = (1,2,3,4,5,6)

def index_item_from_tuple(tuple1:tuple,item):
    new_list = list(tuple1)
    index = new_list.index(item)
    return index

print(index_item_from_tuple(my_tuple,4))
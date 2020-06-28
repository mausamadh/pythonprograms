'''
Write a Python program to slice a tuple.
'''

my_tuple = (1,2,3,4,5,6)

def slice_item_from_tuple(tuple1:tuple,start,end):
    new_list = list()
    for index in range(start,end):
        new_list.append(tuple1[index])
    return tuple(new_list)

print(slice_item_from_tuple(my_tuple,4,6))
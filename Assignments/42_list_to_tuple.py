'''
Write a Python program to convert a list to a tuple.
'''
def list_to_tuple(list1:list):
    return tuple(list1)

list1 = [1,2,3,4,5]
result = list_to_tuple(list1)
print(result)
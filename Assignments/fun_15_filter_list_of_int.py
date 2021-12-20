'''
Write a Python program to filter a list of integers using Lambda.
'''

filter_list_of_int = lambda list1: list(filter(lambda x: isinstance(x,int),list1))

print(filter_list_of_int(['a',1,1,2,3,3,4,5,6,'abc']))
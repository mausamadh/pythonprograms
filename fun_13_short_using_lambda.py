'''
Write a Python program to sort a list of tuples using Lambda.
'''
sort_tuples = lambda list1: list1.sort()

list_of_tuples = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

sort_tuples(list_of_tuples)
print(list_of_tuples) #sorted by first elem
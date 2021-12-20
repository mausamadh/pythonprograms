'''
Write a Python program to get a list, sorted in increasing order by the last
element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
'''

def get_from_tuple(item):
    return item[len(item)-1]

def sort_by_last_elem(sort_me):
    sort_me.sort(key=get_from_tuple)
    return sort_me

Sample_List = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
result = sort_by_last_elem(Sample_List)
print(result)
'''
Write a Python program that accepts a comma separated sequence of words
as input and prints the unique words in sorted form (alphanumerically).
'''

def sorted_here(sort_me): 
    return sorted(set(sort_me))

items_to_be_sorted = ['red', 'white', 'black', 'red', 'green', 'black']
after_sorting = sorted_here(items_to_be_sorted)
print(after_sorting)

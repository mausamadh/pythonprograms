'''
18. Write a Python program to get the largest number from a list.
'''

def get_largest(given_list):
    largest = float('-inf') # a number smaller all than others
    for item in given_list:
        if largest<item:
            largest=item
    return largest


list1=[1,2,3,4,5,6,7,8,9]
print(get_largest(list1))

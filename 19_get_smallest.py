'''
Write a Python program to get the smallest number from a list.
'''

def get_smallest(given_list):
    smallest = float('inf') #number greater all than others
    for item in given_list:
        if smallest>item:
            smallest=item
    return smallest


list1=[1,2,3,4,5,6,7,8,9]
print(get_smallest(list1))

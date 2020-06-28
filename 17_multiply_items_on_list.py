'''
Write a Python program to multiplies all the items in a list.
'''

def multiply_items(list_items):
    result = 1
    for index in range(len(list_items)):
        result *= list_items[index]
    return result

list1 = [1,2,3,4,5,6,7,8,9]
result = multiply_items(list1)
print(result)
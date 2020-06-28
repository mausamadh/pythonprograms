'''
Write a Python function to multiply all the numbers in a list.
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336
'''

def mul_list(list1:list):
    result = 1
    for items in list1:
        result *= items
    return result


sample_list = [8, 2, 3, -1, 7]
print(mul_list(sample_list))
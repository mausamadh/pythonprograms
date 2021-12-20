'''
Write a Python program to replace the last element in a list with another list.
Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
'''
def merge_list(list1:list,list2:list):
    return list1[:len(list1)-1:]+list2


sample_data = [1, 3, 5, 7, 9, 10]
another_data =  [2, 4, 6, 8]

result = merge_list(sample_data,another_data)
print(result)
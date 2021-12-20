'''
Write a Python program to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]
'''
def evem_in_list(list1:list):
    new_list = []
    for item in list1:
        if item%2==0:
            new_list.append(item)

    return new_list

Sample_List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(evem_in_list(Sample_List))
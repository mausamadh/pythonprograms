'''
Write a Python program to insert a given string at the beginning of all items in
a list.

Sample list : [1,2,3,4], string : emp
Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
'''

def add_string_to_all(list1:list,string:str):
    for index in range(len(list1)):
        list1[index] = string + str(list1[index])
        print(list1[index])
    print(list1)


add_string_to_all([1,2,3,4],'emp')
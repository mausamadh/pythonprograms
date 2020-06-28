'''
25. Write a Python program to check whether all dictionaries in a list are empty or
not.

Sample list : [{},{},{}]
Return value : True

Sample list : [{1,2},{},{}]
Return value : False
'''


def is_dict_in_list_empty(list1):
    for item in list1:
        if not item:
            result = True
        else:
            result  = False
            return result
    return result

sample_list1 = [{},{},{}]
sample_list2 = [{},{1:2},{},{}]
sample_list3 = [{},{},{},{},{},{},{},{},{1:2},{},{},{1:2},{},{}]
print(is_dict_in_list_empty(sample_list1))
print(is_dict_in_list_empty(sample_list2))
print(is_dict_in_list_empty(sample_list3))
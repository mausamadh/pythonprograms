'''
Write a Python script to merge two Python dictionaries.
'''

def merge_dict(dict1,dict2):
    dict1.update(dict2)
    return dict1

dict1={1:10, 2:20}
dict2={3:30, 4:40}
print(merge_dict(dict1,dict2))
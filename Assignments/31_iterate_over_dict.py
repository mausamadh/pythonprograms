'''
31. Write a Python program to iterate over dictionaries using for loops.
'''
dict1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

for keys in dict1.keys():
    print(keys ," : ", dict1[keys])
'''
Write a Python script to add a key to a dictionary.

Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}
'''

dictionary = {0: 10, 1: 20}
dictionary[2]=30
print(dictionary)
def add_key(dict1,key,value):
    dict1[key] = value
    return dict1

key = 1
while True:
    key = eval(input("Enter Key to dictionary (enter 0 to exit): "))
    if key == 0:
        exit(0)
    value = eval(input("Enter value to dictionary : "))

    print(add_key(dictionary,key,value))

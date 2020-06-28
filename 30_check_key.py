'''
Write a Python script to check whether a given key already exists in a
dictionary.
'''

dictionary = {0: 10, 1: 20}
dictionary[2]=30
print(dictionary)
def check_key(dict1,key):
    if key in dict1.keys():
        print('key already exists!!!')
    else:
        print('key doesnot exist in this dict')
    return dict1

key = 1
while True:
    key = eval(input("Enter Key to dictionary (enter 0 to exit): "))
    if key == 0:
        exit(0)

    print(check_key(dictionary,key))
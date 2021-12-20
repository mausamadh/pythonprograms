'''
Write a Python script to print a dictionary where the keys are numbers
between 1 and 15 (both included) and the values are square of keys

Sample Dictionary
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144,
13: 169, 14: 196, 15: 225}
'''

def create_dict(number:int):
    dict1 = {}
    for x in range(1,number+1):
        dict1[x]= x*x
    return dict1

number = 15 #eval(input("enter number to create dict from 1 to n keys:"))
dict2 = create_dict(number)
print(dict2)
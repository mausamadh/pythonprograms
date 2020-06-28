'''
Write a Python script to generate and print a dictionary that contains a
number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
'''

def create_dict(number:int):
    dict1 = {}
    for x in range(1,number+1):
        dict1[x]= x*x
    return dict1

number = eval(input("enter number to create dict from 1 to n keys:"))
dict2 = create_dict(number)
print(dict2)
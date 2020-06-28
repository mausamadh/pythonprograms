'''
Write a Python program to convert a tuple to a string.
'''
my_tuple = (1,2,3,4,5,6)
new_str = ""
for item in my_tuple:
    #print(item)
    
    new_str += str(item)

print(new_str)
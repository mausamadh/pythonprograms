'''
Write a Python program to create a lambda function that adds 15 to a given
number passed in as an argument, also create a lambda function that multiplies
argument x with argument y and print the result.
'''

add = lambda number:number+15
multiply = lambda a,b:a*b

print(add(10))
print(multiply(2,3))
'''
Write a Python program to square and cube every number in a given list of
integers using Lambda.
'''

square_numbers = lambda list1 : list(map(lambda x:x**2 , list1))
cube_numbers = lambda list1 : list(map(lambda x:x**3 , list1))

print(square_numbers([1,2,34,4]))
print(cube_numbers([1,2,34,4]))

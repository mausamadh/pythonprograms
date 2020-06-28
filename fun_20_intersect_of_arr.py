'''
Write a Python program to find intersection of two given arrays using
Lambda.
'''

intersection_of_arr = lambda fist_arr,second_arr : list(set(fist_arr).intersection(set(second_arr)))

print(intersection_of_arr([1,2,3,45,6,7,8],[4,5,54,3,6,4]))
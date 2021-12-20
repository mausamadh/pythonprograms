'''
Write a Python program to sort a list of dictionaries using Lambda.
'''


sample_dict = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
sort_dict = sorted(sample_dict , key = lambda x:x['color'])

#sort_dict(sample_dict)
print(sample_dict)
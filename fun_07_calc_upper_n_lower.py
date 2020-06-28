'''
Write a Python function that accepts a string and calculate the number of
upper case letters and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12
'''

def count_upper_and_lower(string:str):
    count_upper=0
    count_lower=0
    for index in range(len(string)):
        if string[index].isupper():
            count_upper +=1
        elif string[index].islower():
            count_lower +=1
        else:
            pass

    print('No. of Upper case characters :',count_upper)
    print('No. of Lower case characters :',count_lower)


count_upper_and_lower('The quick Brow Fox')

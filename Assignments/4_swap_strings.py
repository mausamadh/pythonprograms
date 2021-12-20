'''
Write a Python program to get a single string from two given strings, separated
by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
'''
abc = 'abc'
xyz = 'xyz'
def swap_firts_two_letters(first_string,second_string):
    return second_string[:2:]+first_string[2::]+" "+first_string[:2:]+second_string[2::]

result = swap_firts_two_letters(abc,xyz)
print(result)
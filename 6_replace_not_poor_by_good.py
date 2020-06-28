'''
Write a Python program to find the first appearance of the substring 'not' and
'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
substring with 'good'. Return the resulting string.
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'
'''
check_this_string = "The lyrics is not that poor!"
def check_this(check_this_string):
    if "not" in check_this_string:
        if 'poor' in check_this_string:
            not_index = check_this_string.index("not")
            poor_index = check_this_string.index("poor")
            new_string = check_this_string[:not_index:]+"good"+check_this_string[poor_index+4::]
            return new_string
    else:
        return check_this_string

new_string = check_this(check_this_string)
print(new_string)
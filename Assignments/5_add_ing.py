'''
Write a Python program to add 'ing' at the end of a given string (length should
be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
string length of the given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
'''
check_string='google'

def add_ing(add_ing_to_me):
    if len(add_ing_to_me)<3:
        return add_ing_to_me
    else:
        if add_ing_to_me[len(add_ing_to_me)-3::]=="ing":
            return add_ing_to_me+"ly"
        else:
            return add_ing_to_me+"ing"

check = add_ing(check_string)
print(check)

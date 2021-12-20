'''
Write a Python script that takes input from the user and displays that input
back in upper and lower cases.
'''
def convert_to_lower_and_upper(convert_me):
    print(convert_me.upper())
    print(convert_me.lower())

input_from_user = input("Enter your words to be converted to upper and lower cases: ")
convert_to_lower_and_upper(input_from_user)

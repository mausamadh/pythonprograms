'''
Write a Python program to get a string from a given string where all
occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
'''
def change_occurence(given_string):
    new_string = given_string[0]
    for index in range(1,len(given_string)):

        if given_string[0]==given_string[index]:
            new_string+="$"
        else:
            new_string+=given_string[index]
        
    return new_string

try_this = change_occurence("someonesaidheispythonic")
print(try_this)
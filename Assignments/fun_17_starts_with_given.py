'''
Write a Python program to find if a given string starts with a given character
using Lambda.
'''
given_str = lambda string,char : string.startswith(char)

print(given_str("hello world",'He'))
print(given_str("hello world",'he'))
print(given_str("Greetings friends",'Greet'))
'''
Write a Python program to count the number of characters (character
frequency) in a string. Sample String : google.com'
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
'''

def count_character(hello):
    D = dict()
    for i in range(len(hello)):
        D[hello[i]]=hello.count(hello[i])
    print(D)
count_character("google.com")
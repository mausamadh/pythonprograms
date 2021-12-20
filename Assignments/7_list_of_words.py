'''
Write a Python function that takes a list of words and returns the length of the
longest one.
'''

def longest_word(list_of_words):
    max_length = 0
    for word in list_of_words:
        if len(word)>max_length:
            max_length =  len(word)
    return max_length

my_words = ['hello','my','anything','i']
longest = longest_word(my_words)
print(longest)

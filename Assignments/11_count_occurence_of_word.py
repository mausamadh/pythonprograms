'''
Write a Python program to count the occurrences of each word in a given
sentence.
'''

def count_word(sentence):
    D = dict()
    for i in range(len(sentence)):
        D[sentence[i]]=sentence.count(sentence[i])
    print(D)
my_word_list = ['this','is','my','world','this','is','my','world']
count_word(my_word_list)
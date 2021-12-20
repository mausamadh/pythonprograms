'''
Write a Python function to insert a string in the middle of a string.
Sample function and result :
insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
'''
def insert_sting_middle(string, string_to_add):
    return string[:int(len(string)/2):]+string_to_add+string[int(len(string)/2)::]

print(insert_sting_middle('{{}}', 'PHP'))
print(insert_sting_middle('[[]]<<>>', 'Python'))
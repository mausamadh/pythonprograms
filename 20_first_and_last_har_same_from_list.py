'''
20. Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given list of
strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
'''

def cout_strings(given_list):
    count = 0
    for index in range(len(given_list)):
        if len(given_list[index])>1:
            item = given_list[index]
            if item[0]==item[len(item)-1]:
                count+=1
    return count

Sample_List = ['abc', 'xyz', 'aba', '1221']

result = cout_strings(Sample_List)
print(result)


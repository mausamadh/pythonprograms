'''
Write a Python function to find the Max of three numbers.
'''


a = eval(input("enter digit:"))
b = eval(input("enter digit:"))
c = eval(input("enter digit:"))
def max_of_two(first,second):
    if first > second:
        return first
    else:
        return second

def max_of_three(first,second,third):
    maxim= max_of_two(first,second)
    result = max_of_two(maxim,third)
    return result

print(max_of_three(a,b,c))

    
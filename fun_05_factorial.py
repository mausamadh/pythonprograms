'''
Write a Python function to calculate the factorial of a number (a non-negative
integer). The function accepts the number as an argument.
'''

def fact(number:int):
    result=1
    if number==0:
        return result
    else:
        result = number * fact(number-1)
        

    return result


print(fact(3))


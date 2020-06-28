'''
Write a Python function to check whether a number is in a given range.
'''
def check_range(number,start,end):
    if number in range(start,end):
        return True
    else:
        return False

print(check_range(10,1,10)) #since range is exclusive so 
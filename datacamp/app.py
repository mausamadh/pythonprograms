def closetozero(num):
    if len(num) == 0:
        return 0
    closest = num[0]
    for i in range(0, len(num), 1):
        numb = num[i]
        absnumb = abs(numb)
        absclose = abs(closest)
        if absnumb < absclose:
            closest = numb
        elif absnumb == absclose and closest < 0:
            closest = numb
    return closest


a = int(input())

# arr=[list(map(int,input().split())) for _ in range(a)]
arr = list(map(int, input().split()))[:a]
ab = closetozero(arr)
print(ab)


"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""


def closetozero(num):
    if len(num) == 0:
        return 0
    closest = num[0]
    for i in range(0, len(num), 1):
        numb = num[i]
        absnumb = abs(numb)
        absclose = abs(closest)
        if absnumb < absclose:
            closest = numb
        elif absnumb == absclose and closest < 0:
            closest = numb
    return closest


# Write your code here
a = int(input())

arr = list(map(int, input().split()))[:a]
mi = closetozero(arr)
if arr.count(mi) > 1:
    ma = max(arr)
    print(ma)
else:
    print(mi)

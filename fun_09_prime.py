'''
Write a Python function that takes a number as a parameter and check the
number is prime or not.
Note : A prime number (or a prime) is a natural number greater than 1 and that
has no positive divisors other than 1 and itself.
'''

def prime(number:int):
    if number>0:
        msg='prime'
        for num in range(2,int(number/2)+1):
            if number%num!=0:
                msg = "prime"
            else:
                msg='not prime'
                return msg
    return msg

print(prime(4))
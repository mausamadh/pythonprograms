'''
19. Write a Python program to create Fibonacci series upto n using Lambda.
'''
'''
def fibo(n):
    if n <= 1:
       return n
    else:
       return(fibo(n-1) + fibo(n-2))
'''

squares = map(lambda x: x*squares(x-1),range(x))
print(list(squares))
'''
def horse(mask):
    horse = mask
    def mask(horse):
        return horse
    return horse(mask)

mask = lambda horse: horse(2)

horse(mask)

'''
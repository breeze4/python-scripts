#2 http://projecteuler.net/problem=2

def fib():

    n = 4000000

    fibs = [0]
    
    a, b = 0, 1

    while b < n:
        if b % 2 == 0:
            fibs.append(b)
        a, b = b, a+b

    print sum(fibs)

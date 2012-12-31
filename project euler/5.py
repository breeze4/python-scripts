#http://projecteuler.net/problem=5

#reduce accumulates values in x to be acted on by lambda
def factorial(n):return reduce(lambda x,y:x*y,range(1,n+1))

def prime_sieve(n):
    from array import array
    import math
    a = array('i', (1 for i in range(0,n)))

    for i in range(2, int(math.ceil(math.sqrt(n)))):
        if a[i] == 1:
           for j in range(i*i, n, i):
               a[j] = 0

    primes = []
    for x in range(2, len(a)):
        if a[x] == 1:
            primes.append(x)
    return primes
    

def prime(n):
    #n = 120
    
    if n == 1: return [1]
    primes = prime_sieve(int(n**0.5) + 1)
    prime_factors = []
 
    for p in primes:
        if p*p > n: break
        while n % p == 0:
            prime_factors.append(p)
            n //= p
    if n > 1: prime_factors.append(n)

    return prime_factors

def evendiv():
    num = factorial(10)

    
    

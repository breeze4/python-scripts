#http://www.reddit.com/r/dailyprogrammer/comments/wa0mc/792012_challenge_74_easy/

def zeck(n):
    
    #n = 3**15
    print n

    fibs = [0]
    z = []
    a, b = 0, 1

    while b < n:
        fibs.append(b)
        a, b = b, a+b

    x = n
    check = 0
    while x >= 0 and len(fibs) != 0:
        if sum(z)+fibs[-1] == n:
            z.append(fibs[-1])
            break
        elif sum(z)+fibs[-1] < n:
            z.append(fibs[-1])
            x = sum(z)
            fibs.pop()
            fibs.pop()
        elif sum(z)+fibs[-1] > n:
            fibs.pop()

    print "zeck:", z
    print sum(z)

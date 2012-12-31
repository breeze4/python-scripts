#http://www.reddit.com/r/dailyprogrammer/comments/v89c4/6182012_challenge_66_easy/

def rn(x, y):
    roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

    if len(y) >= len(x):
        length = len(x)
    else: length = len(y)
    
    for i in range(0,length-1):
        if roman.index(y[i]) > roman.index(x[i]):
            #print "y is greater"
            return True
        elif roman.index(y[i]) < roman.index(x[i]):
            #print "y is less"
            return False
        elif roman.index(y[i]) == roman.index(x[i]):
            #print "y is equal"
            
    return False

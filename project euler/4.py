#http://projecteuler.net/problem=4

def pali():

    x,y,largest = 999,999,0
    
    while (x >= 100 and y >= 100):
        
        while (x >= 100 and y >= 100):
            if (str(x*y) == str(x*y)[::-1]) and (x*y > largest):
                largest = x*y
                break
            else: y -= 1
                
        if (str(x*y) == str(x*y)[::-1]) and (x*y > largest):
            largest = x*y
            break
        x -= 1
        y = 999
            
    return largest

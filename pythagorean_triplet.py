#http://www.reddit.com/r/dailyprogrammer/comments/vx3bk/722012_challenge_71_easy/

def ptrip():
    for x in range(1,504):
        for y in range (x,504):
                if x*x + y*y == (504-x-y)*(504-x-y):
                    print x,y,504-x-y

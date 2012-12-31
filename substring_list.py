#http://www.reddit.com/r/dailyprogrammer/comments/x8rl8/7272012_challenge_82_easy_substring_list/

def subs(n):
    global ans
    ans = []
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','q','p','r','s','t','u','v','w','x','y','z']
    generate(1, alpha[0:n])
    #print reduce(lambda x,y:x+y,range(1,n+1))
    print ans

def generate(length, alpha):
    global ans

    if length == len(alpha):
        ans.append(alpha[-1])
        return
    elif length >= 1 :

        for i in range(length-1, len(alpha), 1):
            string = ""
            for x in range(i,length-2,-1):
                string += alpha[x]
            ans.append(string[::-1])
            
        generate(length + 1, alpha)

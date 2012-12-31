#http://www.reddit.com/r/dailyprogrammer/comments/wn3ld/7162012_challenge_77_easy_enumerating_morse_code/

def generate(x, num, count):
    global answers

    if sum(count) == num:
        #print "answer1: ", count
        return count
    elif (num - sum(count)- x) == -1:
        count.append(1)
        #print "answer2: ", count
        return count
    elif sum(count) <= num-1:
        branch1, branch2 = count[:], count[:]
        branch1.append(2)
        branch2.append(1)
        answers1 = generate(2, num, branch1)
        if answers1 != None:
            answers.append(answers1)
        answers2 = generate(1, num, branch2)
        if answers2 != None:
            answers.append(answers2)
    

def morse():
    n = 10
    
    a, k = 0, 1
    x=0
    while x < n: #fibonacci to find the number of strings
        a, k = k, a + k
        x = x+1

    global answers
    answers = []
    c = []
    #k contains the number of strings to generate
    generate(2, n, c)

    outputstrings = []
    
    for x in answers:
        phrase = ""
        for i in x:
            if i == 2:
                phrase = phrase + "-"
            elif i == 1:
                phrase = phrase + "."
        #rint phrase
        outputstrings.append(phrase)
    print outputstrings

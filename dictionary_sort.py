#http://www.reddit.com/r/dailyprogrammer/comments/vsv3g/6292012_challenge_70_easy/



def read():
    import sys
    print sys.argv
    p = sys.arg[2]
    rawwords, allwords, sortedwords = [], [], []
    wordcount = {}
    
    with open(sys.arg[1]) as f:
        rawwords = f.read().split()
        
    for word in rawwords:
        stripped_word = word.strip('|;:.,!$?\n')
        stripped_word = stripped_word.lower()
        allwords.append(stripped_word)
    
    for w in allwords:
        if w in wordcount:
            c = wordcount.get(w)
            wordcount[w]=c+1
        else:
            wordcount[w]=1

    import operator
    sortedwords =  sorted(wordcount.iteritems(), key=operator.itemgetter(1), reverse=True)
    print sortedwords[0:p]
    

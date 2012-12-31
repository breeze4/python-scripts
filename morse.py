#http://www.reddit.com/r/dailyprogrammer/comments/pr2xr/2152012_challenge_7_easy/

def morse(code):
    #code = ".... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. / --. --- --- -.. / .-.. ..- -.-. -.- / --- -. / - .... . / -.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. .- -.--"
    c = code.split(" / ")
    #initialize the tree

    import trie2
    
    m = ".- / -... / -.-. / -.. / . / ..-. / --. / .... / .. / .--- / -.- / .-.. / -- / -. / --- / .--. / --.- / .-. / ... / - / ..- / ...- / .-- / -..- / -.-- / --.."
    m = m.split(" / ")
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    t = trie2.Trie()

    #note that range() goes to 1 less than the end number
    for x in range(0, len(m)):
        t[ m[x] ] = alpha[x]

    #
    resultString = ""
    for x in c:
        letters = x.split(" ")
        for y in letters:
            resultString = resultString + str(t.get(y))
        resultString = resultString + " "
    
    print resultString

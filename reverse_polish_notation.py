#http://www.reddit.com/r/dailyprogrammer/comments/w4l6e/762012_challenge_73_easy/     

def rpn():
        operators = ["+", "-", "*"]
        stack = []
        calc = raw_input("Please enter a string of numbers to compute in Reverse Polish Notation: ")
        s = calc.split()
        for i in s:
                if not i in operators:
                        stack.append(int(i))
                else:
                        print "s:",s
                        print "stack:",stack
                        var1 = stack.pop()
                        print "var1:",var1
                        var2 = stack.pop()
                        print "var2:", var2
                        if i == '+':
                                stack.append(var2 + var1)
                        elif i == '-':
                                stack.append(var2 - var1)
                        elif i == '*':
                                stack.append(var2 * var1)
        return stack[0]

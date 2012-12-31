#http://www.reddit.com/r/dailyprogrammer/comments/wvc21/7182012_challenge_79_easy_counting_in_steps/

def step_count(a, b, steps):
    #a = 18.75
    #b = -22.00
    #steps = 5
    step_val = (a - b) / (steps-1)
    print "step value: ", (a - b) / (steps-1)
    step_list = [a]
    for x in range(1, steps-1):
        step_list.append(step_list[x-1] - step_val)
    step_list.append(b)
    print step_list

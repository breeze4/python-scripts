#http://www.reddit.com/r/dailyprogrammer/comments/xilfu/812012_challenge_84_easy_searching_text_adventure/

def game():
    print "welcome to the shitty adventure game"
    print "the commands available to you are: look, north, south, east, west"
    print "you will be given a compass reading after each action"

    player_x, player_y = 0,0
    
    win = 0

    while win == 0:
        player_x, player_y = takeInput(player_x, player_y)
        if hasWon(player_x, player_y) == 1:
            win = 1
            print "you've won, fuck yeah"
            
    

def takeInput(player_x, player_y):
    command = raw_input("What would you like to do? Enter a command: ")
    if command == "look":
        lookAround(player_x, player_y)
    elif command.lower() == "north":
        player_x += 1
    elif command.lower() == "south":
        player_x -= 1
    elif command.lower() == "west":
        player_y += 1
    elif command.lower() == "east":
        player_y -= 1
    else:
        print "you are stupid, try again"
    print         
    return player_x, player_y    


def hasWon(player_x, player_y):
    prize_x, prize_y = 1, 1
    import math
    compass = math.sqrt((prize_x - player_x)**2 + (prize_y - player_y)**2)
    if player_x == prize_x and player_y == prize_y:
        return 1
    else:
        #prints the first 3 digits of the number, guaranteed to be a float
        print "you are approximately this far from the prize: ", str(compass)[0:3]
        return 0

def lookAround(player_x, player_y):
    print "pretty boring around here"

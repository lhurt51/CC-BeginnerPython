#Liam Hurt's Python Homework 4
#Python v2.7.10
#11/18/18

import random

#Checks for an enter/return or a q
def check_string_input():
    while True:
        inputVal = raw_input("Return or Enter to continue, q to exit  >")
        if inputVal.lower() == "q":
            return "e"
        elif not inputVal.strip() or inputVal.strip() == "":
            return "c"
        else:
            print "Please only input enter/return or q!"

#Main dice game loop
def game_loop():
    rollCount = 0
    doublesCount = 0
    
    while True:
        if check_string_input() == "e":
            break
        rollCount += 1
        roll1 = dice_roll()
        roll2 = dice_roll()
        print "Round #" + str(rollCount) + " You rolled a " + str(roll1) + " and a " + str(roll2)
        if roll1 == roll2:
            print "      DOUBLES!"
            doublesCount += 1
            print "That is time #" + str(doublesCount) + " that you rolled doubles. " + str((float(doublesCount) / float(rollCount)) * 100) + "%"
    print "Ok, bye!"

#Function to return a random dice roll
def dice_roll():
    return random.randint(1,6)

#Running the game loop
game_loop()

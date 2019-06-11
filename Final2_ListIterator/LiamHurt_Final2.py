#Liam Hurt's Final #2
#Python v3.7.1
#Date: 12/13/18

#List iterator

#Importing random
import random

#List to iterate through
LST_ITR = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

#Function to return the next/previous index
def iterateList(index, step):
    if step > 0:
        index += 1
        if index >= len(LST_ITR):
            index = 0
        return index
    elif step < 0:
        index -= 1
        if index < 0:
            index = len(LST_ITR) - 1
        return index
    else:
        return -1

#Main loop to ask the user for input and print
def inputLoop():
    index = LST_ITR.index(random.choice(LST_ITR))
    while True:
        print("Current selection is: ", LST_ITR[index])
        val = str(input('Press p for previous, n for next, anything else to quit:  '))
        if val.lower() == 'p':
            index = iterateList(index, -1)
        elif val.lower() == 'n':
            index = iterateList(index, 1)
        else:
            break
    print("Goodbye")

#Calling the main list iterator loop
inputLoop()

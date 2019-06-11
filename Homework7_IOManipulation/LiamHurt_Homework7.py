#Liam Hurt's Homework #7
#Python v3.7.1
#Date: 12/09/18

#Importing from random
import random
#Importing functions from my read write file
from FileReadWrite import *

#File path constant
High_Score_File = 'HighScores.txt'
#High Score Length Constant
N_High_Scores = 5

#A check to see if the user wants to continue playing
def checkValue(val):
    if val.strip().lower() == "q" or val.strip().lower() == "quit":
        print("Thanks for playing")
        return False
    return True

#Creating a default array of zeros
def getDefArray():
    return [0] * N_High_Scores

#A function to print the results of the new list
def printList(nList):
    print("High scores list is: ")
    for n in nList:
        print("   ", n)

#A function to write my high scores to a file
def setUpFile(highScores, file):
    data = ''
    highScores.sort()
    for score in highScores:
        data += str(score) + '\n'
    writeFile(file, data)

#A func to read a file and obtain a list
def getHighScores(file):
    data = readFile(file).split('\n')
    data.pop()
    data = list(map(lambda v: int(v), data))
    return data

#To determin if there is already a file or not
def getHighScoreList(file):
    if not fileExists(file):
        setUpFile(getDefArray(), file)
    return getHighScores(file)

#Determins whether or not the file should be updated
def updateList(file, val, highScores):
    for score in highScores:
        if val > score:
            if (val > highScores[N_High_Scores - 1]):
                print("Wow, a new all time high score!")
            else:
                print("That score gets on the high scores list")
            highScores.remove(score)
            highScores.append(val)
            setUpFile(highScores, file)
            break
    return highScores

#Simulates a roll of our fake game
def simulateRoll():
    score = random.randrange(1, 101)
    print("Your score for this round is:", score)
    printList(updateList(High_Score_File, score, getHighScoreList(High_Score_File)))

#The main game loop
def gameLoop(prompt):
    while True:
        simulateRoll()
        print()
        val =  input(prompt)
        if not checkValue(val):
            break
        print()

gameLoop("Enter q/quit to exit the game > ")

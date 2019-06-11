#File Read Write Functions
#Python v3.7.1
#Date: 12/09/18

#Importing the operating system for file handling functions
import os

#Checks to see if a file exists
def fileExists(filePath):
    return os.path.exists(filePath)

#Reads from a specified file
def readFile(filePath):
    data = ''
    if not fileExists(filePath):
        print('The file,', filePath, 'does not exist - cannot read it.')
    else:
        fileHandle = open(filePath, 'r')
        data = fileHandle.read()
        fileHandle.close()
    return data

#Write to a specified file
def writeFile(filePath, textToWrite):
    fileHandle = open(filePath, 'w')
    fileHandle.write(textToWrite)
    fileHandle.close()

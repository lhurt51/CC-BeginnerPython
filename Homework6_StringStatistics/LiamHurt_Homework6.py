#Liam Hurt's Homework #6
#Python v3.7.1
#Date: 11/28/18

#Creating an alphabet constant so I can quickly check input against it
ALPHABET = "abcdefghijklmnopqrstuvwxyz"

#A validation check to make sure the user entered a int/float or nothing
def check_value(val):
    try:
        verify = str(val)
    except ValueError:
        print("WARNING: Please only input strings.")
        print()
        return False
    return True

#A function to ask the user for values and validate the input
def ask_for_value(prompt):
    while True:
        val = input(prompt)
        if check_value(val):
            return str(val)

#Prints the letters that weren't used in the phrase
def print_unused_letters(letters):
    print()
    print("There were none of the following letters found:")
    for letter in letters:
        print(" " + letter)

#Returns an array that is assigned to the user input
def ask_for_phrase():
    unusedLetters = []
    userVal = ask_for_value('Please enter a phrase: ').lower()
    for letter in ALPHABET:
        amount = userVal.count(letter)
        if amount == 1:
            print("There is only 1", letter)
        elif amount >= 2:
            print("There are", amount, "of the letter", letter)
        else:
            unusedLetters.append(letter)
    print_unused_letters(unusedLetters)

#Calling the main function to start the program
ask_for_phrase()

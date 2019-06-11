#Liam Hurt's Homework #5
#Python v3.7.1
#Date: 11/24/18

import sys

#A validation check to make sure the user entered a int/float or nothing
def check_value(val):
    try:
        verify = float(val)
    except ValueError:
        if not val.strip() or val.strip() == "":
            return True
        else:
            print("WARNING: Please only input integers.")
            print()
            return False
    return True

#A function to ask the user for values and validate the input
def ask_for_value(prompt):
    while True:
        val = input(prompt)
        if check_value(val):
            return val

#Returns an array that is assigned to the user input
def get_val_array():
    usersNums = []
    while True:
        userVal = ask_for_value('Please enter a number (Return/Enter when done): ')
        if not userVal.strip() or userVal.strip() == "":
            break
        usersNums.append(float(userVal))
    return usersNums

#Prints the array's stats by calculating total and average, while looking for min and max
def print_stats(values):
    total = 0.0
    minVal = sys.float_info.max
    maxVal = sys.float_info.min
    
    print("The values entered were:")
    for val in values:
        total += val
        print(str(val))
        if (val < minVal):
            minVal = val
        if (val > maxVal):
            maxVal = val
    print("Total is: " + str(total))
    print("Average value is: " + str(round(total / len(values), 11)))
    print("Min value is: " + str(minVal))
    print("Max value is: " + str(maxVal))

#The main code loop
print_stats(get_val_array())
        

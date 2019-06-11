# Liam Hurt's Final #1
#Python v3.7.1
#Date: 12/12/18

# Ticket sales

#Importing functions from my read write file
from FileReadWrite import *

FULL_PRICE = 10.00
HALF_PRICE = FULL_PRICE / 2
#Adding a constant for the file directory
SALES_SUMMARY_FILE_DIR = "SalesSummary.txt"

#Looks for a file(Creates one if not found) and reads the info
def lookForSummary():
    shouldPrint = True
    if not fileExists(SALES_SUMMARY_FILE_DIR):
        recordSummary(0, 0, 0.0)
        shouldPrint = False
    data = readFile(SALES_SUMMARY_FILE_DIR).split('\n')
    nChildTickets = int(data[0].split(':')[1])
    nAdultTickets = int(data[1].split(':')[1])
    totalSum = float(data[2].split(':')[1])
    if (shouldPrint):
        print("Total child tickets sold: " + str(nChildTickets) + "\nTotal adult tickets sold: " + str(nAdultTickets) + "\nTotal sum of all earnings: $" + str(totalSum))
    return nChildTickets, nAdultTickets, totalSum

#Write the recordings of the business data to a file
def recordSummary(nChildTickets, nAdultTickets, totalSum):
    data = "Total # of child tickets sold: " + str(nChildTickets) + '\n'
    data += "Total # of adult tickets sold: " + str(nAdultTickets) + '\n'
    data += "Total amount of income before expenses: " + str(totalSum)
    writeFile(SALES_SUMMARY_FILE_DIR, data)

# Calculate the total, based on the number of half price and full price tickets.
# If the user is a student, give a 50 cent discount for each ticket
def calculatePrice(nHalfPriceTix, nFullPriceTix, giveDiscount):
    #Calculate regular total
    total = (nHalfPriceTix * HALF_PRICE) + (nFullPriceTix * FULL_PRICE)
    if giveDiscount:
        #If theres a discount add all tickets and multiply by 0.5
         total -= 0.5 * (nHalfPriceTix + nFullPriceTix)
    return total

# Ask user to input number of child tickets, number of adult tickets,
# and if the person is a student (y/n)
# Keep asking until user enters a 0 and a 0

#Adding a base val of zero for incrementing
todaysEarnings = 0.0
#Looking for previous values stored in the file
totalChildTickets, totalAdultTickets, totalSales = lookForSummary()

while True:
    print()
    nChildTickets = input('How many child tickets do you want? ')
    nChildTickets = int(nChildTickets)
    nAdultTickets = input('How many adult tickets do you want? ')
    #Wrong variable name in the cast
    nAdultTickets = int(nAdultTickets)
    #This should be an and comparison instead of nor
    if (nChildTickets == 0) and (nAdultTickets == 0):
        break

    yesOrNo = input('Are you a student (y/n)? ')
    #Needs to be a double equals sign for comparisons
    if yesOrNo.lower() == 'y':
        isStudent = True
    else:
        isStudent = False

    #Forgot the third parameter
    thisTotal = calculatePrice(nChildTickets, nAdultTickets, isStudent)
    #The total needs to be casted before printing
    print('Your total is $' + str(thisTotal))
    
    #Recording the total child tickets sold
    totalChildTickets += nChildTickets
    #Recording the total adult tickets sold
    totalAdultTickets += nAdultTickets
    # Adding each total to the total sales value
    todaysEarnings += thisTotal

#After the loop I print the total sales
print()
print('Total of todays sales: $', todaysEarnings)
totalSales += todaysEarnings
print('Total sales: $', totalSales)
#Recording the totals
recordSummary(totalChildTickets, totalAdultTickets, totalSales)


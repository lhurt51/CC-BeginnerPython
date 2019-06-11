#Liam Hurt's Pyhton Homework 3
#Python v2.7.10
#11/8/18

#Formating the float to add another 0
def format_dollars(value):
    return "{0:.2f}".format(value)

#Checks all the digit variables to make sure they are within my parameters
def check_digit_input(prompt):
    while True:
        print 'Press enter or "" to exit the program'
        inputVal = raw_input(prompt)
        if not inputVal.strip() or inputVal.strip() == "":
            print "Exiting the program"
            return "E"
        try:
           val = float(inputVal)
        except ValueError:
            print "Please only input numbers!"
            continue
            
        validation = check_string_input(inputVal)
        if validation == "E":
            print "Exiting the program"
            return "E"
        elif validation.lower() == "y":
            return inputVal.strip()
        else:
            print "Please re enter the correct value"
            
#Checks for a y or n or empty to verify your last entry
def check_string_input(value):
    while True:
        inputVal = raw_input("Is " + value + " the correct amount? Please enter y or n: ")
        if not inputVal.strip() or inputVal.strip() == "":
            return "E"
        if not isinstance(inputVal, basestring) or (inputVal.lower() != "n" and inputVal.lower() != "y"):
            print "Please only input y or n!"
            continue
        return inputVal

#Runs the loop to ask for user input
def run_calc_pay_loop():
    i = 4
    while True:
        rph = check_digit_input("Please enter the employee #" + str(i) + "'s rate per hour: ")
        try:
            val = float(rph)
        except ValueError:
            break
        noh = check_digit_input("Please enter the employee #" + str(i) + "'s number of hours: ")
        try:
            val = float(noh)
        except ValueError:
            break
        print "Employee #" + str(i) + " worked for " + str(noh) + " hours at a rate of " + format_dollars(float(rph)) + "$ per hour for a total of " + format_dollars(calculate_pay(float(rph), float(noh))) + "$"
        i += 1
#Constants
REG_HRS = 40
OVERTIME_HRS = 20
DOUBLE_HRS = 60
#Calculating the pay or an employee
def calculate_pay(ratePerHr, nOfHrs):
    if nOfHrs > REG_HRS:
        pay = ratePerHr * REG_HRS
        overtimeRate = ratePerHr * 1.5
        if nOfHrs > DOUBLE_HRS:
            doubleRate = ratePerHr * 2
            pay += (overtimeRate * OVERTIME_HRS) + (doubleRate * (nOfHrs - DOUBLE_HRS))
        else:
            pay += overtimeRate * (nOfHrs - REG_HRS)
    else:
        pay = nOfHrs * ratePerHr
    return pay

print "Employee #1 worked for 20 hours at a rate of 30.00$ per hour for a total of " + format_dollars(calculate_pay(30, 20)) + "$"
print "Employee #2 worked for 50 hours at a rate of 15.50$ per hour for a total of " + format_dollars(calculate_pay(15.50, 50)) + "$"
print "Employee #3 worked for 70.25 hours at a rate of 11.00$ per hour for a total of " + format_dollars(calculate_pay(11, 70.25)) + "$"

run_calc_pay_loop()

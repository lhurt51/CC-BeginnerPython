#Liam Hurt's Pyhton Homework 2
#Python v2.7.10
#10/30/18

#Sorry for the wrong version I am working from my mac and the hardrive is having issues.
#At the moment I am not able to download the new version.

#Formating the float to add another 0
def format_dollars(value):
    return "{0:.2f}".format(value)

#Checks all the digit variables to make sure they are within my parameters
def check_digit_input(prompt):
    while True:
        print 'Press enter or "" to exit the program'
        inputVal = raw_input(prompt)
        try:
            if not inputVal.strip() or inputVal.strip() == "":
                raise EOFError
            if not inputVal.isdigit():
                raise ValueError
            
            validation = check_string_input(inputVal)
            if validation == "E":
                raise EOFError
            elif validation.lower() == "y":
                return inputVal.strip()
            else:
                print "Please re enter the correct value"
        except ValueError:
            print "Please only input numbers!"
        except EOFError:
            print "Exiting the program"
            return "E"
            
#Checks for a y or n or empty to verify your last entry
def check_string_input(value):
    while True:
        print 'Press enter or "" to exit the program'
        inputVal = raw_input("Is " + value + " the correct amount? Please enter y or n: ")
        try:
            if not inputVal.strip() or inputVal.strip() == "":
                raise EOFError
            if not isinstance(inputVal, basestring) or (inputVal.lower() != "n" and inputVal.lower() != "y"):
                raise ValueError
        except ValueError:
            print "Please only input y or n!"
            continue
        except EOFError:
            return "E"
        return inputVal

def calculate_order_total(nOfHamburgers, nOfHotDogs, nOfMilkShakes):
    priceOfHamburgers = 3 * int(nOfHamburgers)
    priceOfHotDogs = 2 * int(nOfHotDogs)
    priceOfMilkShakes = 3 * int(nOfMilkShakes)
    subtotal = priceOfHamburgers + priceOfHotDogs + priceOfMilkShakes
    return format_dollars(subtotal * 0.1 + subtotal)

order1 = calculate_order_total(3, 2, 1)
order2 = calculate_order_total(2, 7, 3)
order3 = 0

print "Total of order #1: " + order1 + "$."
print "Total of order #2: " + order2 + "$."

hamburgers = check_digit_input("How many Hamburgers would you like?: ")
if hamburgers.isdigit():
    hotDogs = check_digit_input("How many Hot Dogs would you like?: ")
    if hotDogs.isdigit():
        milkShakes = check_digit_input("How many Milk Shakes would you like?: ")
        if milkShakes.isdigit():
            order3 = calculate_order_total(hamburgers, hotDogs, milkShakes);
            print "You ordered " + hamburgers + " hamburgers, " + hotDogs + " hot dogs, and " + milkShakes + " milk shakes."
            print "Total of order #3: " + order3 + "$."
            
print "We made a sum total of " + format_dollars(float(order1) + float(order2) + float(order3)) + "$."

#Liam Hurt's Midterm Question 1
import random
import math

SHORT_QUIPS = ["Time to save up", "Put that cash in the bank", "Keep on working hard", "Need to save more"]

def check_value(val):
    try:
        verify = int(val)
    except ValueError:
        print("Please only input integers.")
        return False
    return True

def ask_for_values(prompt):
    while True:
        val = input(prompt)
        if check_value(val):
            return int(val);

def count_change(quarters, dimes, nickels, pennies):
    total = (float(quarters) * 0.25) + (float(dimes) * 0.10) + (float(nickels) * 0.05) + (float(pennies) * 0.01)
    return round(total, 2)

while True:
    userName = input("Please enter your name(Return/Enter to quit): ")
    if not userName.strip() or userName.strip() == "":
        break
    quarters = ask_for_values("How many quarters do you have? ")
    dimes = ask_for_values("How many dimes do you have? ")
    nickels = ask_for_values("How many nickels do you have? ")
    pennies = ask_for_values("How many pennies do you have? ")
    total = count_change(quarters, dimes, nickels, pennies)
    print("All counted, " + userName + " has: $" + str(total))
    cents, dollars = math.modf(total)
    print("You have " + str(int(dollars)) + " dollars and " + str(int(cents * 100)) + " cents.")
    print(SHORT_QUIPS[random.randint(1, 4)])

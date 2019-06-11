# Liam Hurt's Python Homework 1
# Date: 10/27/2018

#Integer variables
yearOfBirth = 1998
yearIStartedCoding = 2016
currentYear = 2018
myAge = currentYear - yearOfBirth
# Floating point variables
pi = 3.14159
diameter = 5.0
radius = diameter / 2.0
circumference = 2 * pi * radius
# String variables
trueOrFalseQ1 = "I have been coding for over 4 years."
trueOrFalseQ2 = "The radius of a circle is half of the diameter."
trueOrFalseQ3 = "I started coding in Javascript, originally learning web languages and frameworks."
trueOrFalseQ4 = "You will not be able to learn other languages with just the basic knowledge of python."
#Boolean variables
trueOrFalseA1 = False
trueOrFalseA2 = True
trueOrFalseA3 = True
trueOrFalseA4 = False
#Personal arrays
#   I do know, this is not the best way of using arrays.
#   However, since you asked for 4 strings and 4 booleans I felt
#   as if I needed to type them out for full credit.
questionsList = [trueOrFalseQ1, trueOrFalseQ2, trueOrFalseQ3, trueOrFalseQ4]
booleansList = [trueOrFalseA1, trueOrFalseA2, trueOrFalseA3, trueOrFalseA4]
#   Min length acts as a limiter if one array is longer than the other
minLen = min(len(questionsList), len(booleansList))
#Printing integers
print("Hi my name is Liam")
print("By my calculations -> ( currentyear:", currentYear , "- yearOfBirth:", yearOfBirth, ")")
print("I am currently", myAge, "years old")
print("I started coding in", yearIStartedCoding, "so I have been coding for over", currentYear - yearIStartedCoding, "years")
# Printing floating point decimals
print("The value of PI is:", pi)
print("The diameter of the circle is:", diameter)
print("To find the radius we must divide the diameter in half")
print("So the radius is:", radius)
print("To find the circumference we must multiply 2 by PI then by the radius")
print("So the circumference is:", circumference)
#Printing strings and booleans
print("For my strings and booleans I decided to do a little True/False questionare:")
for i in range(minLen):
    print("True/False Q", i + 1, ":",questionsList[i],"(",booleansList[i],")")

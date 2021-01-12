
# Programming involves listing all the things that must happen to solve a problem
# When writing a program first determine step-by-step what needs to happen
# Then convert those steps into the language being Python in this situation
 
# Every language has the following
# 1. The ability to accept input and store it in many ways
# 2. The ability to output information to the screen, files, etc.
# 3. The ability to conditionally do one thing or another thing
# 4. The ability to do something multiple times
# 5. The ability to make mathematical calculations
# 6. The ability to change data
# 7. (Object Oriented Programming) Model real world objects using code
 
# ---------- Hello World ----------
 
# Ask the user to input their name and assign it to the name variable
# Variable names start with a letter or _ and then can contain numbers
# Names are case sensitive so name is not the same as Name
name = input('What is your name ')
 
# Print out Hello followed by the name they entered
print('Hello ', name)
 
# You can't use the following for variable names
# and, del, from, not, while, as, elif, global,
# or, with, assert, else, if, pass, yield, break,
# except, import, print, class, exec, in, raise,
# continue, finally, is, return, def, for, lambda,
# try
 
# Single line comments are ignored by the interpreter
'''
So are multiline comments
'''
 
# ---------- MATH ON 2 VALUES ----------
 
# Ask the user to input 2 values and store them in variables num1 and num2
# split() splits input using whitespace
num1, num2 = input('Enter 2 numbers : ').split()
 
# Convert strings into regular numbers (integers)
num1 = int(num1)
num2 = int(num2)
 
# Add the values entered and store in sum
sum = num1 + num2
 
# Subtract the values and store in difference
difference = num1 - num2
 
# Multiply the values and store in product
product = num1 * num2
 
# Divide the values and store in quotient
quotient = num1 / num2
 
# Use modulus on the values to find the remainder
remainder = num1 % num2
 
# Print your results
# format() loads the variable values in order into the {} placeholders
print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))
 
# ---------- PROBLEM : MILES TO KILOMETERS ----------
# Sample knowing that kilometers = miles * 1.60934
# Enter Miles 5
# 5 miles equals 8.0467 kilometers
 
# Ask the user to input miles and assign it to the miles variable
miles = input('Enter Miles ')
 
# Convert from string to integer
miles = int(miles)
 
# Perform calculation by multiplying 1.60934 times miles
kilometers = miles * 1.60934
 
# Print results using format()
print("{} miles equals {} kilometers".format(miles, kilometers))
 
# ---------- CALCULATOR ----------
# Receive 2 numbers separated by an operator and show a result
# Sample
# Enter Calculation: 5 * 6
# 5 * 6 = 30
 
# Store the user input of 2 numbers and an operator
num1, operator, num2 = input('Enter Calculation: ').split()
 
# Convert strings into integers
num1 = int(num1)
num2 = int(num2)
 
# If, else if (elif) and else execute different code depending on a condition
if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1+num2))
 
# If the 1st condition wasn't true check if this one is
elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1 - num2))
elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1 * num2))
elif operator == "/":
    print("{} / {} = {}".format(num1, num2, num1 / num2))
 
# If none of the above conditions were true then execute this by default
else:
    print("Use either + - * or / next time")
 
# Other conditional operators
# > : Greater than
# < : Less than
# >= : Greater than or equal to
# <= : Less than or equal to
# != : Not equal to

# ---------- IS BIRTHDAY IMPORTANT ----------
# We'll provide different output based on age
# 1 - 18 -> Important
# 21, 50, > 65 -> Important
# All others -> Not Important
 
# eval() converts a string into an integer if it meets the guidelines
age = eval(input("Enter age: "))

# Logical operators can be used to combine conditions
# and : If both are true it returns true
# or : If either are true it returns true
# not : Converts true into false and vice versa
 
# If age is both greater than or equal to 1 and less than or equal to 18 it is true
if (age >= 1) and (age <= 18):
    print("Important Birthday")
 
# If age is either 21 or 50 then it is true
elif (age == 21) or (age == 50):
    print("Important Birthday")
 
# We check if age is less than 65 and then convert true to false or vice versa
# This is the same as if we put age > 65
elif not(age < 65):
    print("Important Birthday")
else:
    print("Sorry Not Important")
 
# ---------- PROBLEM : DETERMINE GRADE ----------
# If age 5 go to kindergarten
# Ages 6 through 17 goes to grades 1 through 12
# If age is greater then 17 then say go to college
# Try to complete with 10 or less lines
 
# Ask for the age
age = eval(input("Enter age: "))

# Handle if age < 5
if age < 5:
    print("Too Young for School")
 
# Special output just for age 5
elif age == 5:
    print("Go to Kindergarten")
 
# Since a number is the result for ages 6 - 17 we can check them all
# with 1 condition
# Use calculation to limit the conditions checked
elif (age > 5) and (age <= 17):
    grade = age - 5
    print("Go to {} grade".format(grade))
 
# Handle everyone else
else:
    print("Go to College")


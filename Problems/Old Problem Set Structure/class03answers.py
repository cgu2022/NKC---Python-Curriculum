#######################################################################################
# 3.1
# using inequalities determine True or False whether 5 is less than 10
# print your answer

print(5 < 10)


#######################################################################################
# 3.2
# using inequalities determine True or False whether 10 is less than or equal to 10

print(10 <= 10)

#######################################################################################
# 3.3
# make inequalities which all evaluate to True using <=, >=, ==, !=

print(4 <= 5)
print(6 >= 2)
print(6 == 6)
print(4 != 3)

#######################################################################################
# 3.4
# make inequalities which all evaluate to False using <=, >=, ==, !=

print(4 <= 1)
print(10 >= 15)
print(5 == 2)
print(4 != 4)

# Stop here

#######################################################################################
# 3.5
# use and, or, not to combine inequalities using ()
# 1 evaluates to True using "and", 1 evaluates to False using "and"
# 1 evaluates to True using "or", 1 evaluates to False using "or"
# 1 evaluates to True using "not", 1 evaluates to False using "not"
# try to use a variety of >=, ==, !=, <=, <, >

print((5 < 10) and (2 >= 1)) # true
print((5 > 5) and (2 < 6)) # false

print((5 > 10) or (5 > 2)) # true
print((5 > 7) or (4 > 7)) # false

print(not (1 > 2)) # true
print(not (4 > 3)) # false

# Stop Here

#######################################################################################
# 3.6
# create a variable which holds True
# use an if statement with the variable to print something

var = True
if var:
    print("var must hold True")


#######################################################################################
# 3.7
# create a variable which holds False
# use an if statement and see if anything prints

var = False
if var:
    print("this won't be printed")

#######################################################################################
# 3.8
# create a variable which holds False
# make the if statement print something using that variable

var = False
if not var:
    print("not var(false) is true so this prints")


#######################################################################################
# 3.9
# create an if statement with a condition which will always be true and print something

if 5 > 0:
    print("this will always print")

if True:
    print("this will also always print")


# Stop Here

#######################################################################################
# 3.10
# use the input function to store a number in a variable

num = int(input())

#######################################################################################
# 3.11
# Ask the user for a number. (This also means take in an input.)
# Then, print out either "positive", "negative", or "neither"
# if the number is +, -, or 0

# Hint: Here's how to take in an input:
# v1 = input()
# And then don't forget casting!

num = int(input("Enter Number:"))

if num > 0:
    print("positive")
if num < 0:
    print("negative")
if num == 0:
    print("neither")

#######################################################################################
# 3.12
# modify your code from 3.11 to use elif and else statements

num = int(input("Enter Number:"))

if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("neither")



#######################################################################################
# 3.13
# use the input function to get 2 numbers stored in 2 variables
# print the sum of them

num1 = int(input())
num2 = int(input())

print(num1 + num2)


# Wait here

#######################################################################################
# 3.14
# Import the random library (you only have to do it once!) and print out a random
# number from 1 to 100

import random
rand = random.randint(1, 100)
print(rand)

#######################################################################################
# 3.15 
# Generate a random decimal between 0 and 1. If it is less than 0.5, then set the
# variable to 0.

randomDecimal = random.random()
if randomDecimal < 0.5:
    randomDecimal = 0
print(randomDecimal)


#######################################################################################
# 6.1
# Make a while loop with a counter variable which counts up to 100
# This program should print the numbers 1-100 on the terminal.

counter = 0
while counter <= 100:
    print(counter)
    counter += 1

#######################################################################################
# 6.2
# Get the input of 10 numbers using the input function and a while loop. Then take the
# average of those 10 numbers. Print the average.

total = 0
counter = 0
while counter < 10:
    total += float(input())
    counter += 1

print("Average is {}".format(total / 10))

#######################################################################################
# 6.3
# Make a while loop program which can calculate the factorial of a number. 3! means 3
# factorial. 3! = 3*2*1, 4! = 4*3*2*1, 5! = 5*4*3*2*1. You can either take the number
# to get the factorial of as an input or make it in a variable.

total = 1
number = 4
while number > 1:
    total *= number
    number -= 1

print(total)

#######################################################################################
# 6.4
# Write a program that calculates the greatest common factor(GCF) of two numbers. This
# is the largest number both numbers can be divided evenly by. To check if a certain 
# number divides another evenly, use the modulus operator(%). For example, 10 % 5 == 0,
# 4 % 2 == 0, 10 % 3 == 1, 6 % 4 == 2, 8 % 5 == 3, 100 % 20 == 0.

print("please enter num1: ")
num1 = int(input())
print("please enter num2: ")
num2 = int(input())

largest_factor = 1

# checks which number greater so don't do extra checks
# not necessary to solve problem

i = 1
if num1 <= num2:
    while i <= num1:
        if num2 % i == 0 and num1 % i == 0 and i > largest_factor:
            largest_factor = i
        i += 1
else:
    while i <= num2:
        if num1 % i == 0 and num2 % i == 0 and i > largest_factor:
            largest_factor = i
        i += 1

print("The GCF of {} and {} is {}".format(num1, num2, largest_factor))

#######################################################################################
# 6.5
# Write a program which continually asks the user for a number until they enter they
# type "stop". Once they have typed "stop" the computer should output the average
# of the numbers entered.

total = 0
number = input()
counter = 0
while number != "stop":
    total += int(number)
    number = input()
    counter += 1

if counter == 0:
    print("no average")
else:
    print("The average of the numbers is {}".format(total/counter))

#######################################################################################
# 6.6
# Using a while loop and strings, make a program which prints out a staircase with a 
# certain amount of steps. Ask the user how many steps they want using the input 
# function. For example a staircase with 2 steps would look like this:
# *
# **
# A staircase with 4 steps would look like this:
# *
# **
# ***
# ****
# Remember that you can add strings together. For example "race" + "car" = "racecar"

print("how many steps?")
steps = int(input())

string = ""
counter = 0
while counter < steps:
    string += "*"
    print(string)
    counter += 1

#######################################################################################
# 6.7
# Rock, paper, scissors is a fun and easy game.
# Rock beats scissors, paper beats rock, and scissors beats paper

# Write a program the generates a random move to go (rock, paper, or scissors)
# and then the user will enter their move but will not see the computer's guess.
# Keep playing until the player wins. Make sure to display the computer's guess every round
# 
# Use:
# "random.randint(x,y)" (Generates a random number between x - y, which include x and y)
# from "import random" to generate a random number

import random

win = False

while win == False:
    cpu = random.randint(0,2)
    print("enter a move (rock is 0, paper is 1, and scissors is 2): ")
    num1 = int(input())
    if(cpu == num1):
        print("Just a tie! Computer guessed the same!")
    elif(cpu==0 and num1 == 2) or (cpu == 1 and num1 == 0) or (cpu == 2 and num1 == 1):
        print("Sorry, CPU won this round. The computer's guess was: " + str(cpu))
    else:
        print("Congrats, you won! The computer's guess was: " + str(cpu))
        win = True

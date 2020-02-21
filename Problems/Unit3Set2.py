#######################################################################################
# 6.1
# Make a while loop with a counter variable which counts up to 100
# This program should print the numbers 1-100 on the terminal.


#######################################################################################
# 6.2
# Get the input of 10 numbers using the input function and a while loop. Then take the
# average of those 10 numbers. Print the average.

#######################################################################################
# 6.3
# Make a while loop program which can calculate the factorial of a number. 3! means 3
# factorial. 3! = 3*2*1, 4! = 4*3*2*1, 5! = 5*4*3*2*1. You can either take the number
# to get the factorial of as an input or make it in a variable.

#######################################################################################
# 6.4
# Write a program that calculates the greatest common factor(GCF) of two numbers. This
# is the largest number both numbers can be divided evenly by. To check if a certain 
# number divides another evenly, use the modulus operator(%). For example, 10 % 5 == 0,
# 4 % 2 == 0, 10 % 3 == 1, 6 % 4 == 2, 8 % 5 == 3, 100 % 20 == 0.

#######################################################################################
# 6.5
# Write a program which continually asks the user for a number until they enter they
# type "stop". Once they have typed "stop" the computer should output the average
# of the numbers entered.

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

#######################################################################################
# 6.7
# Get 2 numbers from the user and create a all the possible multiplication expressions
# for numbers within those ranges. For example if the numbers were 1 and 5 some examples
# would be 1x1=1, 1x2=2, 1x3=3, 1x4=4, 1x5=5
# Use a double for loop for this problem.
# The example below is for numbers 5 and 5
# 1x1=1   1x2=2   1x3=3   1x4=4   1x5=5
# 2x1=2   2x2=4   2x3=6   2x4=8   2x5=10
# 3x1=3   3x2=6   3x3=9   3x4=12  3x5=15
# 4x1=4   4x2=8   4x3=12  4x4=16  4x5=20
# 5x1=5   5x2=10  5x3=15  5x4=20  5x5=25

#######################################################################################
# 6.8
# Rock, paper, scissors is a fun and easy game.
# Rock beats scissors, paper beats rock, and scissors beats paper

# Write a program the generates a random move to go (rock, paper, or scissors)
# and then the user will enter their move but will not see the computer's guess.
# Keep playing until the player wins. Make sure to display the computer's guess every round
# 
# Use:
# First write "import random" on the top of your program, before anything else
# "random.randint(x,y)" generates a random number between x - y, which include x and y
# So, x = random.randint(0,10) sets x to a random number between 0 - 10, inclusive
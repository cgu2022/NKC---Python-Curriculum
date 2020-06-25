'''
These are a set of mini-projects!
'''

#IMPORTANT:
# Remember: use int() to convert a string into an integer
# and use float() to convert a string into a decimal

#######################################################################################
# 4.1
# Write a program that uses the string variable below and then prompts the user for a string. 
# If the strings match, print true. If not, print false. Then, do the same with a number. 

thing = "Hello"

# Step 1: Take in an input
# Remeber: It's as simple as defining a variable and making it equal to input().
# For example: v1 = input()


# Step 2: Make your if/else statements. First identify when to print "True" and when to print "False". This will be your if statement's condition.
# Then translate it into code.


#######################################################################################
# 4.2
# Write a program that takes in three numbers using the input function and then prints 
# the largest number.



#######################################################################################
# 4.3
# Write a program that takes in a grade and calculates if it is A, B, C, D, or F
# Extra: Add plus and minuses. Fs do not need + or -.
# Extra2: This program will support decimals.


#######################################################################################
# 4.4
# You are going to make a Magic 8 ball. You ask it a question, and it gives you an answer
# Write a program that takes in a question, and replies with an answer.
# You must have at least 5 responses, generated randomly (hint: use the random function)

# ex: User: Should I listen to the lecture or no?
#    Output: Yes
'''
import random

x = input("Enter Question: ")
number = random.randint(1,5) # number will equal a random number between 1-5
'''


   
#######################################################################################
# 4.5
# A straight in poker (a card game) is defined when 5 cards are aligned consecutively in 
# ascending order (0, 1, 2, 3, 4) but not (8, 9, 10, 0, 1), nor (0, 2, 1, 3, 4).
# Cards are from 0-10

# Write a program prompts the user for 5 numbers, and then determines if they are a 
# straight. You do not need to make sure the number stays within bounds.

# Bonus: if the user enters "J" for a card, it means 11



#######################################################################################
# 4.6
# Write a program that prompts the user for an operation
# (addition, subtraction, multiplication, or division) for (0-3)
#     0          1              2               3
# and then prompts for 2 numbers. Then, display the result.

# e.g. Enter a number: 3 (for division)
#   Enter num1: 50
#   Enter num2: 10
#   5

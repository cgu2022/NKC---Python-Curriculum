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

n2 = input()

# Step 2: Make your if/else statements. First identify when to print "True" and when to print "False". This will be your if statement's condition.
# Then translate it into code.

if n2==thing:
    print("True")
else: 
    print("False")

#######################################################################################
# 4.2
# Write a program that takes in three numbers using the input function and then prints 
# the largest number.

print("Enter number 1:")
n1 = input()
print("Enter number 2:")
n2 = input()
print("Enter number 3:")
n3 = input()

if(n1 >= n2 and n1>=n3):
    print(n1, "is the largest")
elif(n2 >= n1 and n2>=n3):
    print(n1, "is the largest")
elif(n3 >= n2 and n3>=n1):
    print(n1, "is the largest")

#######################################################################################
# 4.3
# Write a program that takes in a grade and calculates if it is A, B, C, D, or F
# Extra: Add plus and minuses. Fs do not need + or -.
# Extra2: This program will support decimals.

grade = float(input("Enter a grade:"))
decimal = grade - float(int(grade))
if decimal >= 0.5:
	grade = float(int(grade)) + 1.0
else:
	grade = float(int(grade))

if(grade>=90):
     print('A', end='')
     grade -= 90
elif(grade>=80):
    print('B', end='')
    grade -= 80
elif(grade>=70):
    print('C', end='')
    grade -= 70
elif(grade>=60):
    print('D', end='')
    grade -= 60
else:
    print('F')
    grade = -1

if(grade!=-1):
    if(grade>=7):
        print('+')
    elif(grade>=3):
        print('')
    else:
        print('-')

#######################################################################################
# 4.4
# You are going to make a Magic 8 ball. You ask it a question, and it gives you an answer
# Write a program that takes in a question, and replies with an answer.
# You must have at least 5 responses, generated randomly (hint: use the random function)

# ex: User: Should I listen to the lecture or no?
#    Output: Yes

import random

x = input("Enter Question: ")
number = random.randint(1,5) # number will equal a random number between 1-5


if(number == 1):
  print("Yes")
if(number == 2):
  print("No")
if(number == 3):
  print("Maybe")
if(number == 4):
  print("IDK")
if(number == 5):
  print("IDC")

   
#######################################################################################
# 4.5
# A straight in poker (a card game) is defined when 5 cards are aligned consecutively in 
# ascending order (0, 1, 2, 3, 4) but not (8, 9, 10, 0, 1), nor (0, 2, 1, 3, 4).
# Cards are from 0-10

# Write a program prompts the user for 5 numbers, and then determines if they are a 
# straight. You do not need to make sure the number stays within bounds.

# Bonus: if the user enters "J" for a card, it means 11

s1 = input("Enter card:")
s2 = input("Enter card:")
s3 = input("Enter card:")
s4 = input("Enter card:")
s5 = input("Enter card:")

if(s1=='J'):
    n1 = 11
else:
    n1 = int(s1)
if(s2=='J'):
    n2 = 11
else:
    n2 = int(s2)
if(s3=='J'):
    n3 = 11
else:
    n3 = int(s3)
if(s4=='J'):
    n4 = 11
else:
    n4 = int(s4)
if(s5=='J'):
    n5 = 11
else:
    n5 = int(s5)

if(n1+1 == n2 and n2+1 == n3 and n3+1 == n4 and n4+1 == n5):
    print("Straight")
else:
    print("Not a straight")

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

op = int(input("Enter operation (0-3):"))
n1 = int(input("First Number:"))
n2 = int(input("Second Number:"))

if(op==0):
    print(n1+n2)
if(op==1):
    print(n1-n2)
if(op==2):
    print(n1*n2)
if(op==3):
    print(n1/n2)

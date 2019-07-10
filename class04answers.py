#######################################################################################
# 4.1
# Write a program that uses a string variable and then prompts the user for a string. 
# If the strings match, print true. If not, print false. Then, do the same with a number. 

thing = "Hello"
n2 = input()
if n2==thing:
    print("True")
else: 
    print("False")
thing2 = 21
n = int(input())
if(n==thing2):
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
# Extra: Added plus and minuses. Fs do not need + or -.
# This program will support decimals.
# Use round() to round the number. Although the function will round 1.5 down, 
# for our purposes, round it up.

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
# A straight in poker(a card game) is defined when 5 cards are aligned consecutively in 
# ascending order (0, 1, 2, 3, 4) but not (8, 9, 10, 0, 1), nor (0, 2, 1, 3, 4).
# Cards are from 0-10, and a J is 11.

# Write a program prompts the user for 5 numbers, and then determines if they are a 
# straight. You do not need to make sure the number stays within bounds.


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
# 4.5
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

#######################################################################################
# 4.6
# Triangles have exactly three sides. If a triangle has three equal sides it is called 
# an equilateral triangle. If a triangle has exactly two equal sides it is called an 
# isosceles triangle. If a triangle has three unequal sides it is called a scalene triangle.
# The sides of a triangle must have a certain relationship to one another in order for 
# them to form a valid triangle. The relationship is that the sum of any two sides must 
# be strictly greater than the third side. Sides must be a whole number.

# Write a program that prompts the user to enter some integer values for the 3 sides 
# of a triangle and then displays the values and the type of triangle they represent.
# If the user enters values that do not make a valid triangle, or if any values are not 
# greater than zero, then the program will invalidate that triangle by saying: 
# “This isn’t a real triangle!”  

#gathering user input
print("Enter a side 1:")
s1 = int(input())
print("Enter a side 2:")
s2 = int(input())
print("Enter a side 3:")
s3 = int(input())

#decision-making
if s1+s2<s3 or s1+s3<s2 or s2+s3<s1 or s1<=0 or s2<=0 or s3<=0:
    print("This isn't a real triangle!")
elif s1==s2 and s2==s3 :
    print("This is an equilateral triangle!")
elif (s1==s2 and s2!=s3) or (s1!=s2 and s2==s3):
    print("This is a isoceles triangle!")
else:
    print("This is a scalene triangle")

#######################################################################################
# 4.7
# Write a program to solve quadratic equations (use if, else if and else).
# Essentially, ask the user for a, b, and c
# If there are no real solutions, just say "No Real Solutions!"
# And remember, to determine if the solutions are real, just make sure the discriminate 
# (b^2 - 4*a*c) is greater than or equal to zero. 
# useful math functions:
# math.pow - get powers of numbers - ex: math.pow(2, 3) = 8
# math.sqrt - get square root of number - ex: math.sqrt(4) = 2

import math

print("Enter a:")
a = float(input())
print("Enter b:")
b = float(input())
print("Enter c:")
c = float(input())

result = math.pow(b, 2) - 4 * a * c

if result > 0:
    r1 = (-b + math.sqrt(result)) / (2 * a)
    r2 = (-b - math.sqrt(result)) / (2 * a)
    print("The roots are ", r1 , " and " , r2)
elif result == 0:
    r1 = -b / (2 * a)
    print ("The root is ", r1)
else:
    print("The equation has no real roots.")


#######################################################################################
# 8.1
# Write code with a while loop and for loop which do the same thing.

counter = 0
while counter < 10:
    print(counter)
    counter += 1

for i in range(0, 10):
    print(i)

#######################################################################################
# 8.2
# Write a program that manually does addition. So, when a user enters 2 numbers
# (e.g. 5, 6), instead of doing 5*6, use a for loop to calculate 5 times 6 (repeated addition).
print("Enter number1: ")
n1 = int(input())
print("Enter number2: ")
n2 = int(input())
total = 0

for i in range(0, n2):
    total += n1
print(total)

#######################################################################################
# 8.3
# Use a for loop to create a power calculator. For example 3 to the third power is 27,
# 2 to the fourth power is 16, 5 to the second power(squared) is 25. Take input from
# the user to get the number and the power that number should be raised to. For a
# challenge you can also try to deal with negative powers.

print("Enter the number: ")
number = int(input())
print("Enter the power: ")
power = int(input())
answer = 1

for i in range(0, power):
    answer *= number
print("=" + str(answer))

#######################################################################################
# 8.4
# Experiment with putting a loop within a loop.


for i in range(0, 3):
    for j in range(0, 2):
        print(j)


#######################################################################################
# 8.5
# Using a for loop inside a for loop, make a program which prints out a rectangle of
# certain dimensions entered by the user. The rectangle can use * or #. You should use
# your knowledge of adding strings together to accomplish this task.


print("Enter rows: ")
length = int(input())
print("Enter cols: ")
width = int(input())

line = ""

for i in range(0, length):
    for j in range(0, width):
        line += "*"
    print(line)
    line = ""


#######################################################################################
# 8.6
# Make a for loop which asks the user for a number three times and then prints out the
# largest number the user supplies.

largest = -1
for i in range(0, 3):
    user_number = int(input())
    if i == 0:
        largest = user_number
    else:
        if largest < user_number:
            largest = user_number
    
print("The largest number is {}".format(largest))


#######################################################################################
# 8.7a
# Get 2 numbers from the user and create a all the possible multiplication expressions
# for numbers within those ranges. For example if the numbers were 1 and 5 some examples
# would be 1x1=1, 1x2=2, 1x3=3, 1x4=4, 1x5=5
# Use a double for loop for this problem.
# print it in a rectangle format - you will have to use string addition
# The example below is for numbers 5 and 5
# 1x1=1   1x2=2   1x3=3   1x4=4   1x5=5
# 2x1=2   2x2=4   2x3=6   2x4=8   2x5=10
# 3x1=3   3x2=6   3x3=9   3x4=12  3x5=15
# 4x1=4   4x2=8   4x3=12  4x4=16  4x5=20
# 5x1=5   5x2=10  5x3=15  5x4=20  5x5=25

print("enter num1: ")
num1 = int(input())
print("enter num2: ")
num2 = int(input())

line = ""

for i in range(1, num1):
    for j in range(1, num2):
        line += "{}x{}={}\t".format(i, j, i*j)
    print(line)
    line = ""

#######################################################################################
# 8.7b
# Do 8.7a but with exponents:
# Example: (6 and 4)
# 1^1=1.0          1^2=1.0         1^3=1.0         1^4=1.0
# 2^1=2.0          2^2=4.0         2^3=8.0         2^4=16.0
# 3^1=3.0          3^2=9.0         3^3=27.0        3^4=81.0
# 4^1=4.0          4^2=16.0        4^3=64.0        4^4=256.0
# 5^1=5.0          5^2=25.0        5^3=125.0       5^4=625.0
import math

print("enter num1: ")
num1 = int(input())
print("enter num2: ")
num2 = int(input())

line = ""

for i in range(1, num1):
    for j in range(1, num2):
        line += "{}^{}={} \t ".format(i, j, math.pow(i, j))
    print(line)
    line = ""

#######################################################################################
# 8.8
# they could also accomplish this using string addition
# Use a for loop to print numbers with an increasing amount of 1s. If the user enters 5
# there should be 5 ones in the last printed number.
# ex. 1, 11, 111, 1111, 11111

print("Enter amount of 1s: ")
number = int(input())
start = 1
tens = 1
for i in range(0, number):
    print(start)
    tens *= 10
    start += tens


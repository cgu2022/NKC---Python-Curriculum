####################################################
'''
Some of these projects were provided by The Pingry School!
'''
#####################################################
# Project: Area and Perimeter
# Link: https://docs.google.com/document/d/1PMkrmhMzF2TYhRymJPRXY-_-o_Y4BqyQ3XbCdv7wlgI/edit?usp=sharing

x = input("Please enter the radius of the circle: ")
x = float(x)
print("Area: " + str(3.14*x*x) + " units squared")
print("Perimeter: " + str(3.14*2*x) + " units" )

#####################################################
# Project: Color Mixer
# Link: https://docs.google.com/document/d/1FnQ2066_0KMzJ1hbQYGOX8zMb8EPLiKyZwAe5Z6CnWA/edit?folder=1pLkspS6-zT_FDWMj7ysPK7Lr2zRytZ96#

color1 = input("Enter the first primary color: ")
color2 = input("Enter the second primary color: ")
if (color1 == "red" and color2 == "blue") or (color2 == "red" and color1 == "blue"):
    print("Mixing red and blue creates purple.")
if (color1 == "red" and color2 == "yellow") or (color2 == "yellow" and color1 == "red"):
    print("Mixing red and yellow creates orange.")
if (color1 == "blue" and color2 == "yellow") or (color2 == "yellow" and color1 == "blue"):
    print("Mixing red and yellow creates green.")


#####################################################
# Project: Software Sales
# Link: https://docs.google.com/document/d/1yEPQW-OAcHlc61V8gm62CIpNMwPo3m3oZsBaG2ju6zw/edit#

num = int(input("Enter the number of packages you want to buy: "))
discount = 0
if(num >= 10 and num <= 19):
    discount = 0.1
if(num >= 20 and num <= 49):
    discount = 0.2
if(num >= 50 and num <= 99):
    discount = 0.3
if(num >= 100):
    discount = 0.4
print("Original Price: " + str(num * 99))
print("Discount: " + str(num * 99 * discount))
print("Price Charged: " + str(num * 99 - num * 99 * discount))

#####################################################
# Project: Guessing Game
# Link: https://docs.google.com/document/d/1YLCkmskcfn5ki5YqFoeIQMatbA4JhLuEBOHX2NVk438/edit?usp=sharing
# Use this to create a random number:

import random

x = int(input("Enter a number: "))
number = random.randint(1,10) # number will equal a random number between 1-10

if(x==number):
    print("Correct! The number was " + str(number))
elif(x < number):
    print("Too low, the number was " + str(number))
else:
    print("Too high, the number was " + str(number))

####################################################
# Challenge Project: Determining Triangles
# Link: https://docs.google.com/document/d/1QKels44IV7VTDcP0giYssgXJr36p5E0ORTm3-WJSbYI/edit?folder=1pLkspS6-zT_FDWMj7ysPK7Lr2zRytZ96#

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

####################################################
# Challenge Project: Quadratic Solver
# Link: https://docs.google.com/document/d/1ELNSs24xsk51lPRVtZLRRkOqkuhL_y9GozKmkDZRan8/edit?folder=1pLkspS6-zT_FDWMj7ysPK7Lr2zRytZ96#

import math

# useful math functions:
# math.pow - get powers of numbers - ex: math.pow(2, 3) = 8
# math.sqrt - get square root of number - ex: math.sqrt(4) = 2

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
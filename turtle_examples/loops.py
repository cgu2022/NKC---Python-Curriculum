# For the problems below, look at the imgur link to see the expected results for each
# problem.

#Imgur link: https://imgur.com/a/xEBjbLm
import turtle
t = turtle.Turtle()

#######################################################################################
# 1.1
# Use a for loop to create an 6 sided shape (hexagon)
# To figure out angle for turn just do 360/#sides
# for a triangle: 360/3 = 120



#######################################################################################
# 1.2
# Make a row of 5 circles with a radius of 10 spaced 10 px apart.



#######################################################################################
# 1.3
# Use a 2 for loops to create a grid of circles. The grid should use the circles from
# the previous problem. You need to make 5 rows print out.



#######################################################################################
# 1.4
# Draw a bullseye with 5 rings.



#######################################################################################
# 1.5
# An example showing how to change the turtle draw color
'''
t.color("red")
for i in range(4):
    t.forward(100)
    t.left(90)

t.color("black")
'''

#######################################################################################
# 1.6
# An example showing color filling
'''
t.color("red")
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()
'''

#######################################################################################
# 1.7
# An interesting example. Try to think about what it does before you run the code.

'''


for i in range(20):
    if i % 10 == 0:
        t.color("red")
    elif i % 9 == 0:
        t.color("green")
    elif i % 8 == 0:
        t.color("blue")
    elif i % 7 == 0:
        t.color("yellow")
    elif i % 6 == 0:
        t.color("orange")
    elif i % 5 == 0:
        t.color("purple")
    elif i % 4 == 0:
        t.color("pink")
    elif i % 3 == 0:
        t.color("black")
    elif i % 2 == 0:
        t.color("grey")
    else:
        t.color("brown")

    for i in range(4):
        t.forward(200)
        t.left(93)
    

'''


#######################################################################################
# 1.8
# Use the fill function to color the bullseye in an alternating color pattern.



#######################################################################################
# 1.9
# Create a shape similar to the one from 1.7. You don't need to change the colors.

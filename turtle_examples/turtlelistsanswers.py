import turtle
t = turtle.Turtle()


#######################################################################################
# 1.1
# Use a for loop to loop through each xy coordinate pair and draw to the screen

coords = [[12.9, 11.9],
    [21.3, 12.15],
    [14.45, 7.7],
    [17, 15.05],
    [19.75, 8.2],
    [12.9, 11.99]]

for c in coords:
    t.goto(c[0], c[1])

#######################################################################################
# 1.2
# Make a list of 4 colors and then draw a square with each side being a different color.
# Color for the turtle pen can be changed using turtle.color("red") = sets color to red
# example colors: "red", "orange", "green", "purple", "brown"
# probably more colors you can think of, but the computer will yell at you if it doesn't
# recognize the color.

c_list = ["red", "green", "orange", "blue"]

for i in range(4):
    t.color(c_list[i])
    t.forward(100)
    t.left(90)



#######################################################################################
# 1.3
# An interesting example showing how a circle is actually drawn. The circle function is 
# not magic!
'''
import time
import math

t.hideturtle()
t.speed(0)
radius = 100
angle = 0
sides = 3
increase = 30

for j in range(increase+1):
    for i in range(sides+1):
        t.goto(math.cos(angle)*radius, math.sin(angle)*radius)
        angle += 2*math.pi/sides
    sides += 1
    time.sleep(0.3)
    t.clear()
'''
#######################################################################################
# 1.4
# Draw circles with a radius of 20 at the following coordinates. Make sure the circles don't have lines
# drawn between them.

circles = [
    [0, 0],
    [100, 200],
    [300, -200],
    [-100, -100],
    [-250, 300],
    [100, 0],
    [-100, 10],
    [200, -50]
]

for c in circles:
    t.penup()
    t.goto(c[0], c[1])
    t.pendown()
    t.circle(20, 360)

#######################################################################################
# 1.5
# bonus example
'''
screen = turtle.Screen()
l = [(0, 0)]

def getxy(x, y):
	global l
	l.append((x, y))

def draw():
	global l
	for c in l:
		t.goto(c[0], c[1])

while True:
	screen.onclick(getxy)
	time.sleep(0.1)
	if len(l) > 0:
		t.penup()
		t.goto(l[-1])
		t.pendown()
		t.circle(1, 360)
	if len(l) == 50:
		draw()
		break
'''

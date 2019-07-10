import turtle
from time import sleep
import datetime

#######################################################################################
# A program which shows the coordinate system the turtle uses.

t = turtle.Turtle()
screen = turtle.Screen()

# slow mode:
# t.speed(10)


#optmizations:
t.speed(0)
screen.tracer(100, 1)
t.hideturtle()

screenx = screen.screensize()[0]
screeny = screen.screensize()[1]

def draw_bounding():
    t.penup()
    t.goto(-screenx, screeny)
    t.pendown()
    for i in range(2):
        t.forward(screenx*2)
        t.right(90)
        t.forward(screeny*2)
        t.right(90)
    t.penup()

def draw_y_axis():
    t.goto(0, -screeny)
    t.pendown()
    t.setheading(90)
    for i in range(0, int(screeny*2/10)):
        t.forward(10)
        t.goto(t.xcor()-5, t.ycor())
        t.setheading(0)
        t.forward(10)
        t.penup()
        if int(round(t.ycor())) > 10 or int(round(t.ycor())) < -10:
            if i % 2 == 0:
                t.goto(t.xcor()+3, t.ycor()-3)
                t.pendown()
                t.write(str(int(round(t.ycor()+3))), font=("Arial", 5, "normal"))
            else:
                t.goto(t.xcor()-13, t.ycor()-3)
                t.pendown()
                t.write(str(int(round(t.ycor()+3))), align="right", font=("Arial", 5, "normal"))
            t.penup()
            t.goto(0, t.ycor()+3)
        t.penup()
        t.goto(0, t.ycor())
        t.pendown()
        t.setheading(90)
    t.penup()

def draw_x_axis():
    t.goto(-screenx, 0)
    t.pendown()
    t.setheading(0)
    for i in range(0, int(screenx*2/10)):
        t.forward(10)
        t.goto(t.xcor(), t.ycor()+5)
        t.setheading(270)
        t.forward(10)
        t.penup()
        if int(round(t.xcor())) > 10 or int(round(t.xcor())) < -10:
            if i % 2 == 0:
                t.forward(10)
                t.pendown()
                t.write(str(int(round(t.xcor()))), align="center", font=("Arial", 5, "normal"))
            else:
                t.forward(-10)
                t.pendown()
                t.write(str(int(round(t.xcor()))), align="center", font=("Arial", 5, "normal"))
        t.penup()
        t.goto(t.xcor(), 0)
        t.pendown()
        t.setheading(0)
    t.penup()



draw_bounding()
draw_x_axis()
draw_y_axis()
screen.mainloop()

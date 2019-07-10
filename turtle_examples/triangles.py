import turtle

t = turtle.Turtle()
s = turtle.Screen()
t.shape("turtle")
t.wheel=24
s.bgcolor("blue")
t.pensize(10)
t.pencolor("red")

for i in range(t.wheel):
    t.begin_fill()
    t.rt(135)
    t.fd(200)
    t.lt(120)
    t.fd(200)
    t.lt(120)
    t.fd(200)
    t.end_fill()
    t.fd(200) 
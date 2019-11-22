import turtle
import random
from time import sleep
import datetime

t = turtle.Turtle()
screen = turtle.Screen()

# slow mode:
#t.speed(10)


#optimizations:
t.speed(0)
screen.tracer(0, 0)
t.hideturtle()

screenx = screen.screensize()[0]
screeny = screen.screensize()[1]



class Square:
    def __init__(self, x, y, vel, size):
        self.x = x
        self.y = y
        self.vel = vel
        self.size = size


    def draw_square(self, x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()
        for i in range(4):
            t.forward(self.size)
            t.right(90)


    def collision_check(self):
        if self.x <= -screenx:
            self.vel[0] *= -1
            self.x = -screenx
        elif self.x >= screenx - self.size:
            self.vel[0] *= -1
            self.x = screenx - self.size
        elif self.y <= -screeny + self.size:
            self.vel[1] *= -1
            self.y = -screeny + self.size
        elif self.y >= screeny:
            self.vel[1] *= -1
            self.y = screeny


    def update(self, dt):
        self.collision_check()
        self.x += dt / 20000 * self.vel[0]
        self.y += dt / 20000 * self.vel[1]
        self.draw_square(self.x, self.y)


def random_sign():
    if random.random() > 0.5:
        return(-1)
    else:
        return(1)

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




square_list = []
square_size = 30
for i in range(0, 20):
    x = random_sign() * random.randint(0, screenx-square_size)
    y = random_sign() * random.randint(0, screeny-square_size)
    xv = random_sign() * random.randint(1, 10)
    yv = random_sign() * random.randint(1, 10)
    square_list.append(Square(x, y, [xv, yv], square_size))

difference = 3000
while True:
    start = datetime.datetime.now()
    draw_bounding()
    for s in square_list:
        s.update(difference)
    screen.update()
    t.clear()
    end = datetime.datetime.now()
    difference = int((end-start).microseconds)

import turtle
import math
import time

start = time.time()

size = 400
turtle.tracer(0)
alex = turtle.Turtle()
alex.ht()
alex.pu()
alex.goto(-size/2, -size*0.75)
alex.pd()
alex.left(108)
alex.fillcolor('black')

offset = math.sin(math.radians(108))/math.sin(math.radians(36))
cos = [offset*math.cos(math.radians(108 - i * 72)) for i in range(5)]
sin = [offset*math.sin(math.radians(108 - i * 72)) for i in range(5)]
ratio = 2+2*math.sin(math.radians(18))


def pentagon(okay, length):
    okay.begin_fill()
    for i in range(5):
        okay.forward(length)
        okay.right(72)
    okay.end_fill()

def recursion(bruh, length, depth):
    if depth <= 0:
        pentagon(bruh, length)

    else:
        length/=ratio
        for i in range(5):
            recursion(bruh, length, depth-1)
            bruh.pu()
            bruh.goto(bruh.xcor()+length*cos[i], bruh.ycor()+length*sin[i])
            bruh.pd()
               

recursion(alex, size, 5)
turtle.update()
print(f'{time.time()-start} seconds')

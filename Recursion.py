# Libraries
import turtle
import math
import time


# Set-up
start = time.time()
size = 400
turtle.tracer(0)
pen = turtle.Turtle()
pen.ht()
pen.pu()
pen.goto(-size/2, -size*0.75)
pen.pd()
pen.left(108)
pen.fillcolor('black')


# Constants
offset = math.sin(math.radians(108))/math.sin(math.radians(36))
cos = [offset*math.cos(math.radians(108 - i * 72)) for i in range(5)]
sin = [offset*math.sin(math.radians(108 - i * 72)) for i in range(5)]
ratio = 2+2*math.sin(math.radians(18))


# Drawing Function
def pentagon(pen, length):
    pen.begin_fill()
    for i in range(5):
        pen.forward(length)
        pen.right(72)
    pen.end_fill()

def recursion(pen, length, depth):
    if depth <= 0:
        pentagon(pen, length)

    else:
        length/=ratio
        for i in range(5):
            recursion(pen, length, depth-1)
            pen.pu()
            pen.goto(pen.xcor()+length*cos[i], pen.ycor()+length*sin[i])
            pen.pd()
               
# Run code
recursion(pen, size, 5)
turtle.update()
print(f'{time.time()-start} seconds')

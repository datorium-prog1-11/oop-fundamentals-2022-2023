import turtle
import random

def draw_retangle(x,y,w,h,color):
    turtle.up()
    turtle.seth(0)
    turtle.goto(x-w/2,y-h/2)
    turtle.fillcolor(color)
    turtle.down()
    turtle.begin_fill()
    for i in range(2):
        turtle.fd(w)
        turtle.left(90)
        turtle.fd(h)
        turtle.left(90)
    turtle.end_fill()

turtle.setup(700,700)
turtle.title("Random Rectangles - PythonTurtle.Academy")
turtle.speed(0)
turtle.hideturtle()
n = 100
for i in range(n):
    draw_retangle(random.randint(-300,300),random.randint(-300,300),
                     random.randint(5,100),random.randint(5,100),
                     (random.uniform(0,1),random.uniform(0,1),random.uniform(0,1)))
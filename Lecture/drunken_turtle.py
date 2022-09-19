import turtle
import random

turtle.shape('turtle')
turtle.speed(0)

while(True):
    turtle.stamp()
    turtle.setheading(random.randint(0,360))
    turtle.forward(random.randint(50,100))
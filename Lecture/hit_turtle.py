import turtle
import random

turtle.speed(0)

def drunken_move():
	turtle.setheading(random.randint(0,360))
	turtle.forward(random.randint(50,300))
	turtle.stamp()

def restart():
	turtle.reset()
	turtle.speed(0)

turtle.shape('turtle')

turtle.onkey(drunken_move, 'space')
turtle.onkey(restart, 'Escape')
turtle.listen()


turtle.exitonclick()
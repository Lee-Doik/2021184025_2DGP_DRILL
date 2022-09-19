import turtle

turtle.speed(0)

#draw horizon lines

y = -250
while y <= 250:
	turtle.penup()
	turtle.goto(-250,y)
	turtle.pendown()
	turtle.goto(250,y)
	y += 100

#draw vertical lines

x = -250
while x <= 250:
	turtle.penup()
	turtle.goto(x,-250)
	turtle.pendown()
	turtle.goto(x,250)
	x += 100

turtle.exitonclick()
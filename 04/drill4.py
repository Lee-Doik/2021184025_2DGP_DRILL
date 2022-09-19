import turtle

turtle.speed(0)
count1 = 5
count2 = 5
y = -200

while (count2 > 0):
    count1 = 5
    turtle.penup()
    x = -220
    while (count1 > 0):
        turtle.goto(x,y)
        turtle.pendown()
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        count1 = count1 -1
        x = x + 100
    y = y + 100
    count2 = count2 - 1
    turtle.penup()


turtle.exitonclick()

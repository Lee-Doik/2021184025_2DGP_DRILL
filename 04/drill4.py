import turtle

turtle.speed(0)
count = 5
x = 0

while (count > 0):
    turtle.goto(x,0)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    count = count -1
    x = x + 100

turtle.penup()
x = 0
count = 5

while (count > 0):
    turtle.goto(x,100)
    turtle.pendown()
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    count = count -1
    x = x + 100

turtle.penup()
x = 0
count = 5

while (count > 0):
    turtle.goto(x,200)
    turtle.pendown()
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    count = count -1
    x = x + 100

turtle.penup()
x = 0
count = 5

while (count > 0):
    turtle.goto(x,300)
    turtle.pendown()
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    count = count -1
    x = x + 100

turtle.penup()
x = 0
count = 5

while (count > 0):
    turtle.goto(x,400)
    turtle.pendown()
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    count = count -1
    x = x + 100

turtle.exitonclick()

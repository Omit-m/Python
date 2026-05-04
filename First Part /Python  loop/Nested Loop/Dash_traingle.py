import turtle

turtle.speed(2)
turtle.shape('turtle')

for i in range(3):
    for i in range(20):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(3)
        turtle.pendown()
    turtle.left(120)        

turtle.exitonclick()
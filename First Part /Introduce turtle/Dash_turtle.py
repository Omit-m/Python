import turtle
turtle.speed(1)
      
for i in range(10):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(3)
    turtle.pendown()
    turtle.forward(10)

turtle.exitonclick()
import turtle

length = int(input(" Enter the length :  "))

def triangle(length):
    for i in range (3):
        turtle.forward(length)
        turtle.left(120)


triangle(length)
turtle.exitonclick()        
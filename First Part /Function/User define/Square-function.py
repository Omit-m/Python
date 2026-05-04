import turtle

def draw_square (side_langth):
    for i in range(4):
        turtle.forward(side_langth)
        turtle.left(90)
draw_square(100)

turtle.done()


import turtle   
nonte = turtle.Turtle()
fonte = turtle.Turtle()

nonte.shape("circle")
fonte.shape("square")
nonte.left(30)
nonte.forward(100)
fonte.backward(50)

monte = turtle.Turtle()
monte.setpos(-100,-100)

monte.forward(30)
monte.forward(30)


monte.clear()
fonte.clear()
nonte.clear()

fonte.shape("triangle")
monte.shape("square")

turtle.exitonclick ()
import turtle
import random

turtle.speed(5) # Set the turtle speed to the fastest

colors=    ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
for i in range ( 100):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    
    # turtle.penup()
    turtle.setposition(x, y)

    i= random.randint(0, len(colors)-1)
    turtle.color(colors[i])
    turtle.dot()

turtle.done()    
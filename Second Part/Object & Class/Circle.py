import turtle
import random


# tom = turtle.Turtle() # creates a turtle object named tom
turtle.speed(5)
turtle.hideturtle() # # makes the turtle invisible
colors = ["red", "blue", "green", "yellow", "orange", "purple"] 



for i in range(10):
    turtle.color(random.choice(colors))
    turtle.begin_fill()
    turtle.circle(200)
    turtle.end_fill()       

turtle.done()
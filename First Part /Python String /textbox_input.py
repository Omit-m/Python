import turtle

name = turtle.textinput( " Name ", " What is your name ? ")

name = name.lower()

if name.startswith("mr"):
    print("Hello sir, how are you")
elif name.startswith("mrs") or name.startswith("miss") or name.startswith("ma") :
    print("Hello mam, how are you")

else:
    name = name.capitalize()
    str = "Hi " + name + "! How are you " 
    print(str)

turtle.exitonclick()   
"""
Inside the editor, complete the following steps:

Create a list called colors with the values "red", "green", "blue"
Print the first item in the list
Change the second item to "yellow"
Add "purple" to the end of the list using append()
Remove "red" from the list using remove()
Print the list
"""

# Ans

colors = ["red", "green", "blue"]
print(colors)

colors[1:2]=["yellow"]
print(colors)


colors.append("purple")
print(colors)

colors.remove("red")
print(colors)
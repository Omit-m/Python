"""
Write a  function for multiplication table :
👉 If the user presses Enter,the default value becomes 1.
👉 Otherwise, it prints the multiplication table of the entered number.
"""

def mul(n=1):
    for i in range(1,11):
        print(n, "*", i, "=",n * i)

Input = input("Enter a number : ")

if Input == "":
    mul()
else:
    mul(int(Input))    
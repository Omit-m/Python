# def div ( a, b):
#     return a/b

# print(div(10,2))
# print(div(3,0))
# print(div(6,2))

"""
Output :

5.0
ZeroDivisionError: division by zero

"""

def div1(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Can not dicide by zero")

print(div1(10,2))
print(div1(3,0))
print(div1(6,2))
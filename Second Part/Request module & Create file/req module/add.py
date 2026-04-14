import sys 

print(sys.argv) 
print(type(sys.argv))

arguments = sys.argv  # Exclude the script name

a= int(arguments[1] ) # First argument
b= int(arguments[2])  # Second argument      

print(a + b)  # Concatenation of strings


"""
Output:

omit@Omits-MacBook-Air req module % python3 add.py 3 6
['add.py', '3', '6']
<class 'list'>
9
"""




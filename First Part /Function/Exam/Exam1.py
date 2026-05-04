"""
# Write a Python function that takes a list of numbers and print the average of those numbers ?

"""

def my_fnc(numbers):
    total_number = len(numbers)
    result=0
    for number in numbers:
        result +=number

    # global avg
    avg= result / total_number
    return avg
    

"""
This method only worked when the local variable turned into a global variable.
"""
# my_fnc([10,20,30,40,50,60,70,80,90,100])    
# print("Avg = ",avg)    


#  Better Practice: Using return

avg = my_fnc([10,20,30,40,50,60,70,80,90,100])    
print("Avg = ",avg)    
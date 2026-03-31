import random


n= [random.randint(1, 100) for _ in range(10)]  
print("Original list:", n)  

n.sort()
print("Sorted list:", n)    

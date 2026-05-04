step= int(input("Enter the lenght of list :  "))
ls=[]

for i in range(step):
    value = int(input("Enter the value : "))
    ls.append(value)
 
print(ls)

total = sum(ls) 
#(The sum() function in Python is used to quickly add numbers from a list)

print("total = ", total)
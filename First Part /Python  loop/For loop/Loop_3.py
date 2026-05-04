# Find highest value from list 
import random
ls=[]
maX_num=0
for i in range (5):
    num= random.randint(10, 50)
    ls.append(num)
print(ls)

for n in ls:
    if n > maX_num:
        maX_num=n
print(maX_num)  


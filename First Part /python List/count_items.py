import random
ls = []

for i in range (500):
    item=random.randint(1,100)
    ls.append(item)
    
for i in range (1,101):
    Count = ls.count(i)
    print(i, "appeares ",Count, " times ") 
numbers = (10,20,30,40,50)
n1, n2, n3, n4, n5 = numbers

print(n1)
print(n2)
print(n3)

t = n3,n4
print(t)

print(type(t))


# ...............

items = (10,20,30,5.5,["a","b","c"],("apple","banana"))

for item in items:
    print(item, type(item))

print(items[4].append("d")) 

print(items[4][3])
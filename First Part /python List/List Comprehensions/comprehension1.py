# List comprehensions provide a concise way to create lists. It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The expressions can be anything, meaning you can put in all kinds of objects in lists. The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it. The list comprehension always returns a result list.

# without list comprehension
# li = [1,2,3,4,5,6,7,8,9,10]
# new_li = []

# for x in li:
#     new_li.append(x*2)
  
# new_li2 = li + new_li

# even = []
# for x in new_li2:
#     if x%2 == 0:
#         even.append(x)
# print(even)


# with list comprehension

li = [11,23,33,44,55,66,77,88,99,100]
new_li2 = li + [i*2 for i in li] 

even = [x for x in new_li2 if x%2 == 0]

print(even)
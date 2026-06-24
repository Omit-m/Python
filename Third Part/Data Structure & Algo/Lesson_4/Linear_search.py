def linear_search(list, target):

 list_length = len(list)
 i = 0

 while i < list_length:
  if list[i] == target:
   return i
  i += 1

i = -1  

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5
result = linear_search(list, target) 

print(f'Target digit {target} found at index: {result}')
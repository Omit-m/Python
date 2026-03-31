# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

# | Feature     | List               | Array                   |
# | ----------- | ------------------ | ----------------------- |
# | Data Type   | Mixed allowed      | Same type only          |
# | Built-in    | Yes                | No (`array` module)     |
# | Flexibility | Very flexible      | Less flexible           |
# | Performance | Slower for numbers | Faster for numeric data |


# Example of using list methods

my_list = [1, 2, 3, 4, 5]
my_list.append(6)  

print(my_list)  

my_list.reverse() 
print(my_list)
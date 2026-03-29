marks = {1:85, 2:90, 3:78, 4:92, 5:88}

print(type(marks)) 


print(marks[3])  # Accessing value via using key
print(marks.get(4))  # Accessing value via using get() method

print(marks.get(6, "Key not found"))  # Accessing value for a non-existent key with default message
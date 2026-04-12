
"""
Write a Python program to perform file handling operations as follows:

1. Create a file named file2.txt and write the line:
"This is the task file" into it.
2. Then reopen the same file and write the given line without removing the previous line:
"This is the appended line of the task file".
3. Close the file properly after each operation.

"""

file2= open("file2.txt","w")
file2.write("This is the task file")
file2.close()

file2= open("file2.txt","a")
file2.write("\nThis is the appended line of the task file")
file2.close()
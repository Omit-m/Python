# Write mode: overwrites the file
file1 = open("myfile.txt", "w")
# L = ["This is Delhi \n", "This is Paris \n", "This is London"]
file1.write("This is Delhi \nThis is Paris \nThis is London\n")
file1.close()

# Append mode: adds to the end of the file
file1 = open("myfile.txt", "a")
file1.write("this is Dhaka\nthis is paris")
file1.close()

# Reading file content
file1 = open("myfile.txt", "r")
print("Output after appending:\n")
print(file1.read())
file1.close()

# Write mode again: overwrites previous content
file1 = open("myfile.txt", "w")
file1.write("This is Omit from Dhaka, bangladesh")
file1.close()

# print the overwriting
file1 = open("myfile.txt", "r")
print("Output after overwriting:")
print(file1.read())
file1.close()
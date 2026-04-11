# Write mode: overwrites the file
file1 = open("myfile.txt", "w")
# L = ["This is Delhi \n", "This is Paris \n", "This is London"]
file1.write("This is Delhi \nThis is Paris \nThis is London\n")
file1.close()


file1 = open("myfile.txt", "a")
file1.write("Now I am in Append mode---------------------\nthis is Dhaka\nthis is paris")
file1.close()
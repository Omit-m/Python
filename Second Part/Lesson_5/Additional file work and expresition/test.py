lines = ["This is the first line.", "This is the second line.", "This is the third line."]


with open("file.txt", "w") as f:
    for line in lines:
        f.write(line + "\n")


with open("file.txt", "r") as f: 
    content = f.read() # read() reads the entire content of the file and returns it as a single string.
    print(content)  


with open ("file.txt", "r") as f:
    lines = f.readlines() # readlines() reads the file and returns a list of lines, where each line is a string in the list.
    print("\n",lines,"\n")
    for line in lines:  
        print(line)  

with open("file.txt", "r") as f:
    for line in f: # When you iterate over a file object, it reads the file line by line, returning each line as a string in each iteration.
        print(line)





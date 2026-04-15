lines = ["This is the first line.", "This is the second line.", "This is the third line."]


with open("file.txt", "w") as f:
    for line in lines:
        f.write(line + "\n")


# with open("file.txt", "r") as f:
#     content = f.read()
#     print(content)  


with open ("file.txt", "r") as f:
    lines = f.readlines()
    print("\n",lines,"\n")
    for line in lines:  
        print(line)      




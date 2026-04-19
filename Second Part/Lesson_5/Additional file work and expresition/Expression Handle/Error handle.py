import io 

try:
    with open ("file.txt","r") as fp:
        content = fp.read()
        print(content)

except FileNotFoundError:
    print("file.txt not found. please check if the file's name is ccorrect.")

except io.UnsupportedOperation:
    print("Are you sure file.txt is readable")            
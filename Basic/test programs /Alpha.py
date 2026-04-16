import os, string, pycountry,names

# for letter in string.ascii_lowercase:
#     print(letter)

os.makedirs("Name list", exist_ok= True)
with open ("Name list/name.txt", "w") as name:
    for i in range(1000):
        name.write(names.get_full_name() + "\n")


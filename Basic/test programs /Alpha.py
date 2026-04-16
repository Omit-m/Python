import os
import string
import names

# Step 1: Create folder
os.makedirs("Names", exist_ok=True)

# Step 2: Create name.txt and store 1000 names
with open("Names/name.txt", "w") as file:
    for i in range(1000):
        file.write(names.get_full_name() + "\n")

# Step 3: Read names and organize by first letter
with open("Names/name.txt", "r") as file:
    for name in file:
        name = name.strip()  # remove newline

        if name:  # avoid empty lines
            first_letter = name[0].lower()  # get first character

            file_path = f"Names/{first_letter}.txt"

            # Step 4: Write name into corresponding file
            with open(file_path, "a") as letter_file:
                letter_file.write(name + "\n")
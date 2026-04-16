import pycountry
import string
import os
                
os.makedirs("Country list", exist_ok=True)

for letter in string.ascii_uppercase:
    
    
    with open("Country list/"+ letter + ".txt", "w") as c:
        for country in pycountry.countries:
            if country.name.startswith(letter):
                c.write(country.name + "\n")








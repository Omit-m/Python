import pycountry

with open("countries.txt", "w") as f:
    for country in pycountry.countries:
        f.write(country.name + "\n")





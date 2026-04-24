# Country = "Afganistan, America, Bangladesh, Canada, Denmark, England, Greenland, Netherlands, New Zealand, Sweden, Swithzerland"

# Countries = Country.split(",")

# li = [item for item in Countries if item.endswith("land") or item.endswith("lands")]

# print(li)


import re 

Country = "Afganistan, America, Bangladesh, Canada, Denmark, England, Greenland, Netherlands, New Zealand, Sweden, Swithzerland"


li = re.findall(r'(\w+lands*)', Country )

print(li)
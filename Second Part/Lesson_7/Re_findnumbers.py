import re


text = "Age 22 and 105"

# findall() → gets all numbers
single_digits = re.findall(r'\d', text)
multiple_digits = re.findall(r'\d+', text)

print(single_digits)
print(multiple_digits)


# Search() for the first occurrence.


import re

text = "I have 2 apples and 5 bananas"

m = re.search(r'apples', text)
print(m.group())






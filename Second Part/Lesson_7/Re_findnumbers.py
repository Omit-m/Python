import re


text = "Age 22 and 105"

single_digits = re.findall(r'\d', text)
multiple_digits = re.findall(r'\d+', text)

print(single_digits)
print(multiple_digits)
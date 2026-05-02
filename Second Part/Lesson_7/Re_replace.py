import re

text = "My email is omit123@gmail.com and I love Bangladesh. Call me at 01872035199."


# sub() → replace text
new_text = re.sub(r'Bangladesh', 'Canada', text)
print("sub():", new_text)
import re

text = "My email is omit123@gmail.com and I love Bangladesh. Call me at 01872035199."


# # finditer() → iterator with position
# print("finditer():")
# for m in re.finditer(r'\d+', text):
#     print("Value:", m.group(), "Start:", m.start())



for m in re.finditer(r'\d+', text):
    print(m.group(), m.span())    
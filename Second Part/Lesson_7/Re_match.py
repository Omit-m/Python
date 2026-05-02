import re

text = "My email is omit123@gmail.com and I love Bangladesh. Call me at 01872035199."

# match() → check from beginning
match_result = re.match(r'My', text)
print("match():", match_result.group() if match_result else "No match")
import re

text = "My email is omit123@gmail.com and I love Bangladesh. Call me at 01872035199."



# search() → find first occurrence
search_result = re.search(r'\d+', text)
print("search():", search_result.group())



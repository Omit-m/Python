import re

text = "My email is omit123@gmail.com and I love Bangladesh. Call me at 01872035199."

# 1. search() → find first occurrence
search_result = re.search(r'\d+', text)
print("search():", search_result.group())

# 2. match() → check from beginning
match_result = re.match(r'My', text)
print("match():", match_result.group() if match_result else "No match")

# 3. findall() → find all matches
all_numbers = re.findall(r'\d+', text)
print("findall():", all_numbers)

# 4. finditer() → iterator with position
print("finditer():")
for m in re.finditer(r'\d+', text):
    print("Value:", m.group(), "Start:", m.start())

# 5. sub() → replace text
new_text = re.sub(r'Bangladesh', 'Canada', text)
print("sub():", new_text)
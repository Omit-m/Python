import re

s = "Bangladesh is our homeland"

match = re.search('B.+h',s)

print(match.group())    

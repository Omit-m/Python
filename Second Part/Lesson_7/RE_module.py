import re

match = re.search('Bangla', 'Bangladesh')

match = re.search('desh' , 'Bangladesh')

match= re.search('des', 'Bangladesh')

print(match.group())
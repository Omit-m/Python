import re 

text = " Roses are red, violets are blue, sugar is sweet"

result = re.search(r"violets", text)
print(result.group())


# find all words that start with s      
result2 = re.findall(r"\bs\w+", text)
print(result2)
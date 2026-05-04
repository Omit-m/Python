Input = input("Enter a string : ")

Upper = ""
Lower = ""
disit = ""
special = ""

for ch in Input:
    if ch.isupper():
        Upper += ch
    elif ch.islower():
        Lower += ch  
    elif ch.isdigit():
        disit += ch
    else :
        special +=ch

print("Uppercase : ", Upper)      
print("lowercase : ", Lower)
print("Disit : ", disit) 
print("Special Characters : ", special)        
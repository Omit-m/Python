n = int(input("Enter number of terms: "))

a = 0  # first value
b = 1  # second value

for i in range(n):
    print(a)
    temp = a      # store current a
    a = b         # update a to b
    b = temp + b  # update b to sum of old a and b
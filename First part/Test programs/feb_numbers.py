n = int(input("Enter number of terms: "))

a = 0  # first value
b = 1  # second value

for i in range(n):
    print(a)
    temp = a      # store current a
    a = b         # update a to b
    b = temp + b  # update b to sum of old a and b
# This program generates the Fibonacci sequence up to n terms. The first two terms are 0 and 1, and each subsequent term is the sum of the previous two terms.
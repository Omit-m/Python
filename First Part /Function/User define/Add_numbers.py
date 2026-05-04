n=int(input(" How many numbers you want to add ? "))

sum=0
def total ():
    global sum # use global variable
    for i in range(n):
        number = int(input("Enter a number : "))
        sum += number
    print("Total = ",sum)

total()



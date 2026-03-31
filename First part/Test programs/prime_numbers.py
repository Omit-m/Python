# def is_prime(num):
#     if num < 2:
#         return False
#     prime = True
#     for i in range(2,num):
#         if num % i == 0:
#             prime = False
#             break
#     return prime

# while True:
#     number = int(input("Enter a number (or 'exit' to quit): "))
#     if number ==  0:
#         break
#     prime = is_prime(number)
#     if prime is True:
#         print(f"{number} is a prime number.")
#     else:
#         print(f"{number} is not a prime number.")   




range_end = int(input("Enter the end of the range: "))
def is_prime(range_end):
    

    for i in range(2, range_end + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i) 


is_prime(range_end)    
               
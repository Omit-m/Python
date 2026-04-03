n = int(input("Enter the number of limits : "))
def list_fib(n):
    if n <= 2:
        return 1 
    fib_x, fib_next = 1, 1
    fib_list=[]

    i = 3
    while i <= n:
            
        fib_x, fib_next = fib_next, fib_x + fib_next
        fib_list.append(fib_next)
        i += 1  
    return fib_list
   

print(list_fib(n))
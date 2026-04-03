import create_module as cm


print( "hello, I am inside exam.py file")

lm = 16
for i in range(1, lm):
    n = cm.find_fib(i)
    print(i, ":", n)
import create_module as cm


print( "hello, I am inside exam.py file")

ls =[]
lm = 16
for i in range(1, lm):
    n = cm.find_fib(i)
    ls.append(n)
print(ls)
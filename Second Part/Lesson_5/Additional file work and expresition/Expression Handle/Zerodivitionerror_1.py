def div1(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Can not dicide by zero")
    except TypeError:
        print("Unsupported type. Did you use string ? ")    

print(div1(10,2))
print(div1(3,0))
print(div1(6,2))
print(div1("12", 4))
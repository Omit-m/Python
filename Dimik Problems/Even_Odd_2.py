t = int (input ())

for _ in range (t) :
    n= input ().strip ()

    if n[-1] in '02468' :
        print ('even')
    else :        
        print ('odd')
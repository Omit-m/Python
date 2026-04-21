class numbers: 
    a = 10
    b = 20

class Addition(numbers):
    c = 30
    d = 40 

    def add(self):
        total= self.a + self.b + self.c + self.d
        print(total)
        
ob = Addition()

ob.add()
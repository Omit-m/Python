class Numbers:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Numbers1:
    def __init__(self, e, f):
        self.e = e
        self.f = f

class Addition(Numbers, Numbers1):
    def __init__(self, a, b, c, d, e, f):
        Numbers.__init__(self, a, b)      # call first parent
        Numbers1.__init__(self, e, f)     # call second parent

        self.c = c
        self.d = d

    def add(self):
        total = self.a + self.b + self.c + self.d + self.e + self.f
        print("Total:", total)


obj = Addition(10, 20, 30, 40, 50, 60)
obj.add()
class Numbers:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Addition(Numbers):
    def __init__(self, a, b, c, d):
        super().__init__(a, b) # Call the parent class constructor (__init__) and pass a and b to it.
        self.c = c
        self.d = d

    def add(self):
        total = self.a + self.b + self.c + self.d
        print("Total:", total)


obj = Addition(10, 20, 30, 40)
obj.add()
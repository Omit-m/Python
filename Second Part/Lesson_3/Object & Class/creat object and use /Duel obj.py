class Student:
    def __init__(self,n,m,o,p,q):
        self.name = n
        self.roll = m
        self.age = o
        self.marks = p
        self.address = q

    def details(self):

        print("Student details : ")
        print("\n")
        print("name : ", self.name)
        print("Roll:", self.roll)
        print("Age : ",self.age)
        print("Marks : ", self.marks)
        print("Address : ", self.address)
        
student1= Student("Omit", 550810, 23 , 88 , "Alfadanga")
student1.details()
print("\n")
student2= Student("Tonne", 14, 17 , 81 , "Alfadanga")
student2.details()
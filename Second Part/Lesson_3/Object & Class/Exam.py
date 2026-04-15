# Write a Python program to design a Car class.

# The class should have the following attributes:
# - Name
# - Manufacturer
# - Color
# - Year
# - Engine capacity (cc)

# The class should include the following methods:
# - start() → to start the car
# - brake() → to stop the car
# - drive() → to drive the car
# - turn() → to turn the car
# - change_gear() → to change the gear

# Tasks:
# 1. Create the Car class with the above attributes and methods.
# 2. Create an object of the class.
# 3. Take user input and call at least one method based on the input



class car:
    def __init__(self,name, manufacturer, color, year, cc):
        self.name= name
        self.manufacturer = manufacturer
        self.color= color
        self.year= year
        self.cc=cc

    def start(self):
        print("Name : ",self.name)
        print("manufacturer : " ,self.manufacturer)
        print("color : ", self.color)
        print("Year : ", self.year)
        print("Cc : ", self.cc)
        print("Car is starting...")


    def brake(self):
        print("Name : ",self.name)
        print("manufacturer : " ,self.manufacturer)
        print("color : ", self.color)
        print("Year : ", self.year)
        print("Cc : ", self.cc)
        print("Car is braking...")


    def drive(self):
        print("Name : ",self.name)
        print("manufacturer : " ,self.manufacturer)
        print("color : ", self.color)
        print("Year : ", self.year)
        print("Cc : ", self.cc)
        print("Car is driving...")


    
    def turn(self):
        print("Name : ",self.name)
        print("manufacturer : " ,self.manufacturer)
        print("color : ", self.color)
        print("Year : ", self.year)
        print("Cc : ", self.cc)
        print("Car is turning...")    


   
    def change_gear(self):
        print("Name : ",self.name)
        print("manufacturer : " ,self.manufacturer)
        print("color : ", self.color)
        print("Year : ", self.year)
        print("Cc : ", self.cc)
        print("Car is changing the gear...")


my_car = car("BMW X5", "BMW", "Black", 2023, 3000) 
n = input("Enter action: ").lower()

n = n.lower()

if n=="start":
    my_car.start()
elif n=="brake":
    my_car.brake()
elif n=="drive":
    my_car.drive()
elif n== "turn":
    my_car.turn()
elif n=="change_gear": 
    my_car.change_gear()
else:
    print("Invalid action")



    
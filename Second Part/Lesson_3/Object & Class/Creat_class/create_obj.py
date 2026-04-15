class Car:
    name = ""
    model = ""
    year = ''

    def start(self):
        print("Car is starting...")


# create object of the class
my_car = Car()
my_car.name = "BMW"
my_car.model = "X5"
my_car.year = 2020

# print the attributes of the object
print("Name of the car is ", my_car.name)
print("Name of the model of ", my_car.name, "is ", my_car.model)
print("Year of the car is", my_car.year)    

my_car.start()
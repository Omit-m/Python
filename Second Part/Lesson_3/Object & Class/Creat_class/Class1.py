class car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def start(self):
        print("Car is starting...")


my_car=car ("BMW", "X5", 2020)

print("Name of the car is ", my_car.name)
print("Model of the car is ", my_car.model)
print("Year of the car is ", my_car.year)

my_car.start()  
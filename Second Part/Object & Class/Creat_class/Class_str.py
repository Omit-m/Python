"""
class <class_name>:
    <statement-1>   
    <statement-2>
    ...
    <statement-N>

"""

class Car:
    name = "BMW"
    model = "X5"
    year = 2020

    def start():
        print("Car is starting...")

print("Name of the car is ",Car.name)
print("Name of the model of ",Car.name,"is ",Car.model)
print("Year of the car is", Car.year)

Car.start()   

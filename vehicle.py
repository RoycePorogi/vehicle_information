
# Name: Royce Porogi
# File Name: vehicle.py
# Description: This program asks the user to enter information about a car,
#              stores the information in an Automobile object, and displays
#              the vehicle's information.

# Variables:
# vehicle_type - Stores the type of vehicle (car).
# year - Stores the year the car was made.
# make - Stores the manufacturer of the car.
# model - Stores the model of the car.
# doors - Stores the number of doors on the car.
# roof - Stores the type of roof on the car.
# car - Stores the Automobile object created using the user's input.



#Vehicle Super Class
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

#Automobile Subclass
class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__("car")
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


#Main Program
print("Enter vehicle information below:")

year = input("Enter the year: ")
make = input("Enter the make: ")
model = input("Enter the model: ")
doors = input("Enter the number of doors (2 or 4): ")
roof = input("Enter the type of roof (solid or sun roof): ")

#Automobile Object Creation
car = Automobile(year, make, model, doors, roof)

#Display vehicle information
print("\nVehicle Information:")
print("Vehicle type: ",car.vehicle_type)
print("Year: ",car.year)
print("Make: ",car.make)
print("Model: ",car.model)
print("Number of doors: ",car.doors)
print("Type of roof: ",car.roof)

#Inheritance and polymorphism

#inheritance involves creating new classes (subclasses or derived classes) based on existing classes (superclasses or base classes)

#the word polymorphism is derived from Greek - means many forms

#follows an Is - A relationship
# A car IS A vehicle
# A bike IS A vehicle

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Vehicle is starting")

    def stop(self):
        print("Vehicle is stopping")


class Car(Vehicle):

    def __init__(self, brand, model, year, number_doors):
        super().__init__(brand, model, year)
        self.number_doors = number_doors

    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car is stopping")

class Bike(Vehicle):

    def __init__(self, brand, model, year, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_wheels = number_of_wheels

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)

    # Below, we "override" the start and stop methods, inherited from Vehicle, to provide bike-specific behaviour

    def start(self):
        print("Motorcycle is starting.")

    def stop(self):
        print("Motorcycle is stopping.")


car = Car("Ford", "Focus", 2008, 4,)
bike = Bike("Honda", "Scoopy", 2018, 2)

print(car.__dict__)
print(bike.__dict__)

car.start()
bike.start()

# Client code (in other words, inside some other class or script)
# Create list of vehicles to inspect
vehicles: list[Vehicle] = [
    Car("Ford", "Focus", 2008, 5),
    Motorcycle("Honda", "Scoopy", 2018)
]

# for vehicle in vehicles:
#     if isinstance(vehicle, Car):
#         print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
#         vehicle.start()
#         vehicle.stop()
#     elif isinstance(vehicle, Motorcycle):
#         print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
#         vehicle.start()
#         vehicle.stop()
#     else:
#         raise Exception("Object is not a valid vehicle")

for vehicle in vehicles:

    if isinstance(vehicle, Vehicle):
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start()
        vehicle.stop()  
    else:
        raise Exception("Object is not a valid vehicle")

#better for-loop above ^^






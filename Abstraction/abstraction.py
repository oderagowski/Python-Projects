from abc import ABC, abstractmethod # needed to make abstract methods

class Vehicle(ABC):
    def ON(self):
        print("You turn the vehicle on")

    @abstractmethod #makes the method an abstract method
    def drive(self):
        pass

#Child Class #1
class Car(Vehicle):

    def drive(self):  ## defines "Vehicle" abstract method
        print("You drive the car")

#Child Class #2
class Motorcycle(Vehicle):
    def drive(self): # defines "Vehicle" abstract method
        print("You ride the motorcycle")


# newVehicle = Vehicle() # cannot be instantiated because Vehicle class has an abstract method

#Object
car1 = Car() #instantiation
car1.ON() # regular method inherited from parent class "Vehicle"
car1.drive() #abstract class inherited from parent class "Vehicle"


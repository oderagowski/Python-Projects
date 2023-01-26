class Car:
    def __init__(self, make, model, transmission, color):
        self.make = make
        self.model = model
        self._transmission = transmission # protected property
        self.__color = color ## private property

    #used to access private property
    def set_color(self, value):
        self.__color = value

    def get_color(self):
        print(self.__color)


Car1 = Car("Honda", "Accord", "Automatic", "Gray")


print(Car1.make)
print(Car1.model)
print(Car1._transmission) # can still be accessed since protected properties do not affect the property
# print(Car1.__color) # Error because __color is a private property
print(Car1.get_color()) # used to access the private property of "__color"



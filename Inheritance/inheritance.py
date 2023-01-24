# Parent Class
class Animal:
    def __init__(self, name, eyes, legs):
        self.name = name
        self.eyes = eyes
        self.legs = legs

    def eat(self, food):
        print(f"I like to eat {food}")

    def breathe(self):
        print("I can breathe")

# First Child Class; inherits all properties and functions of "Animal" class 
class Bird(Animal):
    def __init__(self, wings, feather_color):
        self.wings = wings
        self.feather_color = feather_color

    def fly(self):
        print("I can fly!")

# Second Child Class; inherits all properties and functions of "Animal" class 
class Fish(Animal):
    def __int__(self, fins, scales_color):
        self.fins = fins
        self.scales_color = scales_color

    def swim(self):
        print("I can swim and breather under water!")

# Parent Class

class Bird:
    def __init__(self, wings, feather_color, num_of_eggs, time_active):
        self.wings = wings
        self.feather_color = feather_color
        self.num_of_eggs = num_of_eggs
        self.time_active = time_active

    def sound(self):
        print("Tweet tweet")

    def fly(self):
        print("I'm flying high in the sky")

# First Child Class; inherits all properties and functions from parent class
# Polymorphism: sound()
class Owl(Bird):
    def __init__(self, head_size, talon_length):
        self.head_size = head_size
        self.talon_length = talon_length

    def sound(self):
        print("Hoot hoot")

# Second Child Class; inherits all properties and functions from parent class
# Polymorphism: fly()
class Penguin(Bird):
    def __init__(self, hours_swimming, likes_salt_water):
        self.hours_swimming = hours_swimming
        self.likes_salt_water = likes_salt_water

    def fly(self):
        print("I can't fly ☹")


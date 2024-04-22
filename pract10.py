# Define a class called Bike
class Bike:
    def __init__(self):
        self.name = ""  # Initialize name attribute
        self.gear = 0   # Initialize gear attribute

# Create an object of the Bike class
bike1 = Bike()

# Modify the attributes of the bike1 object
bike1.name = "Mountain Bike"
bike1.gear = 11

# Access and print the modified attributes
print(f"Name: {bike1.name}, Gears: {bike1.gear}")

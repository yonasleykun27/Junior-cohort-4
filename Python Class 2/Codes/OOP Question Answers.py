# Create a class Person with attributes name and age. Print both values.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Yonas", 25)

print(f"Name: {person1.name}")
print(f"Age: {person1.age}")


# Create a class Rectangle that has methods to calculate area and perimeter.
# Hint: area = length * width, perimeter = 2 * (length + width)
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

rect1 = Rectangle(5, 3)
print(f"Area: {rect1.area()}")
print(f"Perimeter: {rect1.perimeter()}")


# Create a parent class Vehicle and a child class Car that inherits from it.
# The Car should have an extra attribute fuel_type and a method to display all details.
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def display_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Fuel Type: {self.fuel_type}")

car1 = Car("Toyota", "Corolla", "Petrol")


car1.display_details()
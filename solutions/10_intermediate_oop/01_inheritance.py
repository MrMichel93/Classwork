"""Reference solution for Mini-Program 1: Inheritance Basics."""


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Some generic animal sound")

    def info(self):
        print(f"{self.name} is a {self.species}")


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")


class Car(Vehicle):
    def honk(self):
        print("Beep beep!")


class Motorcycle(Vehicle):
    def rev_engine(self):
        print("Vroom vroom!")


class ElectricVehicle(Vehicle):
    def __init__(self, brand, model, year, battery_capacity):
        Vehicle.__init__(self, brand, model, year)
        self.battery_capacity = battery_capacity

    def charge(self):
        return f"Charging {self.battery_capacity} kWh battery"


class TeslaCar(ElectricVehicle):
    def autopilot(self):
        return "Autopilot enabled"


if __name__ == "__main__":
    dog = Dog("Buddy", "Canine")
    cat = Cat("Whiskers", "Feline")
    dog.info()
    cat.info()
    cat.make_sound()
    car = Car("Toyota", "Camry", 2024)
    motorcycle = Motorcycle("Honda", "CBR", 2023)
    car.display_info()
    car.honk()
    motorcycle.rev_engine()

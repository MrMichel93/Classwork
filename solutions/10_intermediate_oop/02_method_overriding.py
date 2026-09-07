"""Reference solution for Mini-Program 2: Method Overriding."""


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0

    def description(self):
        return "This is a shape"


class Rectangle(Shape):
    def __init__(self, name, width, height):
        Shape.__init__(self, name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, name, radius):
        Shape.__init__(self, name)
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Cow(Animal):
    def speak(self):
        return "Moo!"


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.1


class Manager(Employee):
    def calculate_bonus(self):
        return self.salary * 0.2


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"


if __name__ == "__main__":
    rectangle = Rectangle("screen", 4, 6)
    circle = Circle("coin", 5)
    animals = [Dog("Buddy"), Cat("Whiskers"), Cow("Bessie")]
    print(rectangle.area(), circle.area())
    for animal in animals:
        print(animal.name, animal.speak())
    print(Employee("Avery", 50000).calculate_bonus())
    print(Manager("Jordan", 50000).calculate_bonus())

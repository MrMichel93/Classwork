"""Reference solution for Mini-Program 3: Class Methods."""


class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, number):
        self.result += number

    def subtract(self, number):
        self.result -= number

    def get_result(self):
        return self.result


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14159 * self.radius * self.radius

    def calculate_circumference(self):
        return 2 * 3.14159 * self.radius


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def reset(self):
        self.count = 0

    def get_count(self):
        return self.count


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    def to_kelvin(self):
        return self.celsius + 273.15


if __name__ == "__main__":
    calculator = Calculator()
    calculator.add(10)
    calculator.add(5)
    calculator.subtract(3)
    circle, rectangle = Circle(5), Rectangle(4, 6)
    counter = Counter()
    for _ in range(5):
        counter.increment()
    counter.decrement()
    counter.decrement()
    print(calculator.get_result())
    print(circle.calculate_area(), circle.calculate_circumference())
    print(rectangle.calculate_area(), rectangle.calculate_perimeter())
    print(counter.get_count())
    counter.reset()
    print(counter.get_count())

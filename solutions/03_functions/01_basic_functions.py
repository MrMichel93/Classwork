"""Reference solution for the basic functions exercise."""


def greet():
    """Print a general greeting."""
    print("Hello, World!")


def greet_person(name):
    """Print a greeting for one person."""
    print(f"Hello, {name}!")


def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def calculate_area(length, width):
    """Return a rectangle's area."""
    return length * width


def is_even(number):
    """Return whether a number is even."""
    return number % 2 == 0


def power(base, exponent=2):
    """Return a base raised to an optional exponent."""
    return base**exponent


if __name__ == "__main__":
    greet()
    greet_person("Student")
    print(add_numbers(5, 3))
    print(multiply(4, 6))
    print(f"Area: {calculate_area(10, 5)}")
    print(is_even(8))
    print(power(3))

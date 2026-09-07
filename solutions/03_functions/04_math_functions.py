"""Reference solution for the mathematical utility functions exercise."""

PI = 3.14159


def find_max(a, b):
    """Return the larger of two values."""
    return a if a > b else b


def find_min(a, b):
    """Return the smaller of two values."""
    return a if a < b else b


def calculate_average(a, b):
    """Return the average of two values."""
    return (a + b) / 2


def is_positive(number):
    """Return whether a number is greater than zero."""
    return number > 0


def absolute_value(number):
    """Return a number's non-negative value."""
    return -number if number < 0 else number


def calculate_circle_area(radius):
    """Return a circle's area."""
    return PI * radius * radius


def calculate_circle_circumference(radius):
    """Return a circle's circumference."""
    return 2 * PI * radius


def find_max_of_three(a, b, c):
    """Return the largest of three values using ``find_max``."""
    return find_max(find_max(a, b), c)


def calculate_bmi(weight_kg, height_m):
    """Return body mass index from kilograms and metres."""
    return weight_kg / (height_m * height_m)


if __name__ == "__main__":
    print(find_max(15, 23), find_min(15, 23))
    print(absolute_value(-15))
    print(f"Circle area: {calculate_circle_area(5)}")
    print(f"Circle circumference: {calculate_circle_circumference(5)}")

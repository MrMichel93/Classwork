"""Reference solution for the area and perimeter calculator exercise."""

pi = 3.14159
length = 10.5
width = 6.2
rectangle_area = length * width
rectangle_perimeter = 2 * (length + width)
radius = 5.0
circle_area = pi * radius * radius
circle_circumference = 2 * pi * radius
base = 8.0
height = 6.0
triangle_area = 0.5 * base * height
square_side = 7
square_area = square_side * square_side
square_perimeter = 4 * square_side


def rectangle_measurements(rectangle_length, rectangle_width):
    """Return a rectangle's area and perimeter."""
    return rectangle_length * rectangle_width, 2 * (rectangle_length + rectangle_width)


def circle_measurements(circle_radius):
    """Return a circle's area and circumference using the exercise value of pi."""
    return pi * circle_radius**2, 2 * pi * circle_radius


def triangle_area_for(triangle_base, triangle_height):
    """Return a triangle's area."""
    return 0.5 * triangle_base * triangle_height


if __name__ == "__main__":
    print(f"Rectangle area: {rectangle_area}; perimeter: {rectangle_perimeter}")
    print(f"Circle area: {circle_area}; circumference: {circle_circumference}")
    print(f"Triangle area: {triangle_area}")
    print(f"Square area: {square_area}; perimeter: {square_perimeter}")

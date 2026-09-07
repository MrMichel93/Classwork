"""
Mini-Program 2: Method Overriding
Topic: Intermediate OOP

Learning Objectives:
- Understand method overriding in child classes
- Override parent methods with custom implementations
- Use method overriding to create specialized behavior
- Know when to override methods

Instructions:
Complete this program to learn about method overriding.
"""

# Student Self-Check
# Run: python3 -m unittest starter_tests.test_10_intermediate_oop.IntermediateOOPSelfChecks.test_method_overriding
# Expect: a 4 by 6 Rectangle area is 24; Dog.speak() returns "Woof!";
# a $50,000 Manager bonus is $10,000.

# TODO 1-4: Create a Shape/Rectangle hierarchy with method overriding
# Build Shape with __init__(name), area() returns 0, description() returns "This is a shape"
# Build Rectangle(Shape) with __init__(name, width, height)
# Override area() to return width * height
# Create a Rectangle instance and print its area
# Write your code here:


# TODO 5-6: Create a Circle child class that overrides area
# Build Circle(Shape) with __init__(name, radius)
# Override area() to return 3.14159 * radius * radius
# Create a Circle instance and print its area
# Write your code here:


# TODO 7-10: Create an Animal hierarchy with speak() overriding
# Build Animal with __init__(name), speak() returns "Some sound"
# Build Dog, Cat, Cow as children, each overriding speak()
# Dog returns "Woof!", Cat returns "Meow!", Cow returns "Moo!"
# Create instances, call speak() to demonstrate different behaviors
# Create a list of all three and loop to print names and sounds
# Write your code here:


# TODO 11-13: Create an Employee hierarchy with bonus calculation
# Build Employee with __init__(name, salary), calculate_bonus() returns salary * 0.1
# Build Manager(Employee) that overrides calculate_bonus() to return salary * 0.2
# Create both Employee and Manager with same salary, print bonuses to show difference
# Write your code here:


# BONUS TODO: Override __str__ in a custom class
# __str__ is called when you print() or str() an object
# Create Person class that overrides __str__ to return a formatted string
# Test with print statements
# Write your code here:

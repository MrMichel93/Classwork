"""
Mini-Program 3: Class Methods
Topic: Basic OOP

Learning Objectives:
- Define methods inside a class
- Use the self parameter
- Call methods on object instances
- Return values from methods

Instructions:
Complete this program to learn about class methods.
"""

# Student Self-Check
# Run: python3 -m unittest starter_tests.test_09_basic_oop.BasicOOPSelfChecks.test_class_methods
# Expect: add(10) then subtract(3) gives 7; a radius-5 circle has area 78.53975;
# incrementing a new Counter once makes its count 1.

# TODO 1-5: Create a Calculator class with basic operations
# Define Calculator with __init__ initializing result to 0
# Add 'add' and 'subtract' methods that modify self.result
# Add 'get_result' method that returns the current result
# Hint: def add(self, number): self.result += number
# Create an instance, call add(10), add(5), subtract(3), and print result
# Write your code here:


# TODO 6-9: Create a Circle class with geometric calculations
# Define Circle with __init__(self, radius)
# Add 'calculate_area' and 'calculate_circumference' methods
# Hint: Area = 3.14159 * r * r; Circumference = 2 * 3.14159 * r
# Create an instance with radius 5 and call both methods
# Write your code here:


# TODO 10-11: Create a Rectangle class for area and perimeter calculations
# Define Rectangle with __init__(self, width, height)
# Add 'calculate_area' (width * height) and 'calculate_perimeter' (2 * (width + height))
# Create an instance and test both methods
# Write your code here:


# TODO 12-13: Create a Counter class with increment/decrement/reset operations
# Define Counter with count initialized to 0
# Add methods: increment(), decrement(), reset(), get_count()
# Create an instance, increment 5 times, decrement 2 times, print, reset, print again
# Write your code here:


# BONUS TODO: Create a Temperature class for unit conversions
# Store a temperature in Celsius; add methods to convert to Fahrenheit and Kelvin
# Create an instance and test both conversion methods
# Write your code here:

"""
Mini-Program 2: Class Methods and Static Methods
Topic: Advanced OOP

Learning Objectives:
- Understand the difference between instance, class, and static methods
- Use @classmethod decorator for class methods
- Use @staticmethod decorator for static methods
- Know when to use each type of method

Instructions:
Complete this program to learn about class and static methods.
"""

# TODO 1-6: Create a Pizza class that uses class methods and a static validator
# Build Pizza with class attribute restaurant and __init__(size, toppings)
# Add factory-style class methods such as margherita() and pepperoni()
# Add validate_size(size) as a static method for accepted pizza sizes
# Create pizzas through the class methods and print their details
# Test validate_size with both valid and invalid size values
# Hint: class Pizza: def __init__(self, size, toppings): ...
# Hint: @classmethod def margherita(cls): ...
# Hint: @staticmethod def validate_size(size): ...
# Write your code here:


# TODO 7-10: Create a Date class with parsing and leap-year utilities
# Build Date with __init__(day, month, year)
# Add from_string(date_string) as a class method that builds a Date from text like "15-03-2024"
# Add is_leap_year(year) as a static method using the standard leap-year rules
# Test both helpers by creating a Date from a string and checking several years
# Hint: class Date: def __init__(self, day, month, year): ...
# Hint: @classmethod def from_string(cls, date_string): ...
# Hint: use date_string.split("-")
# Write your code here:


# TODO 11-13: Create utility classes that emphasize static and class-level behavior
# Build MathOperations with static methods add(a, b), multiply(a, b), and power(a, b)
# Build Counter with class attribute count and class methods increment(), get_count(), and reset()
# Use the math helpers without instantiating the class and demonstrate Counter tracking shared state
# Hint: class MathOperations: @staticmethod def add(a, b): ...
# Hint: class Counter: @classmethod def increment(cls): ...
# Write your code here:


# BONUS TODO: Create an Employee class with several factory class methods
# Add alternate constructors such as from_string(...), from_dict(...), and from_json(...)
# Each should build the same kind of object from a different input format
# Write your code here:

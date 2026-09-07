"""
Mini-Program 1: Inheritance Basics
Topic: Intermediate OOP

Learning Objectives:
- Understand class inheritance and why it's useful
- Create parent (base) and child (derived) classes
- Inherit attributes and methods from parent classes
- Add new methods to child classes

Instructions:
Complete this program to learn about inheritance in OOP.
"""

# Student Self-Check
# Run: python3 -m unittest starter_tests.test_10_intermediate_oop.IntermediateOOPSelfChecks.test_inheritance
# Expect: a Dog is an Animal; Dog keeps its name and species; Car has honk();
# Motorcycle has rev_engine().

# TODO 1-3: Create an Animal parent class
# Define Animal with __init__(self, name, species)
# Add 'make_sound' method that prints a generic animal sound
# Add 'info' method that prints the name and species
# Write your code here:


# TODO 4-6: Create a Dog child class
# Define Dog that inherits from Animal (use: class Dog(Animal):)
# Create a Dog instance with "Buddy" and "Canine"
# Call the inherited info() method
# Write your code here:


# TODO 7-8: Create a Cat child class
# Define Cat that inherits from Animal
# Create an instance with "Whiskers" and "Feline"
# Call both info() and make_sound() methods
# Write your code here:


# TODO 9-13: Create a Vehicle hierarchy with specialized classes
# Define Vehicle with __init__(self, brand, model, year)
# Add 'display_info' method that prints vehicle details
# Create Car child class with honk() method
# Create Motorcycle child class with rev_engine() method
# Create instances of both and call their unique methods
# Write your code here:


# BONUS TODO: Create a three-level inheritance hierarchy
# Example: Vehicle → ElectricVehicle → TeslaCar
# Each level adds new methods or attributes
# Write your code here:

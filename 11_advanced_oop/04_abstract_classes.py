"""
Mini-Program 4: Abstract Classes and Interfaces
Topic: Advanced OOP

Learning Objectives:
- Understand abstract base classes (ABC)
- Use the abc module and @abstractmethod decorator
- Create interfaces using abstract classes
- Enforce method implementation in subclasses

Instructions:
Complete this program to learn about abstract classes.
"""

# First, import the ABC module
from abc import ABC, abstractmethod

# TODO 1: Define an abstract class 'Shape' that inherits from ABC
# Add an abstract method 'area' (no implementation, just pass)
# Hint: class Shape(ABC):
#           @abstractmethod
#           def area(self):
#               pass
# Write your code here:


# TODO 2: Add another abstract method 'perimeter' to Shape
# Write your code here:


# TODO 3: Try to create an instance of Shape
# Use try-except to catch the TypeError
# Print the error message (you can't instantiate abstract classes)
# Write your code here:


# TODO 4: Define a concrete class 'Rectangle' that inherits from Shape
# Implement both abstract methods: area and perimeter
# __init__ should take width and height
# Write your code here:


# TODO 5: Create a Rectangle instance
# Call both area() and perimeter() methods
# Write your code here:


# TODO 6: Define another concrete class 'Circle' that inherits from Shape
# Implement both abstract methods
# __init__ should take radius
# Write your code here:


# TODO 7: Create a Circle instance
# Call both methods
# Write your code here:


# TODO 8: Define an abstract class 'Animal' with abstract methods:
# - 'make_sound' (no parameters besides self)
# - 'move' (no parameters besides self)
# Write your code here:


# TODO 9: Create concrete classes 'Dog' and 'Bird' that inherit from Animal
# Implement the abstract methods differently for each
# Dog: "Woof!" and "Running"
# Bird: "Chirp!" and "Flying"
# Write your code here:


# TODO 10: Create instances of Dog and Bird
# Call their methods to see the different implementations
# Write your code here:


# TODO 11: Create a function 'describe_animal' that takes an Animal parameter
# Call both make_sound() and move() on the animal
# This demonstrates polymorphism with abstract classes
# Write your code here:


# TODO 12: Test the describe_animal function with different animals
# Pass both Dog and Bird instances
# Write your code here:


# TODO 13: Define an abstract class 'PaymentMethod' with:
# - Abstract method 'process_payment' taking an amount
# - Concrete method 'validate_amount' that checks if amount > 0
# Write your code here:


# TODO 14: Create concrete classes 'CreditCard' and 'PayPal'
# Implement the abstract process_payment method differently
# Use the inherited validate_amount method
# Write your code here:


# TODO 15: Create instances and test payment processing
# Try to process a payment with valid and invalid amounts
# Write your code here:


# BONUS TODO: Create an abstract class 'Database' with abstract methods:
# connect, disconnect, query, insert
# Create concrete implementations: 'MySQLDatabase' and 'PostgreSQLDatabase'
# Write your code here:


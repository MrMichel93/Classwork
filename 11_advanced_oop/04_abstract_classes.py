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

# TODO 1-7: Create a Shape abstract base class and concrete shape implementations
# Build Shape(ABC) with abstract methods area() and perimeter()
# Show that Shape cannot be instantiated directly by catching the TypeError
# Build Rectangle and Circle as concrete subclasses with their own initializers and geometry methods
# Create instances and call area() and perimeter() on each
# Hint: class Shape(ABC): @abstractmethod def area(self): ...
# Hint: class Rectangle(Shape): def __init__(self, width, height): ...
# Hint: class Circle(Shape): def __init__(self, radius): ...
# Write your code here:


# TODO 8-12: Create an Animal abstract base class and use polymorphism
# Build Animal(ABC) with abstract methods make_sound() and move()
# Build Dog and Bird with distinct implementations
# Create a describe_animal(animal) function that works with any Animal subclass
# Test the function with multiple animal objects
# Hint: class Animal(ABC): ...
# Hint: def describe_animal(animal): ...
# Write your code here:


# TODO 13-15: Create a PaymentMethod abstract base class with shared validation
# Build PaymentMethod(ABC) with abstract process_payment(amount) and concrete validate_amount(amount)
# Build CreditCard and PayPal subclasses that process payments in their own way
# Create instances and test both valid and invalid payment amounts
# Hint: class PaymentMethod(ABC): def validate_amount(self, amount): ...
# Write your code here:


# BONUS TODO: Create a Database abstract base class and concrete implementations
# Define abstract operations such as connect(), disconnect(), query(sql), and insert(data)
# Build at least two database subclasses with their own behavior
# Write your code here:

"""
Mini-Program 3: Magic Methods (Dunder Methods)
Topic: Advanced OOP

Learning Objectives:
- Understand special methods (magic/dunder methods)
- Override __str__ and __repr__ for string representation
- Implement comparison operators (__eq__, __lt__, etc.)
- Use arithmetic operator overloading

Instructions:
Complete this program to learn about magic methods in Python.
"""

# TODO 1-6: Create a Book class with representation and comparison magic methods
# Build Book with __init__(title, author, pages)
# Implement __str__ for a reader-friendly display and __repr__ for a developer-friendly representation
# Implement __eq__ so books compare by title and author
# Create Book instances and demonstrate print(), repr(), and == behavior
# Hint: class Book: def __init__(self, title, author, pages): ...
# Hint: def __str__(self): ...
# Hint: def __repr__(self): ...
# Hint: def __eq__(self, other): ...
# Write your code here:


# TODO 7-10: Create a Vector class with arithmetic operator overloading
# Build Vector with x and y coordinates
# Implement __add__ to combine two vectors and __mul__ for scalar multiplication
# Keep the operator hints: Vector(self.x + other.x, self.y + other.y) and Vector(self.x * scalar, self.y * scalar)
# Create vector examples and print the results of addition and multiplication
# Hint: class Vector: def __add__(self, other): ...
# Hint: def __mul__(self, scalar): ...
# Write your code here:


# TODO 11-12: Create a Rectangle class with comparison operators
# Build Rectangle with width and height
# Implement __lt__ and __gt__ so rectangles compare by area
# Create several rectangles, compare them, and sort a list of them
# Hint: class Rectangle: def __lt__(self, other): ...
# Write your code here:


# TODO 13-14: Create a ShoppingCart class that behaves like a container
# Build ShoppingCart with an internal items list
# Implement __len__, __getitem__, and __contains__ so the cart works with len(), indexing, and the in operator
# Add sample items and demonstrate each magic method in use
# Hint: class ShoppingCart: def __len__(self): ...
# Write your code here:


# BONUS TODO: Create a 2x2 Matrix class with arithmetic magic methods
# Implement __add__, __mul__, and __str__ to support matrix operations and readable output
# Write your code here:

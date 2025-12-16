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

# TODO 1: Define a class 'Book' with __init__ taking: title, author, pages
# Override __str__ to return a formatted string: "Title by Author (X pages)"
# Hint: def __str__(self):
#           return f"{self.title} by {self.author} ({self.pages} pages)"
# Write your code here:


# TODO 2: Create a Book instance and print it
# See how __str__ provides a nice string representation
# Write your code here:


# TODO 3: Override __repr__ in Book
# It should return a string that could recreate the object
# Example: "Book('Title', 'Author', 300)"
# Hint: def __repr__(self):
# Write your code here:


# TODO 4: Test __repr__ by using repr() on a Book instance
# Write your code here:


# TODO 5: Override __eq__ in Book to compare books by title and author
# Two books are equal if they have the same title and author
# Hint: def __eq__(self, other):
#           return self.title == other.title and self.author == other.author
# Write your code here:


# TODO 6: Create two Book instances with the same title and author
# Test if they are equal using ==
# Write your code here:


# TODO 7: Define a class 'Vector' representing a 2D vector with x and y
# Override __add__ to add two vectors
# Return a new Vector with the sum of x and y coordinates
# Hint: def __add__(self, other):
#           return Vector(self.x + other.x, self.y + other.y)
# Write your code here:


# TODO 8: Create two Vector instances and add them using +
# Example: v1 = Vector(1, 2), v2 = Vector(3, 4), v3 = v1 + v2
# Print the result
# Write your code here:


# TODO 9: Override __mul__ in Vector for scalar multiplication
# Multiply the vector by a number
# Example: Vector(2, 3) * 2 should give Vector(4, 6)
# Write your code here:


# TODO 10: Test vector multiplication
# Write your code here:


# TODO 11: Define a class 'Rectangle' with width and height
# Override __lt__ (less than) to compare rectangles by area
# Override __gt__ (greater than) to compare by area
# Write your code here:


# TODO 12: Create several Rectangle instances
# Compare them using < and > operators
# Sort a list of rectangles
# Write your code here:


# TODO 13: Define a class 'ShoppingCart' with:
# - __init__ creating an empty items list
# - __len__ returning the number of items
# - __getitem__ to access items by index
# - __contains__ to check if an item exists (for 'in' operator)
# Write your code here:


# TODO 14: Test the ShoppingCart magic methods
# Add items, use len(), access items with [], use 'in' operator
# Write your code here:


# BONUS TODO: Create a class 'Matrix' representing a 2x2 matrix
# Implement __add__, __mul__ (matrix multiplication), and __str__
# Test matrix operations
# Write your code here:


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

# TODO 1: Define a parent class 'Shape' with:
# - __init__ taking 'name'
# - method 'area' that returns 0 (placeholder)
# - method 'description' that returns "This is a shape"
# Write your code here:


# TODO 2: Define a child class 'Rectangle' that inherits from Shape
# Override __init__ to take name, width, and height
# Call the parent's __init__ for name, then store width and height
# Hint: For now, don't use super(); we'll cover that next
# Write your code here:


# TODO 3: Override the 'area' method in Rectangle
# Make it return width * height
# Write your code here:


# TODO 4: Create a Rectangle instance
# Print its area using the overridden method
# Write your code here:


# TODO 5: Define another child class 'Circle' that inherits from Shape
# Override __init__ to take name and radius
# Override 'area' to return 3.14159 * radius * radius
# Write your code here:


# TODO 6: Create a Circle instance
# Print its area
# Write your code here:


# TODO 7: Define a parent class 'Animal' with:
# - __init__ taking 'name'
# - method 'speak' that returns "Some sound"
# Write your code here:


# TODO 8: Create child classes Dog, Cat, and Cow
# Each should override the 'speak' method
# Dog returns "Woof!", Cat returns "Meow!", Cow returns "Moo!"
# Write your code here:


# TODO 9: Create instances of Dog, Cat, and Cow
# Call speak() on each to see the different overridden behaviors
# Write your code here:


# TODO 10: Create a list containing all three animal instances
# Loop through and print each animal's name and sound
# Write your code here:


# TODO 11: Define a parent class 'Employee' with:
# - __init__ taking name and salary
# - method 'calculate_bonus' returning salary * 0.1 (10%)
# Write your code here:


# TODO 12: Create a child class 'Manager' that inherits from Employee
# Override 'calculate_bonus' to return salary * 0.2 (20%)
# Write your code here:


# TODO 13: Create instances of both Employee and Manager with the same salary
# Print their bonuses to see the difference due to overriding
# Write your code here:


# BONUS TODO: Override the __str__ method in a custom class
# This method is called when you use print() or str() on an object
# Create a Person class and override __str__ to return a formatted string
# Write your code here:


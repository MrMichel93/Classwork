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

# TODO 1: Define a class 'Pizza' with:
# - Class attribute 'restaurant' = "Python Pizza"
# - __init__ with parameters: size, toppings (list)
# Write your code here:


# TODO 2: Add a class method 'margherita' to Pizza
# Use @classmethod decorator
# It should create and return a Pizza with size "Medium" and toppings ["cheese", "tomato"]
# Hint: @classmethod
#       def margherita(cls):
#           return cls("Medium", ["cheese", "tomato"])
# Write your code here:


# TODO 3: Add another class method 'pepperoni' to Pizza
# It should create a Pizza with size "Large" and toppings ["cheese", "pepperoni"]
# Write your code here:


# TODO 4: Create Pizza instances using the class methods
# Create one using Pizza.margherita()
# Create one using Pizza.pepperoni()
# Print their sizes and toppings
# Write your code here:


# TODO 5: Add a static method 'validate_size' to Pizza
# Use @staticmethod decorator
# It should take a size parameter and return True if it's "Small", "Medium", or "Large"
# Otherwise return False
# Hint: @staticmethod
#       def validate_size(size):
# Write your code here:


# TODO 6: Test the static method
# Call Pizza.validate_size("Medium") - should return True
# Call Pizza.validate_size("Huge") - should return False
# Print the results
# Write your code here:


# TODO 7: Define a class 'Date' with:
# - __init__ taking day, month, year
# - Add a class method 'from_string' that takes a date string like "15-03-2024"
#   and creates a Date instance by parsing the string
# Hint: Use string.split("-") to parse
# Write your code here:


# TODO 8: Test the from_string class method
# Create a Date instance using Date.from_string("25-12-2024")
# Print the day, month, and year
# Write your code here:


# TODO 9: Add a static method 'is_leap_year' to Date
# It should take a year and return True if it's a leap year
# Leap year rules: divisible by 4, except centuries unless divisible by 400
# Write your code here:


# TODO 10: Test the is_leap_year static method
# Test with years: 2024 (True), 2023 (False), 2000 (True), 1900 (False)
# Write your code here:


# TODO 11: Define a class 'MathOperations' with only static methods:
# - 'add' that returns the sum of two numbers
# - 'multiply' that returns the product of two numbers
# - 'power' that returns first number raised to the second
# Write your code here:


# TODO 12: Use the MathOperations static methods
# Call all three methods with different values
# Note: You don't need to create an instance
# Write your code here:


# TODO 13: Create a class 'Counter' with:
# - Class attribute 'count' = 0
# - Class method 'increment' that increases count by 1
# - Class method 'get_count' that returns the current count
# - Class method 'reset' that sets count back to 0
# Write your code here:


# BONUS TODO: Create a class 'Employee' with multiple factory class methods
# Example: from_string, from_dict, from_json
# Each method should parse different input formats and create an Employee
# Write your code here:


"""
Mini-Program 1: Properties and Getters/Setters
Topic: Advanced OOP

Learning Objectives:
- Understand the @property decorator
- Create getters and setters for controlled attribute access
- Use properties to validate and process data
- Implement computed properties

Instructions:
Complete this program to learn about properties in Python.
"""

# TODO 1: Define a class 'Temperature' with a private attribute _celsius
# Initialize _celsius to 0 in __init__
# Hint: Use self._celsius (underscore prefix for "private")
# Write your code here:


# TODO 2: Add a property getter for celsius
# Use @property decorator
# The method should return self._celsius
# Hint: @property
#       def celsius(self):
#           return self._celsius
# Write your code here:


# TODO 3: Add a property setter for celsius
# Use @celsius.setter decorator
# The setter should validate that the value is above -273.15 (absolute zero)
# If invalid, raise ValueError
# Write your code here:


# TODO 4: Create a Temperature instance
# Try setting the celsius property to 25
# Print the celsius value
# Write your code here:


# TODO 5: Try setting an invalid temperature (below -273.15)
# Use try-except to catch the ValueError
# Write your code here:


# TODO 6: Add a computed property 'fahrenheit' to Temperature
# It should calculate and return celsius converted to Fahrenheit
# Formula: (celsius * 9/5) + 32
# This is a read-only property (no setter needed)
# Write your code here:


# TODO 7: Test the fahrenheit property
# Set celsius to 0, print fahrenheit (should be 32)
# Set celsius to 100, print fahrenheit (should be 212)
# Write your code here:


# TODO 8: Define a class 'BankAccount' with:
# - Private attribute _balance initialized to 0
# - Property getter for balance (read-only)
# Write your code here:


# TODO 9: Add a method 'deposit' to BankAccount
# It should add to _balance only if amount is positive
# Write your code here:


# TODO 10: Add a method 'withdraw' to BankAccount
# It should subtract from _balance only if:
# - Amount is positive
# - Balance is sufficient
# Return True if successful, False otherwise
# Write your code here:


# TODO 11: Create a BankAccount instance
# Make several deposits and withdrawals
# Try to access balance property (should work)
# Try to directly set balance (should not work - read-only)
# Write your code here:


# TODO 12: Define a class 'Person' with private attributes for:
# - _name
# - _age
# Create property getters and setters for both
# Age setter should validate age is between 0 and 150
# Write your code here:


# TODO 13: Create a Person instance
# Test the property setters with valid and invalid values
# Write your code here:


# BONUS TODO: Create a class 'Rectangle' with private _width and _height
# Add properties for width and height with validation (must be positive)
# Add a computed property 'area' that returns width * height
# Add a computed property 'perimeter' that returns 2 * (width + height)
# Write your code here:


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

# TODO 1-7: Create a Temperature class with property getters, setters, and computed properties
# Define Temperature with private _celsius attribute (init to 0)
# Add @property getter for celsius
# Add @celsius.setter that validates >= -273.15 (raises ValueError if invalid)
# Add read-only @property for fahrenheit that computes: (celsius * 9/5) + 32
# Create an instance, set celsius to 25, print it
# Try setting invalid temperature (< -273.15) with try-except
# Test fahrenheit conversions (0°C = 32°F, 100°C = 212°F)
# Hint: @property and @attribute.setter decorators
# Write your code here:


# TODO 8-11: Create a BankAccount class with controlled access and operations
# Define BankAccount with private _balance (init to 0)
# Add property getter for balance (read-only - no setter)
# Add 'deposit' method that adds only if amount > 0
# Add 'withdraw' method that subtracts only if amount > 0 and sufficient funds (return True/False)
# Create an instance, make deposits/withdrawals, test access to balance
# Try to set balance directly (should fail)
# Write your code here:


# TODO 12-13: Create a Person class with validated properties
# Define Person with private _name and _age attributes
# Add @property getters and @attribute.setter setters for both
# Age setter should validate 0 ≤ age ≤ 150 (raise ValueError if invalid)
# Create an instance and test with valid and invalid values
# Write your code here:


# BONUS TODO: Create a Rectangle class with validation and computed properties
# Define with private _width and _height (must be positive via setters)
# Add properties for width and height with validation
# Add read-only computed properties: area (width * height) and perimeter (2 * (width + height))
# Write your code here:


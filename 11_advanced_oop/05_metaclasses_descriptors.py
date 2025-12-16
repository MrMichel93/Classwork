"""
Mini-Program 5: Metaclasses and Descriptors
Topic: Advanced OOP

Learning Objectives:
- Understand descriptors and their use cases
- Implement property validation with descriptors
- Explore class customization
- Create reusable property validators
- Master advanced Python OOP features

Instructions:
Complete this program exploring advanced OOP concepts like descriptors.
"""

# TODO 1: Create a simple descriptor for validation
# Create a PositiveNumber descriptor class
# Implements __get__, __set__, __set_name__
# Validates that value is positive when setting
# Write your code here:


# TODO 2: Use the descriptor in a class
# Create a Product class
# Use PositiveNumber descriptor for price attribute
# Try setting negative price (should raise error)
# Write your code here:


# TODO 3: Create a RangeValidator descriptor
# Validates that value is within min and max range
# Takes min_value and max_value in __init__
# Write your code here:


# TODO 4: Create a Person class using RangeValidator
# Use it for age (range 0-150)
# Test with valid and invalid values
# Write your code here:


# TODO 5: Create a TypeValidator descriptor
# Validates that value is of specific type
# Takes expected_type in __init__
# Write your code here:


# TODO 6: Create an Employee class
# Use TypeValidator for name (str), employee_id (int)
# Test type validation
# Write your code here:


# TODO 7: Create a StringLength descriptor
# Validates string length (min and max)
# Use for password validation
# Write your code here:


# TODO 8: Create a User class
# Use StringLength for username (3-20 chars) and password (8-50 chars)
# Test with various string lengths
# Write your code here:


# TODO 9: Create a computed property using descriptor
# Create a FullName descriptor
# Combines first_name and last_name
# Only implements __get__ (read-only property)
# Write your code here:


# TODO 10: Use FullName descriptor
# Create a Contact class with first_name, last_name, and full_name (descriptor)
# full_name should be automatically computed
# Write your code here:


# TODO 11: Create a Cached descriptor
# Implements caching for expensive computations
# Stores computed value after first call
# Write your code here:


# TODO 12: Use Cached descriptor
# Create a DataProcessor class
# Use Cached for an expensive_calculation property
# Call it multiple times, should only compute once
# Write your code here:


# TODO 13: Create a Logged descriptor
# Logs all access and modifications to a value
# Wraps another descriptor
# Write your code here:


# TODO 14: Create a class using multiple descriptor types
# Create a BankAccount class
# - account_number (TypeValidator for str)
# - balance (PositiveNumber)
# - owner_age (RangeValidator 18-150)
# Test all validations
# Write your code here:


# TODO 15: Create a class with class-level attributes tracking
# Use __init_subclass__ to track all subclasses
# Create a Vehicle base class
# Track all vehicle types created
# Write your code here:


# TODO 16: Create a ValidatedClass base class
# Automatically validates all attributes marked with validators
# Use class decorators or __init_subclass__
# Write your code here:


# TODO 17: Create a simple ORM-like descriptor
# Create a Field descriptor that represents database columns
# Create an IntField, StringField, DateField
# Each validates and formats data appropriately
# Write your code here:


# TODO 18: Create a Model base class
# Uses Field descriptors to represent database records
# Create a simple User model with id, name, email fields
# Demonstrate basic ORM-like behavior
# Write your code here:


# BONUS TODO: Create a complete validation framework
# Implement:
# - Multiple validator descriptors (email, phone, URL, etc.)
# - Validator chaining (multiple validators per field)
# - Custom error messages
# - Required vs optional fields
# - Default values
# Create example model classes using the framework
# This is very advanced!
# Write your code here:


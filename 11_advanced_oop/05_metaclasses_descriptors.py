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

# TODO 1-2: Create a PositiveNumber descriptor and use it in Product
# Build PositiveNumber with descriptor methods such as __get__, __set__, and __set_name__
# Use it in Product so positive values are accepted and invalid values raise an error
# Hint: class PositiveNumber: def __set_name__(self, owner, name): ...
# Hint: class Product: ...
# Write your code here:


# TODO 3-4: Create a RangeValidator descriptor and use it in Person
# Build RangeValidator(min_value, max_value) to keep values within a required range
# Use it for a Person age attribute and demonstrate both valid and invalid assignments
# Hint: class RangeValidator: def __init__(self, min_value, max_value): ...
# Write your code here:


# TODO 5-6: Create a TypeValidator descriptor and use it in Employee
# Build TypeValidator(expected_type) to enforce attribute types
# Use it in Employee for fields such as name and employee_id, then test type checking
# Hint: class TypeValidator: def __init__(self, expected_type): ...
# Write your code here:


# TODO 7-8: Create a StringLength descriptor and use it in User
# Build StringLength(min_length, max_length) for validating string sizes
# Use it for values such as username and password and test several edge cases
# Hint: class StringLength: def __init__(self, min_length, max_length): ...
# Write your code here:


# TODO 9-10: Create a computed descriptor for full names
# Build FullName as a read-only descriptor that combines first_name and last_name
# Use it in Contact so full_name is derived automatically from the stored names
# Hint: class FullName: def __get__(self, instance, owner): ...
# Write your code here:


# TODO 11-12: Create a caching descriptor and use it in DataProcessor
# Build Cached so a computed value is stored after first access
# Use it for an expensive_calculation attribute or property and show that repeated access reuses the cached value
# Hint: class Cached: def __get__(self, instance, owner): ...
# Write your code here:


# TODO 13-14: Create a logging descriptor and combine descriptor types in BankAccount
# Build Logged to wrap another descriptor and report reads or writes
# Build BankAccount with validated fields such as account_number, balance, and owner_age
# Demonstrate how multiple descriptors can enforce rules on one class
# Hint: class Logged: def __init__(self, descriptor): ...
# Write your code here:


# TODO 15-16: Create class-level customization helpers
# Build a Vehicle base class that tracks subclasses via __init_subclass__
# Build a ValidatedClass base that cooperates with validator-style attributes or setup hooks
# Show how new subclasses automatically participate in the tracking or validation system
# Hint: class Vehicle: def __init_subclass__(cls, **kwargs): ...
# Write your code here:


# TODO 17-18: Create a simple ORM-style field system
# Build a Field descriptor plus specialized field types such as IntField, StringField, and DateField
# Build a Model base class that uses those descriptors to represent record data
# Create a User model and demonstrate storing and validating field values
# Hint: class Field: ...
# Hint: class Model: ...
# Write your code here:


# BONUS TODO: Create a more complete validation framework with descriptors
# Extend the idea with additional validators, chaining, custom messages, optional fields, and defaults
# Create a few example models that use the framework
# Write your code here:

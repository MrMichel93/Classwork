"""
Mini-Program 2: Class Attributes
Topic: Basic OOP

Learning Objectives:
- Understand the difference between class and instance attributes
- Use class attributes for shared data
- Access class attributes from instances
- Modify class and instance attributes

Instructions:
Complete this program to learn about class vs instance attributes.
"""

# TODO 1: Define a class called 'Car' with a class attribute
# Add a class attribute 'wheels' set to 4 (all cars have 4 wheels)
# Also add an __init__ method with parameters: make, model
# Hint: class Car:
#           wheels = 4
#           def __init__(self, make, model):
# Write your code here:


# TODO 2: Create two Car instances with different makes and models
# Example: car1 = Car("Toyota", "Camry")
# Write your code here:


# TODO 3: Print the wheels attribute for both cars
# Access it using car1.wheels and car2.wheels
# Notice they both have 4 wheels (shared class attribute)
# Write your code here:


# TODO 4: Print the make and model for both cars
# These are instance attributes (different for each car)
# Write your code here:


# TODO 5: Access the class attribute using the class name
# Print Car.wheels
# Write your code here:


# TODO 6: Define a class 'BankAccount' with:
# - Class attribute 'bank_name' = "Python Bank"
# - Instance attributes: account_holder, balance (set in __init__)
# Write your code here:


# TODO 7: Create two BankAccount instances with different holders and balances
# Write your code here:


# TODO 8: Print the bank_name for both accounts (should be the same)
# Print the account holders (should be different)
# Write your code here:


# TODO 9: Change the class attribute through the class
# Set BankAccount.bank_name = "New Python Bank"
# Print the bank_name from both account instances
# Notice how it changes for all instances
# Write your code here:


# TODO 10: Create a class 'Student' with:
# - Class attribute 'school' = "Python High School"
# - Class attribute 'total_students' = 0 (we'll increment this)
# - Instance attributes: name, grade (from __init__)
# Write your code here:


# TODO 11: Modify the __init__ method to increment total_students
# Each time a Student is created, add 1 to Student.total_students
# Hint: Student.total_students += 1
# Write your code here:


# TODO 12: Create three Student instances
# Print Student.total_students after creating all three
# It should show 3
# Write your code here:


# BONUS TODO: Create a class that tracks the number of instances created
# Use a class attribute as a counter
# Create several instances and print the total count
# Write your code here:


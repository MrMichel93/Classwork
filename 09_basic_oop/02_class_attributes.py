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

# Student Self-Check
# Run: python3 -m unittest starter_tests.test_09_basic_oop.BasicOOPSelfChecks.test_class_attributes
# Expect: every Car reports 4 wheels; BankAccount starts with "Python Bank";
# making a Student increases Student.total_students.

# TODO 1-5: Create a Car class with class and instance attributes
# Define Car with class attribute 'wheels' = 4
# Add __init__(self, make, model) for instance attributes
# Create two Car instances and print wheels (should be 4 for both)
# Print make/model for each (should be different)
# Also access wheels through the class name (Car.wheels)
# Hint: class Car: wheels = 4; def __init__(self, make, model):
# Write your code here:


# TODO 6-9: Create a BankAccount class with shared and unique attributes
# Define BankAccount with class attribute 'bank_name' = "Python Bank"
# Add instance attributes: account_holder, balance
# Create two instances and print bank_name (same) and account holders (different)
# Change the class attribute and observe it affects all instances
# Write your code here:


# TODO 10-12: Create a Student class that tracks total enrollment
# Define Student with class attributes: 'school' = "Python High School", 'total_students' = 0
# Add instance attributes: name, grade
# In __init__, increment Student.total_students by 1 for each new student
# Create three instances and print Student.total_students (should be 3)
# Hint: Student.total_students += 1
# Write your code here:


# BONUS TODO: Create a counter class
# Use a class attribute to count how many instances have been created
# Create several instances and display the total count
# Write your code here:

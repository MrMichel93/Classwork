"""
Mini-Program 3: Using super()
Topic: Intermediate OOP

Learning Objectives:
- Understand the purpose of super()
- Use super() to call parent class methods
- Extend parent class functionality without duplicating code
- Work with super() in __init__ methods

Instructions:
Complete this program to learn about the super() function.
"""

# TODO 1: Define a parent class 'Person' with:
# - __init__ taking name and age
# - method 'introduce' that prints "Hi, I'm {name}, {age} years old"
# Write your code here:


# TODO 2: Define a child class 'Student' that inherits from Person
# Override __init__ to take name, age, and student_id
# Use super().__init__(name, age) to call the parent's __init__
# Then store student_id as an instance attribute
# Write your code here:


# TODO 3: Create a Student instance
# Call the introduce() method (inherited from Person)
# Print the student_id
# Write your code here:


# TODO 4: Override the 'introduce' method in Student
# Use super().introduce() to call the parent's version
# Then add an additional print statement for the student_id
# Write your code here:


# TODO 5: Create a Student instance and call introduce()
# See how it uses both the parent's and child's code
# Write your code here:


# TODO 6: Define a parent class 'Vehicle' with:
# - __init__ taking brand and model
# - method 'start' that prints "Vehicle starting"
# Write your code here:


# TODO 7: Define a child class 'ElectricCar' that inherits from Vehicle
# Override __init__ to take brand, model, and battery_capacity
# Use super() to initialize brand and model
# Store battery_capacity as an instance attribute
# Write your code here:


# TODO 8: Override the 'start' method in ElectricCar
# Use super().start() to call the parent's start method
# Then print "Electric motor engaged"
# Write your code here:


# TODO 9: Create an ElectricCar instance
# Call the start() method to see both messages
# Write your code here:


# TODO 10: Define a parent class 'BankAccount' with:
# - __init__ taking account_number and balance
# - method 'deposit' that adds to balance
# Write your code here:


# TODO 11: Define a child class 'SavingsAccount' that inherits from BankAccount
# Override 'deposit' to:
# - Call super().deposit(amount) to do the regular deposit
# - Add interest: self.balance *= 1.01 (1% interest)
# - Print "Interest applied"
# Write your code here:


# TODO 12: Create a SavingsAccount instance
# Make several deposits and see how interest is applied each time
# Print the final balance
# Write your code here:


# BONUS TODO: Create a three-level inheritance hierarchy
# Use super() in each level to build upon the parent's functionality
# Example: Animal -> Mammal -> Dog
# Each level adds more specific behavior while calling parent methods
# Write your code here:


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

# Student Self-Check
# Run: python3 -m unittest starter_tests.test_10_intermediate_oop.IntermediateOOPSelfChecks.test_super_function
# Expect: Student is a Person; ElectricCar keeps battery capacity; depositing $50
# into $100 SavingsAccount leaves a $151.50 balance after interest.

# TODO 1-5: Create a Person/Student hierarchy that uses super()
# Build Person with __init__(name, age) and introduce()
# Build Student(Person) with __init__(name, age, student_id)
# Override introduce() so it reuses Person behavior before adding student details
# Create Student examples that first use the inherited introduction and then the overridden one
# Hint: class Person: def __init__(self, name, age): ...
# Hint: class Student(Person): def __init__(self, name, age, student_id): ...
# Hint: def introduce(self): ...
# Write your code here:


# TODO 6-9: Create a Vehicle/ElectricCar example that extends parent behavior
# Build Vehicle with __init__(brand, model) and start()
# Build ElectricCar(Vehicle) with __init__(brand, model, battery_capacity)
# Override start() so it keeps the parent start message and adds electric-specific output
# Create an ElectricCar instance and call start() to show both layers working together
# Hint: class Vehicle: def __init__(self, brand, model): ...
# Hint: class ElectricCar(Vehicle): def __init__(self, brand, model, battery_capacity): ...
# Write your code here:


# TODO 10-12: Create a BankAccount/SavingsAccount hierarchy with an overridden deposit
# Build BankAccount with __init__(account_number, balance) and deposit(amount)
# Build SavingsAccount(BankAccount) that reuses the base deposit and then applies interest
# Keep the interest formula hint: self.balance *= 1.01
# Create a savings account, make deposits, and print the resulting balance
# Hint: class BankAccount: def __init__(self, account_number, balance): ...
# Hint: class SavingsAccount(BankAccount): def deposit(self, amount): ...
# Write your code here:


# BONUS TODO: Create a three-level inheritance hierarchy that chains super() calls
# Build three related classes where each level adds behavior while reusing the parent implementation
# Hint: class Animal: ... / class Mammal(Animal): ... / class Dog(Mammal): ...
# Write your code here:

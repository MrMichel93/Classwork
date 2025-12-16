"""
Mini-Program 5: Polymorphism and Interface Design
Topic: Intermediate OOP

Learning Objectives:
- Master polymorphic behavior
- Design interface-like classes
- Use duck typing effectively
- Implement method overriding strategically
- Create flexible, extensible code

Instructions:
Complete this program exploring polymorphism and interface patterns.
"""

# TODO 1: Create a Shape base class (interface-like)
# Methods: area(), perimeter(), describe()
# These should return 0 or "Unknown shape" (will be overridden)
# Write your code here:


# TODO 2: Create Circle, Rectangle, Triangle classes
# All inherit from Shape
# Override area() and perimeter() with proper formulas
# Override describe() with specific descriptions
# Write your code here:


# TODO 3: Demonstrate polymorphism
# Create list of different shapes
# Loop through and call area() on each
# Even though they're different classes, same method name works!
# Write your code here:


# TODO 4: Create a function that works with any shape
# def calculate_total_area(shapes):
#     # Calculate sum of areas for all shapes
# This demonstrates polymorphism - function works with any Shape subclass
# Write your code here:


# TODO 5: Create a Payment interface (base class)
# Methods: process_payment(amount), refund(amount), get_details()
# Write your code here:


# TODO 6: Create payment method classes
# CreditCard, PayPal, Bitcoin - all inherit from Payment
# Each implements process_payment() differently
# Write your code here:


# TODO 7: Create a PaymentProcessor class
# Method: process_transaction(payment_method, amount)
# Works with any Payment subclass (polymorphism)
# Write your code here:


# TODO 8: Test payment processing with different methods
# Create instances of different payment types
# Process payments using PaymentProcessor
# Demonstrate same interface, different behavior
# Write your code here:


# TODO 9: Create an Animal base class
# Methods: make_sound(), move(), eat()
# Write your code here:


# TODO 10: Create specific animal classes
# Dog, Cat, Bird, Fish - all inherit from Animal
# Each overrides methods with specific behaviors
# Dog: "Bark", "Run"
# Cat: "Meow", "Walk"
# Bird: "Chirp", "Fly"
# Fish: "Bubble", "Swim"
# Write your code here:


# TODO 11: Create a Zoo class
# Manages list of animals
# Methods:
# - add_animal(animal)
# - feed_all_animals() - calls eat() on each
# - make_all_sounds() - calls make_sound() on each
# Demonstrates polymorphism with different animals
# Write your code here:


# TODO 12: Create a Database interface
# Methods: connect(), disconnect(), query(sql), insert(data)
# Write your code here:


# TODO 13: Create specific database implementations
# MySQLDatabase, PostgreSQLDatabase, SQLiteDatabase
# Each implements methods differently
# Simulate different connection strings and behaviors
# Write your code here:


# TODO 14: Create a DataManager class
# Works with any Database subclass
# Method: migrate_data(source_db, target_db)
# Reads from source, writes to target
# Works regardless of database type (polymorphism)
# Write your code here:


# TODO 15: Demonstrate duck typing
# Create classes that don't inherit from same base but have same methods
# If it walks like a duck and quacks like a duck...
# Create: EmailNotifier, SMSNotifier, PushNotifier
# All have send(message) method
# Create function that works with any notifier
# Write your code here:


# TODO 16: Create a Vehicle base class
# Methods: start(), stop(), accelerate(speed), brake()
# Write your code here:


# TODO 17: Create vehicle type classes with different behaviors
# Car, Motorcycle, Truck, Bicycle
# Each implements methods differently
# Bicycle might not have start() (human powered)
# Handle this appropriately
# Write your code here:


# TODO 18: Create a TrafficSimulator
# Manages multiple vehicles
# Methods:
# - add_vehicle(vehicle)
# - start_all()
# - simulate_traffic()
# Calls methods on all vehicles polymorphically
# Write your code here:


# BONUS TODO: Create a plugin system
# Design a Plugin base class with load(), execute(), unload()
# Create several plugin implementations
# Create PluginManager that:
# - Loads plugins dynamically
# - Executes plugins
# - Works with any plugin type
# This demonstrates real-world polymorphism use case
# Write your code here:


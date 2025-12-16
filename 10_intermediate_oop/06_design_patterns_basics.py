"""
Mini-Program 6: Introduction to Design Patterns
Topic: Intermediate OOP

Learning Objectives:
- Understand basic design patterns
- Implement Singleton, Factory, and Observer patterns
- Apply design patterns to solve common problems
- Create flexible and maintainable code
- Recognize when to use specific patterns

Instructions:
Complete this introduction to design patterns. This is the most
challenging intermediate OOP program!
"""

# TODO 1: Implement Singleton pattern
# Create a DatabaseConnection class that:
# - Only allows one instance to exist
# - Returns same instance on multiple creations
# - Store instance as class variable
# - Override __new__ method
# Write your code here:


# TODO 2: Test Singleton pattern
# Try to create multiple instances
# Verify they're all the same object (use 'is' operator)
# Write your code here:


# TODO 3: Implement Factory pattern
# Create a ShapeFactory class
# Method: create_shape(shape_type) returns appropriate shape object
# shape_type can be 'circle', 'rectangle', 'triangle'
# Factory decides which class to instantiate
# Write your code here:


# TODO 4: Test Factory pattern
# Use factory to create different shapes
# User doesn't need to know about specific shape classes
# Write your code here:


# TODO 5: Implement Observer pattern - Subject class
# Create a WeatherStation class (the subject)
# Attributes: temperature, observers (list)
# Methods:
# - attach(observer) - add observer
# - detach(observer) - remove observer
# - notify() - notify all observers of change
# - set_temperature(temp) - update temp and notify
# Write your code here:


# TODO 6: Implement Observer pattern - Observer classes
# Create observer classes:
# - PhoneDisplay - displays on phone
# - WebDisplay - displays on website
# - EmailAlert - sends email if temp extreme
# Each has update(temperature) method
# Write your code here:


# TODO 7: Test Observer pattern
# Create weather station
# Create and attach multiple observers
# Change temperature
# See all observers get notified automatically
# Write your code here:


# TODO 8: Implement Strategy pattern
# Create different sorting strategies
# Base class: SortStrategy with method sort(data)
# Implementations: BubbleSort, QuickSort, MergeSort
# Write your code here:


# TODO 9: Create Sorter class that uses strategies
# Attributes: strategy (SortStrategy)
# Methods:
# - set_strategy(strategy)
# - sort_data(data) - uses current strategy
# Can change strategy at runtime
# Write your code here:


# TODO 10: Test Strategy pattern
# Create sorter
# Try different strategies on same data
# Show that behavior changes based on strategy
# Write your code here:


# TODO 11: Implement Builder pattern
# Create a Computer class with many optional components
# Create ComputerBuilder class with methods:
# - set_cpu(cpu)
# - set_ram(ram)
# - set_storage(storage)
# - set_gpu(gpu)
# - build() - returns configured Computer
# Allows step-by-step object construction
# Write your code here:


# TODO 12: Test Builder pattern
# Build different computer configurations
# Show how builder makes complex object creation easier
# Write your code here:


# TODO 13: Implement Adapter pattern
# Create OldPrinter class with method print_document(text)
# Create NewPrinter class with method print(text, color, duplex)
# Create PrinterAdapter that adapts NewPrinter to OldPrinter interface
# Write your code here:


# TODO 14: Test Adapter pattern
# Create function that works with OldPrinter interface
# Use adapter to make NewPrinter work with old interface
# Write your code here:


# TODO 15: Implement Decorator pattern
# Create a Coffee class with cost() and description()
# Create decorator classes:
# - MilkDecorator
# - SugarDecorator
# - WhipDecorator
# Each adds to cost and description
# Decorators wrap Coffee objects
# Write your code here:


# TODO 16: Test Decorator pattern
# Create plain coffee
# Add decorators dynamically
# Each decorator adds features without modifying Coffee class
# Write your code here:


# TODO 17: Implement Command pattern
# Create Command base class with execute() and undo()
# Create specific commands:
# - LightOnCommand, LightOffCommand
# - FanHighCommand, FanLowCommand
# Create RemoteControl class that stores and executes commands
# Write your code here:


# TODO 18: Test Command pattern
# Configure remote with different commands
# Execute commands
# Demonstrate undo functionality
# Write your code here:


# TODO 19: Implement State pattern
# Create a VendingMachine with states:
# - NoMoneyState
# - HasMoneyState
# - DispensingState
# Each state handles insertMoney(), selectItem() differently
# Machine changes state based on actions
# Write your code here:


# TODO 20: Test State pattern
# Create vending machine
# Perform various actions
# See how behavior changes based on state
# Write your code here:


# BONUS TODO: Combine multiple patterns
# Create a complete application that uses:
# - Singleton for configuration manager
# - Factory for creating different types of users
# - Observer for notification system
# - Strategy for different authentication methods
# This demonstrates how patterns work together!
# Write your code here:


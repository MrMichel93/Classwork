"""
Mini-Program 4: Multiple Inheritance
Topic: Intermediate OOP

Learning Objectives:
- Understand multiple inheritance in Python
- Create classes that inherit from multiple parents
- Use multiple inheritance to combine functionality
- Understand the method resolution order (MRO)

Instructions:
Complete this program to learn about multiple inheritance.
"""

# TODO 1-4: Create capability mixins and combine them in Duck
# Build Flyable with fly() and Swimmable with swim()
# Build Duck(Flyable, Swimmable) with __init__(name)
# Create a Duck instance and demonstrate both inherited capabilities
# Hint: class Duck(Flyable, Swimmable): def __init__(self, name): ...
# Write your code here:


# TODO 5-7: Create another multiple-inheritance example with Dog
# Build Walkable with walk()
# Build Dog(Walkable, Swimmable) with __init__(name)
# Create a Dog instance, use the supported abilities, and observe what capability it does not inherit
# Hint: class Dog(Walkable, Swimmable): def __init__(self, name): ...
# Write your code here:


# TODO 8-10: Create a HybridCar that combines two fuel-system behaviors
# Build Electric with charge() and Gasoline with refuel()
# Build HybridCar(Electric, Gasoline) with __init__(model)
# Create a HybridCar instance and show that it can use both behaviors
# Hint: class HybridCar(Electric, Gasoline): def __init__(self, model): ...
# Write your code here:


# TODO 11-13: Create a TechLead role and inspect method resolution order
# Build Developer with write_code() and Manager with manage_team()
# Build TechLead(Developer, Manager) and demonstrate both role behaviors
# Print HybridCar.__mro__ to examine the order Python searches for inherited methods
# Hint: class TechLead(Developer, Manager): ...
# Write your code here:


# BONUS TODO: Create a larger multiple-inheritance example using capability classes
# Combine several small behavior classes into one object and demonstrate each inherited feature
# Hint: class FileManager(Readable, Writable, Executable, Deletable): ...
# Write your code here:

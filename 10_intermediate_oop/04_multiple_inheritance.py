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

# TODO 1: Define a class 'Flyable' with a method 'fly'
# The fly method should print "Flying through the air"
# Write your code here:


# TODO 2: Define a class 'Swimmable' with a method 'swim'
# The swim method should print "Swimming in water"
# Write your code here:


# TODO 3: Define a class 'Duck' that inherits from both Flyable and Swimmable
# Hint: class Duck(Flyable, Swimmable):
# Add an __init__ method that takes 'name'
# Write your code here:


# TODO 4: Create a Duck instance
# Call both fly() and swim() methods
# Notice how Duck has capabilities from both parent classes
# Write your code here:


# TODO 5: Define a class 'Walkable' with a method 'walk'
# The walk method should print "Walking on land"
# Write your code here:


# TODO 6: Define a class 'Dog' that inherits from Walkable and Swimmable
# Dogs can walk and swim, but not fly
# Add an __init__ method that takes 'name'
# Write your code here:


# TODO 7: Create a Dog instance
# Call walk() and swim() methods
# Try to call fly() - it should cause an error (dogs don't fly!)
# Write your code here:


# TODO 8: Define two classes: 'Electric' and 'Gasoline'
# Electric has method 'charge' that prints "Charging battery"
# Gasoline has method 'refuel' that prints "Filling gas tank"
# Write your code here:


# TODO 9: Define a class 'HybridCar' that inherits from both Electric and Gasoline
# Add an __init__ method that takes 'model'
# Write your code here:


# TODO 10: Create a HybridCar instance
# Call both charge() and refuel() methods
# This represents a car with both capabilities
# Write your code here:


# TODO 11: Define classes for different employee roles:
# - 'Developer' with method 'write_code'
# - 'Manager' with method 'manage_team'
# Then create 'TechLead' that inherits from both
# Write your code here:


# TODO 12: Create a TechLead instance
# Call both write_code() and manage_team()
# This represents someone with both technical and managerial skills
# Write your code here:


# TODO 13: Use the __mro__ attribute to see the method resolution order
# Print HybridCar.__mro__ to understand the order Python searches for methods
# Write your code here:


# BONUS TODO: Create a complex multiple inheritance scenario
# Define 4 different capability classes (like Readable, Writable, Executable, Deletable)
# Create a class that inherits from multiple capabilities
# Demonstrate using all inherited methods
# Write your code here:


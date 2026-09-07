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

# TODO 1-2: Implement and demonstrate the Singleton pattern
# Build DatabaseConnection so repeated construction returns the same instance
# Keep the __new__ hint without providing the full implementation
# Create multiple instances and verify they refer to the same object with the is operator
# Hint: class DatabaseConnection: def __new__(cls, *args, **kwargs): ...
# Write your code here:


# TODO 3-4: Implement and demonstrate the Factory pattern
# Build ShapeFactory with create_shape(shape_type) to return the appropriate shape object
# Support shape types such as circle, rectangle, and triangle without exposing creation details to the caller
# Hint: class ShapeFactory: def create_shape(self, shape_type): ...
# Write your code here:


# TODO 5-7: Implement and demonstrate the Observer pattern
# Build WeatherStation with temperature state plus attach(observer), detach(observer), notify(), and set_temperature(temp)
# Build observer classes such as PhoneDisplay, WebDisplay, and EmailAlert with update(temperature)
# Create a station, attach observers, and show them reacting when the temperature changes
# Hint: class WeatherStation: def set_temperature(self, temp): ...
# Write your code here:


# TODO 8-10: Implement and demonstrate the Strategy pattern
# Build SortStrategy with sort(data), then create multiple strategy classes with different sorting behavior
# Build Sorter with set_strategy(strategy) and sort_data(data) so the active algorithm can change at runtime
# Create one sorter and run the same data through different strategies
# Hint: class Sorter: def sort_data(self, data): ...
# Write your code here:


# TODO 11-12: Implement and demonstrate the Builder pattern
# Build Computer and ComputerBuilder so a computer can be assembled step by step
# Include configuration methods such as set_cpu(cpu), set_ram(ram), set_storage(storage), set_gpu(gpu), and build()
# Create multiple finished computer configurations to show the builder's flexibility
# Hint: class ComputerBuilder: def build(self): ...
# Write your code here:


# TODO 13-14: Implement and demonstrate the Adapter pattern
# Build OldPrinter with print_document(text) and NewPrinter with print(text, color, duplex)
# Build PrinterAdapter so code expecting the old interface can still use a new printer
# Create a function that depends on the old interface and pass it an adapted new printer
# Hint: class PrinterAdapter: def print_document(self, text): ...
# Write your code here:


# TODO 15-16: Implement and demonstrate the Decorator pattern
# Build Coffee with cost() and description()
# Build decorators such as MilkDecorator, SugarDecorator, and WhipDecorator that wrap a coffee object
# Keep the focus on dynamically adding features and updating both cost and description
# Hint: class MilkDecorator: def cost(self): ... / def description(self): ...
# Write your code here:


# TODO 17-18: Implement and demonstrate the Command pattern
# Build a Command base class with execute() and undo()
# Build command objects for device actions and a RemoteControl that stores and runs commands
# Configure the remote, execute commands, and demonstrate undo behavior
# Hint: class RemoteControl: ...
# Write your code here:


# TODO 19-20: Implement and demonstrate the State pattern
# Build a VendingMachine with state objects such as NoMoneyState, HasMoneyState, and DispensingState
# Let each state define how actions like insertMoney() and selectItem() behave
# Create a machine, perform actions, and show how the response changes as the current state changes
# Hint: class VendingMachine: ...
# Write your code here:


# BONUS TODO: Combine several patterns in one small application
# Use a few patterns together, such as Singleton, Factory, Observer, and Strategy, to show how they complement each other
# Write your code here:

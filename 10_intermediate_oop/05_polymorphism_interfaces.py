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

# Student Self-Check
# Run: python3 -m unittest starter_tests.test_10_intermediate_oop.IntermediateOOPSelfChecks.test_polymorphism_interfaces
# Expect: a circle plus 3-by-4 rectangle area is about 15.14159; PayPal processes
# through PaymentProcessor; Bicycle.start() reports beginning to pedal.

# TODO 1-4: Create a Shape interface-like hierarchy and use polymorphism
# Build Shape with area(), perimeter(), and describe()
# Build Circle, Rectangle, and Triangle as Shape subclasses with their own formulas and descriptions
# Create a mixed list of shapes and a calculate_total_area(shapes) function that works with all of them
# Keep formula hints without full implementations, such as width * height and 3.14159 * radius * radius
# Hint: class Shape: def area(self): ... / def perimeter(self): ... / def describe(self): ...
# Hint: def calculate_total_area(shapes): ...
# Write your code here:


# TODO 5-8: Create a payment interface and processor
# Build Payment with process_payment(amount), refund(amount), and get_details()
# Build CreditCard, PayPal, and Bitcoin to provide payment-specific behavior
# Build PaymentProcessor with process_transaction(payment_method, amount)
# Create several payment objects and process transactions through the shared interface
# Hint: class Payment: def process_payment(self, amount): ...
# Hint: class PaymentProcessor: def process_transaction(self, payment_method, amount): ...
# Write your code here:


# TODO 9-11: Create an Animal hierarchy and a Zoo manager
# Build Animal with make_sound(), move(), and eat()
# Build Dog, Cat, Bird, and Fish with distinct sound and movement behavior
# Build Zoo with add_animal(animal), feed_all_animals(), and make_all_sounds()
# Use the zoo to show the same method calls working across different animal types
# Hint: class Zoo: def add_animal(self, animal): ...
# Write your code here:


# TODO 12-15: Create database abstractions and a duck-typed notifier example
# Build Database with connect(), disconnect(), query(sql), and insert(data)
# Build MySQLDatabase, PostgreSQLDatabase, and SQLiteDatabase with database-specific behavior
# Build DataManager with migrate_data(source_db, target_db) that works with any database implementation
# Build notifier classes such as EmailNotifier, SMSNotifier, and PushNotifier that all provide send(message)
# Create a function that accepts any object with a send(message) method and uses it without requiring inheritance
# Hint: class Database: def query(self, sql): ...
# Hint: class DataManager: def migrate_data(self, source_db, target_db): ...
# Hint: def notify_user(notifier, message): ...
# Write your code here:


# TODO 16-18: Create a Vehicle hierarchy and traffic simulator
# Build Vehicle with start(), stop(), accelerate(speed), and brake()
# Build Car, Motorcycle, Truck, and Bicycle with vehicle-specific behavior while keeping the same interface
# Build TrafficSimulator with add_vehicle(vehicle), start_all(), and simulate_traffic()
# Ensure Bicycle.start() represents beginning to pedal rather than engine ignition
# Hint: class Vehicle: def accelerate(self, speed): ...
# Hint: class TrafficSimulator: def simulate_traffic(self): ...
# Write your code here:


# BONUS TODO: Create a plugin system that relies on polymorphism
# Build Plugin with load(), execute(), and unload(), then create multiple plugin implementations
# Build PluginManager to work with any plugin object through the shared interface
# Write your code here:

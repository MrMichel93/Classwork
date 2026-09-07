"""
Mini-Program 5: Object Composition and Aggregation
Topic: Basic OOP

Learning Objectives:
- Understand composition (has-a relationship)
- Create objects that contain other objects
- Build complex systems from simpler components
- Manage object relationships
- Initialize and work with nested objects

Instructions:
Complete this program exploring composition and aggregation patterns.
"""

# Student Self-Check
# Run: python3 -m unittest starter_tests.test_09_basic_oop.BasicOOPSelfChecks.test_composition_aggregation
# Expect: a full address includes its city; a 3-credit course adds 3 credits;
# starting a car starts its engine.

# TODO 1-3: Create an Address class and use it in Person
# Build Address with street, city, state, zip_code attributes
# Add 'get_full_address' method returning formatted address string
# Build Person with name, age, and address (Address object)
# Add 'get_info' method that includes full address in output
# Create instances and test composition (Person "has-a" Address)
# Write your code here:


# TODO 4-6: Create a Student/Course system using composition
# Build Course with course_code, name, credits
# Build Student with name, student_id, courses (list)
# Add methods: add_course(), drop_course(), get_total_credits(), list_courses()
# Create Course instances, add to Student, calculate credits, list courses
# Write your code here:


# TODO 7-9: Create an Engine/Car composition relationship
# Build Engine with horsepower, fuel_type, and methods: start(), stop(), get_info()
# Build Car with make, model, year, engine (Engine object)
# Add methods: start_car(), stop_car(), get_car_info() that use engine methods
# Create and test engine/car relationships
# Write your code here:


# TODO 10-12: Create a Book/Library system
# Build Book with title, author, isbn, available (boolean)
# Add methods: checkout(), return_book(), get_info()
# Build Library with name and books (list)
# Add methods: add_book(), find_book_by_title(), checkout_book(), return_book(), list_available_books()
# Create, add, checkout, and return books
# Write your code here:


# TODO 13-15: Create a banking system with Customer and Accounts
# Build BankAccount with account_number, balance, account_type
# Add methods: deposit(), withdraw(), get_balance()
# Build Customer with name, customer_id, accounts (list)
# Add methods: add_account(), get_total_balance(), transfer(), list_accounts()
# Create accounts, add to customer, perform transactions
# Write your code here:


# TODO 16-18: Create a House/Room composition system
# Build Room with name, length, width and get_area() method
# Build House with address (Address object), rooms (list)
# Add methods: add_room(), get_total_area(), count_rooms(), list_rooms()
# Create and manage house with multiple rooms
# Write your code here:


# BONUS TODO: Create a complete University system
# Classes: Department (name, code, courses), Professor (name, id, department),
#          Course (code, name, professor, students), Student (name, id, major, courses)
# Implement: enroll student, assign professor, list courses in department, find by major
# This demonstrates complex multi-level composition
# Write your code here:

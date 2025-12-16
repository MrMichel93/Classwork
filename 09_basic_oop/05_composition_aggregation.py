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

# TODO 1: Create an Address class
# Attributes: street, city, state, zip_code
# Method: get_full_address() that returns formatted address
# Write your code here:


# TODO 2: Create a Person class that uses Address
# Person has: name, age, address (Address object)
# Method: get_info() that returns person info including full address
# This is composition: Person "has-a" Address
# Write your code here:


# TODO 3: Create instances and test
# Create an Address object
# Create a Person object using that address
# Call get_info() and print
# Write your code here:


# TODO 4: Create a Course class
# Attributes: course_code, name, credits
# Method: get_course_info()
# Write your code here:


# TODO 5: Create a Student class with multiple courses
# Attributes: name, student_id, courses (list of Course objects)
# Methods:
# - add_course(course)
# - drop_course(course_code)
# - get_total_credits()
# - list_courses()
# Write your code here:


# TODO 6: Test the Student class
# Create several Course objects
# Create a Student
# Add courses to student
# Print total credits
# List all courses
# Write your code here:


# TODO 7: Create an Engine class
# Attributes: horsepower, fuel_type
# Method: start(), stop(), get_info()
# Write your code here:


# TODO 8: Create a Car class that contains Engine
# Attributes: make, model, year, engine (Engine object)
# Methods: start_car(), stop_car(), get_car_info()
# When car starts, engine starts
# Write your code here:


# TODO 9: Test the Car and Engine relationship
# Create Engine object
# Create Car with that engine
# Start and stop the car
# Print car info
# Write your code here:


# TODO 10: Create a Book class
# Attributes: title, author, isbn, available (boolean)
# Methods: checkout(), return_book(), get_info()
# Write your code here:


# TODO 11: Create a Library class
# Attributes: name, books (list of Book objects)
# Methods:
# - add_book(book)
# - find_book_by_title(title)
# - checkout_book(isbn)
# - return_book(isbn)
# - list_available_books()
# Write your code here:


# TODO 12: Test the Library system
# Create several books
# Create a library
# Add books to library
# Checkout a book
# List available books
# Return the book
# Write your code here:


# TODO 13: Create a BankAccount class
# Attributes: account_number, balance, account_type
# Methods: deposit(amount), withdraw(amount), get_balance()
# Write your code here:


# TODO 14: Create a Customer class
# Attributes: name, customer_id, accounts (list of BankAccount objects)
# Methods:
# - add_account(account)
# - get_total_balance()
# - transfer(from_account_num, to_account_num, amount)
# - list_accounts()
# Write your code here:


# TODO 15: Test the banking system
# Create multiple accounts
# Create a customer
# Add accounts to customer
# Perform deposits and withdrawals
# Transfer between accounts
# Print total balance
# Write your code here:


# TODO 16: Create a Room class
# Attributes: name, length, width
# Method: get_area()
# Write your code here:


# TODO 17: Create a House class
# Attributes: address (Address object), rooms (list of Room objects)
# Methods:
# - add_room(room)
# - get_total_area()
# - count_rooms()
# - list_rooms()
# Write your code here:


# TODO 18: Test the House system
# Create an address
# Create several rooms
# Create a house
# Add rooms to house
# Calculate total area
# Print house details
# Write your code here:


# BONUS TODO: Create a complete University system
# Classes needed:
# - Department (name, code, courses)
# - Professor (name, employee_id, department)
# - Course (code, name, professor, enrolled_students)
# - Student (name, id, major_department, enrolled_courses)
# Implement:
# - Enroll student in course
# - Assign professor to course
# - List all courses in department
# - Find students by major
# This demonstrates complex composition!
# Write your code here:


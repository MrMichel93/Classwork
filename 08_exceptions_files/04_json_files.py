"""
Mini-Program 4: Working with JSON Files
Topic: Exceptions & Files

Learning Objectives:
- Understand JSON format for data storage
- Use the json module to read and write JSON
- Convert between Python objects and JSON
- Handle JSON parsing errors

Instructions:
Complete this program to practice working with JSON files.
"""

# First, import the json module at the top
import json

# TODO 1: Create a dictionary with student information
# Include: name, age, grade, and subjects (as a list)
# Example: {"name": "Bob", "age": 16, "grade": "11th", "subjects": ["Math", "Science", "English"]}
# Write your code here:


# TODO 2: Write the dictionary to a JSON file called 'student.json'
# Hint: Use json.dump(data, file) with a file opened in write mode
# Write your code here:


# TODO 3: Read the JSON file back into a Python dictionary
# Hint: Use json.load(file) with a file opened in read mode
# Store in a variable called 'loaded_student' and print it
# Write your code here:


# TODO 4: Convert a Python list to a JSON string (not a file)
# Create a list: [1, 2, 3, 4, 5]
# Use json.dumps() to convert it to a JSON string
# Print the JSON string
# Write your code here:


# TODO 5: Convert a JSON string back to a Python object
# Take the JSON string: '{"city": "New York", "population": 8000000}'
# Use json.loads() to parse it
# Print the resulting dictionary
# Write your code here:


# TODO 6: Create a list of dictionaries representing multiple students
# Each dictionary should have: name, age, and grade
# Include at least 3 students
# Write your code here:


# TODO 7: Save the list of students to 'students.json'
# Use indent=4 for pretty formatting
# Hint: json.dump(data, file, indent=4)
# Write your code here:


# TODO 8: Read the 'students.json' file
# Loop through the students and print each student's name
# Write your code here:


# TODO 9: Write a try-except block to handle JSON parsing errors
# Try to parse an invalid JSON string: '{"name": "Alice", age: 25}'
# (Note: age is missing quotes, making it invalid JSON)
# Catch json.JSONDecodeError and print "Invalid JSON format"
# Write your code here:


# TODO 10: Create a nested dictionary structure and save it as JSON
# Example: A school with classes, each class having students
# Structure: {"school": "Central High", "classes": {"Math": ["Alice", "Bob"], "Science": ["Charlie", "Diana"]}}
# Write your code here:


# TODO 11: Read the nested JSON back and access a specific value
# Access and print the students in the Math class
# Write your code here:


# TODO 12: Create a function called 'save_to_json' that:
# - Takes a filename and data (dict or list) as parameters
# - Saves the data to a JSON file with pretty formatting
# - Uses try-except to handle IOError
# Write your code here:


# BONUS TODO: Create a function to update a specific value in a JSON file
# For example, change a student's grade in 'student.json'
# Read the file, modify the data, and write it back
# Write your code here:


"""
Mini-Program 1: Exception Handling
Topic: Exceptions & Files

Learning Objectives:
- Understand what exceptions are and why they occur
- Use try-except blocks to handle errors
- Handle specific exception types
- Use finally clause for cleanup code

Instructions:
Complete this program to practice handling exceptions gracefully.
"""

# TODO 1: Write a try-except block to handle division by zero
# Try to divide 10 by 0 and catch the ZeroDivisionError
# Print "Cannot divide by zero!" in the except block
# Write your code here:


# TODO 2: Write a try-except block to handle invalid integer conversion
# Try to convert the string "abc" to an integer
# Catch the ValueError and print "Invalid number format!"
# Write your code here:


# TODO 3: Write a try-except block that catches multiple exception types
# Try to access index 10 of a list [1, 2, 3]
# Catch IndexError and print "Index out of range!"
# Write your code here:


# TODO 4: Write a try-except-else block
# Try to divide 20 by 4
# In the except block, handle ZeroDivisionError
# In the else block (runs if no exception), print the result
# Write your code here:


# TODO 5: Write a try-except-finally block
# Try to convert "123" to an integer
# Catch any ValueError
# In the finally block, print "Conversion attempt complete"
# (finally always runs, whether there's an exception or not)
# Write your code here:


# TODO 6: Create a function called 'safe_divide' that takes two parameters
# Use try-except to safely divide the first by the second
# Return the result if successful, or return None if ZeroDivisionError occurs
# Write your code here:


# TODO 7: Test your safe_divide function with:
# - safe_divide(10, 2) - should return 5.0
# - safe_divide(10, 0) - should return None
# Print both results
# Write your code here:


# TODO 8: Write a try-except block with a general exception handler
# Try to perform: int("hello") + [1, 2, 3]
# Use except Exception as e to catch any exception
# Print the exception type and message
# Hint: Use type(e).__name__ and str(e)
# Write your code here:


# TODO 9: Create a function that raises an exception
# Define 'check_positive' that takes a number
# If the number is negative, raise ValueError with message "Number must be positive"
# Otherwise, print "Number is valid"
# Hint: Use raise ValueError("message")
# Write your code here:


# TODO 10: Test check_positive with try-except
# Try calling check_positive(-5)
# Catch the ValueError and print its message
# Write your code here:


# BONUS TODO: Create a custom exception class called 'InvalidAgeError'
# Use it to validate that an age is between 0 and 120
# Write a function that raises this exception for invalid ages
# Write your code here:


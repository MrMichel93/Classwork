"""
Mini-Program 5: Recursive Functions and Advanced Techniques
Topic: Functions

Learning Objectives:
- Understand recursion and recursive function calls
- Create functions with default parameters
- Use functions as arguments to other functions
- Build complex logic with helper functions
- Master return value manipulation

Instructions:
Complete this program exploring advanced function concepts including
recursion and function composition.
"""

# TODO 1: Define a recursive function called 'factorial'
# It should take one parameter: n
# Factorial of n (n!) = n * (n-1) * (n-2) * ... * 1
# Base case: if n <= 1, return 1
# Recursive case: return n * factorial(n-1)
# Example: factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
# Write your code here:


# TODO 2: Test the factorial function with n = 5 and print the result
# Write your code here:


# TODO 3: Define a recursive function called 'fibonacci'
# It should take one parameter: n
# Returns the nth Fibonacci number
# Base cases: if n <= 1, return n
# Recursive case: return fibonacci(n-1) + fibonacci(n-2)
# Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21...
# Write your code here:


# TODO 4: Print the first 10 Fibonacci numbers using a loop
# Use range(10) and call fibonacci(i) for each i
# Write your code here:


# TODO 5: Define a recursive function called 'countdown'
# It should take one parameter: n
# Print numbers from n down to 1, then print "Blastoff!"
# Base case: if n <= 0, print "Blastoff!" and return
# Recursive case: print n, then call countdown(n-1)
# Write your code here:


# TODO 6: Test countdown with n = 5
# Write your code here:


# TODO 7: Define a function called 'power' with default parameter
# Parameters: base, exponent=2
# Returns base raised to the power of exponent
# The exponent should default to 2 if not provided
# Use a loop or the ** operator
# Write your code here:


# TODO 8: Test power function
# Call it with power(3, 4) and power(5) (should use default exponent of 2)
# Print both results
# Write your code here:


# TODO 9: Define a function called 'apply_operation'
# Parameters: a, b, operation
# This function takes two numbers and a function
# It returns the result of calling operation(a, b)
# This demonstrates passing functions as arguments!
# Write your code here:


# TODO 10: Define simple operation functions to use with apply_operation
# Create: add(a, b), subtract(a, b), multiply(a, b), divide(a, b)
# Each should return the result of the operation
# Write your code here:


# TODO 11: Test apply_operation with different operations
# Call apply_operation(10, 5, add)
# Call apply_operation(10, 5, multiply)
# Print both results
# Write your code here:


# TODO 12: Define a function called 'is_palindrome'
# Parameter: text (a string)
# Returns True if the text reads the same forwards and backwards
# Hint: Compare text with text[::-1] (reversed)
# Example: "radar" is a palindrome
# Write your code here:


# TODO 13: Test is_palindrome with various strings
# Test with: "radar", "hello", "level", "python"
# Print the results
# Write your code here:


# TODO 14: Define a recursive function called 'sum_digits'
# Parameter: n (a positive integer)
# Returns the sum of all digits in n
# Example: sum_digits(123) = 1 + 2 + 3 = 6
# Base case: if n < 10, return n
# Recursive case: return (n % 10) + sum_digits(n // 10)
# Write your code here:


# TODO 15: Test sum_digits with 12345
# Write your code here:


# TODO 16: Define a function called 'filter_positive'
# Parameter: numbers (a list of numbers)
# Returns a new list containing only positive numbers
# Use a loop to build the new list
# Write your code here:


# TODO 17: Test filter_positive with a list containing positive and negative numbers
# Example: [-5, 10, -3, 7, 0, 15, -8]
# Write your code here:


# TODO 18: Define a function called 'calculate_compound_interest'
# Parameters: principal, rate, years, compounds_per_year=12
# Calculate and return compound interest
# Formula: A = P(1 + r/n)^(nt)
# Use default value of 12 for compounds_per_year (monthly)
# Write your code here:


# TODO 19: Test calculate_compound_interest with different scenarios
# Scenario 1: principal=1000, rate=0.05, years=10 (use default compounding)
# Scenario 2: principal=1000, rate=0.05, years=10, compounds_per_year=1 (annual)
# Print both results to compare
# Write your code here:


# BONUS TODO: Define a recursive function called 'reverse_string'
# Parameter: text
# Returns the reversed string using recursion
# Base case: if len(text) <= 1, return text
# Recursive case: return reverse_string(text[1:]) + text[0]
# Test with "hello" - should return "olleh"
# Write your code here:


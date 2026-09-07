"""
Mini-Program 2: Temperature Conversion Functions
Topic: Functions

Learning Objectives:
- Create functions that perform calculations
- Use parameters and return values effectively
- Call functions multiple times with different arguments
- Organize related code into reusable functions

Instructions:
Complete this program by creating temperature conversion functions.
"""

# Student Self-Check
# Run: python -m unittest starter_tests.test_03_functions
# - Confirm celsius_to_fahrenheit converts 0 to 32 and 100 to 212.
# - Confirm fahrenheit_to_celsius converts 98.6 to approximately 37.
# - Confirm fahrenheit_to_kelvin(32) returns 273.15 by reusing the earlier functions.

# TODO 1-4: Create temperature conversion functions
# Build four conversion functions:
# - celsius_to_fahrenheit(celsius): formula is (celsius * 9/5) + 32
# - fahrenheit_to_celsius(fahrenheit): formula is (fahrenheit - 32) * 5/9
# - celsius_to_kelvin(celsius): formula is celsius + 273.15
# - kelvin_to_celsius(kelvin): formula is kelvin - 273.15
# Hint: Each function takes one parameter and returns the converted value
# Write your code here:


# TODO 5-8: Test your conversion functions
# Call each function with test values and print the results
# Test: 0°C to F (should be 32), 100°C to F (should be 212), 98.6°F to C (should be ~37)
# Test: 25°C to K
# Write your code here:


# TODO 9-10: Create a combined conversion function
# Build 'fahrenheit_to_kelvin' by composing your existing functions
# Hint: Convert F → C (using fahrenheit_to_celsius), then C → K (using celsius_to_kelvin)
# Test with 32°F (should return 273.15)
# Write your code here:


# BONUS TODO: Create a utility function that displays all three scales
# Build 'print_all_temps(celsius)' that prints C, F, and K values
# Use your existing conversion functions
# Write your code here:

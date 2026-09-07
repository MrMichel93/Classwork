"""
Mini-Program 4: Password Validator
Topic: Conditionals

Learning Objectives:
- Work with string comparisons
- Use the 'in' operator to check string contents
- Apply multiple conditions with logical operators
- Validate data based on rules

Instructions:
Complete this program that validates a password based on certain rules.
"""

# Student Self-Check
# Run: python -m unittest starter_tests.test_02_conditionals
# - Confirm "Secret123" reports good length, a number, matching confirmation, and valid status.
# - Try a password shorter than eight characters to confirm it is rejected.
# - Try "user123" and a value containing "password" to confirm both invalid cases.

# TODO 1-6: Build the core password checks
# Create the password and username values, then test the length, number requirement,
# username rule, and forbidden-word rule.
# Hint: len(password), password.lower(), and membership checks such as '1' in password
# Write your code here:


# TODO 7-9: Confirm and summarize the password status
# Add a confirmation value, compare it with the password, and print whether the password passes the main rules.
# Hint: password == confirm_password and a combined condition using and
# Write your code here:


# BONUS TODO: Add an uppercase-letter check
# Report whether the password includes at least one uppercase character.
# Hint: compare password with password.lower()
# Write your code here:

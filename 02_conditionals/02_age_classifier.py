"""
Mini-Program 2: Age Classifier
Topic: Conditionals

Learning Objectives:
- Practice using if-elif-else statements
- Work with multiple conditions
- Use logical operators (and, or)
- Create age-based classifications

Instructions:
Complete this program that classifies people into age groups and determines
what activities they can do.
"""

# Student Self-Check
# Run: python -m unittest starter_tests.test_02_conditionals
# - Test ages 12, 13, 20, and 65 to confirm every age-group boundary.
# - Test 16, 18, and 21 to confirm each activity message appears at the right age.
# - Test -1 to confirm invalid ages do not receive a normal age-group message.

# TODO 1: Set up your age variable
# Assign a test age value
# Write your code here:


# TODO 2-6: Create a conditional structure for age classifications
# Classify ages into groups: invalid (<0), child (0-12), teenager (13-19), adult (20-64), senior (65+)
# Hint: Use if/elif/else; use 'and' operator for range checks (age >= 0 and age <= 12)
# Write your code here:


# TODO 7-9: Add activity eligibility checks
# Create separate if statements to check:
# - Age 16+: Can get driver's license
# - Age 18+: Can vote
# - Age 21+: All adult activities
# These print messages in addition to the age group classification
# Write your code here:


# BONUS TODO: Add ID verification logic
# Create a 'has_id' variable and check if age >= 18 AND has_id is True
# Print appropriate club entry message
# Write your code here:

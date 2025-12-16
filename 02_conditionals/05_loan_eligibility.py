"""
Mini-Program 5: Loan Eligibility Checker
Topic: Conditionals

Learning Objectives:
- Use multiple conditions with logical operators (and, or, not)
- Create complex decision trees
- Implement nested if statements
- Apply real-world business logic
- Work with multiple variables in conditions

Instructions:
Complete this loan eligibility checker that determines if someone
qualifies for a loan based on multiple criteria.
"""

# TODO 1: Create variables for the applicant's information
# age = 30
# annual_income = 55000
# credit_score = 720
# has_job = True
# Write your code here:


# TODO 2: Create a variable for existing debt
# monthly_debt = 800
# Write your code here:


# TODO 3: Calculate monthly income (annual_income / 12)
# Store in 'monthly_income'
# Write your code here:


# TODO 4: Calculate debt-to-income ratio
# Formula: debt_to_income_ratio = monthly_debt / monthly_income
# Write your code here:


# TODO 5: Start the eligibility check
# First, check if the applicant is at least 18 years old
# If not, print "Must be at least 18 years old" and set eligible = False
# Otherwise, set eligible = True
# Write your code here:


# TODO 6: Check if the applicant has a job
# If eligible is True and has_job is False
# Print "Employment required" and set eligible = False
# Write your code here:


# TODO 7: Check the minimum income requirement ($25,000 annually)
# If eligible is True and annual_income < 25000
# Print "Minimum income requirement not met" and set eligible = False
# Write your code here:


# TODO 8: Check the credit score requirement (minimum 650)
# If eligible is True and credit_score < 650
# Print "Credit score too low (minimum 650)" and set eligible = False
# Write your code here:


# TODO 9: Check the debt-to-income ratio (must be less than 0.43)
# If eligible is True and debt_to_income_ratio >= 0.43
# Print "Debt-to-income ratio too high" and set eligible = False
# Write your code here:


# TODO 10: Determine loan amount based on income and credit score
# Create variable 'max_loan_amount'
# If credit_score >= 750 and annual_income >= 50000:
#     max_loan_amount = annual_income * 5
# elif credit_score >= 700 and annual_income >= 40000:
#     max_loan_amount = annual_income * 4
# elif credit_score >= 650 and annual_income >= 30000:
#     max_loan_amount = annual_income * 3
# else:
#     max_loan_amount = 0
# Write your code here:


# TODO 11: Determine interest rate based on credit score
# If credit_score >= 750: interest_rate = 3.5
# elif credit_score >= 700: interest_rate = 4.5
# elif credit_score >= 650: interest_rate = 6.0
# else: interest_rate = 0
# Write your code here:


# TODO 12: Print final decision
# If eligible is True and max_loan_amount > 0:
#     Print "Loan APPROVED"
#     Print the max_loan_amount
#     Print the interest_rate
# else:
#     Print "Loan DENIED"
# Write your code here:


# TODO 13: Add a special promotion check
# If annual_income > 75000 AND credit_score > 780:
#     Print "You qualify for our premium rate!"
#     Reduce interest_rate by 0.5
# Write your code here:


# TODO 14: Check for first-time buyer benefits
# Create variable 'first_time_buyer' = True
# If first_time_buyer is True and eligible is True:
#     Increase max_loan_amount by 10%
#     Print "First-time buyer bonus applied!"
# Write your code here:


# BONUS TODO: Create a comprehensive loan comparison
# Test the program with 3 different applicant profiles:
# 1. High income, excellent credit (should get best terms)
# 2. Moderate income, good credit (should get standard terms)
# 3. Low income or poor credit (should be denied)
# Write your code here for all three scenarios:


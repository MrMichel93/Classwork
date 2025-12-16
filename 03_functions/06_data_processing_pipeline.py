"""
Mini-Program 6: Data Processing Pipeline with Functions
Topic: Functions

Learning Objectives:
- Design a multi-function data processing system
- Chain function calls for complex operations
- Use functions to organize large programs
- Implement validation and error checking
- Create reusable utility functions

Instructions:
Complete this advanced data processing pipeline that analyzes student grades.
This is the most challenging functions program!
"""

# TODO 1: Define a function called 'validate_score'
# Parameter: score
# Returns True if score is between 0 and 100 (inclusive), False otherwise
# Write your code here:


# TODO 2: Define a function called 'calculate_letter_grade'
# Parameter: score
# Returns letter grade: 'A' (90+), 'B' (80+), 'C' (70+), 'D' (60+), 'F' (below 60)
# Should first validate the score using validate_score
# If invalid, return 'Invalid'
# Write your code here:


# TODO 3: Define a function called 'calculate_gpa_points'
# Parameter: letter_grade
# Returns GPA points: A=4.0, B=3.0, C=2.0, D=1.0, F=0.0
# Write your code here:


# TODO 4: Define a function called 'calculate_average'
# Parameter: scores (a list of numbers)
# Returns the average of all scores
# Should handle empty list (return 0)
# Write your code here:


# TODO 5: Define a function called 'find_highest_score'
# Parameter: scores (a list of numbers)
# Returns the highest score
# Should handle empty list (return 0)
# Write your code here:


# TODO 6: Define a function called 'find_lowest_score'
# Parameter: scores (a list of numbers)
# Returns the lowest score
# Should handle empty list (return 0)
# Write your code here:


# TODO 7: Define a function called 'count_passing_scores'
# Parameter: scores (a list of numbers)
# Returns count of scores that are 60 or higher
# Write your code here:


# TODO 8: Define a function called 'count_failing_scores'
# Parameter: scores (a list of numbers)
# Returns count of scores that are below 60
# Write your code here:


# TODO 9: Define a function called 'calculate_grade_distribution'
# Parameter: scores (a list of numbers)
# Returns a dictionary with counts: {'A': count, 'B': count, 'C': count, 'D': count, 'F': count}
# Use calculate_letter_grade to determine the grade for each score
# Write your code here:


# TODO 10: Define a function called 'apply_curve'
# Parameters: scores (list), curve_points (default=5)
# Returns a new list with curve_points added to each score
# Make sure no score goes above 100
# Write your code here:


# TODO 11: Define a function called 'drop_lowest_score'
# Parameter: scores (a list of numbers)
# Returns a new list with the lowest score removed
# Should handle lists with only one element
# Write your code here:


# TODO 12: Define a function called 'calculate_weighted_average'
# Parameters: scores (list), weights (list)
# Returns weighted average
# Example: scores=[90, 80, 70], weights=[0.5, 0.3, 0.2]
# Result: 90*0.5 + 80*0.3 + 70*0.2 = 83
# Assume scores and weights are same length
# Write your code here:


# TODO 13: Define a function called 'standardize_score'
# Parameters: score, mean, std_deviation
# Returns the z-score: (score - mean) / std_deviation
# This converts scores to standard deviations from the mean
# Write your code here:


# TODO 14: Define a function called 'calculate_std_deviation'
# Parameter: scores (list)
# Returns the standard deviation
# Formula: sqrt(sum((score - mean)^2) / n)
# You'll need to calculate mean first
# Use ** 0.5 for square root
# Write your code here:


# TODO 15: Define a function called 'generate_report'
# Parameter: student_name, scores (list)
# This function orchestrates all the above functions
# It should:
# 1. Calculate and print average
# 2. Calculate and print letter grade for average
# 3. Find and print highest and lowest scores
# 4. Print passing/failing counts
# 5. Print grade distribution
# 6. Print a formatted report header with student name
# Write your code here:


# TODO 16: Create test data and run the pipeline
# Create a list of scores: [85, 92, 78, 90, 88, 76, 95, 82]
# Call generate_report with student name "Alice" and the scores
# Write your code here:


# TODO 17: Test the curve functionality
# Apply a 5-point curve to the scores
# Generate a new report with curved scores for student "Alice (Curved)"
# Write your code here:


# TODO 18: Test the drop lowest score functionality
# Drop the lowest score from original scores
# Generate a report with remaining scores for "Alice (Best Scores)"
# Write your code here:


# TODO 19: Test weighted average calculation
# Create test scores: [88, 92, 85]
# Create weights: [0.3, 0.4, 0.3] (30%, 40%, 30%)
# Calculate and print the weighted average
# Write your code here:


# TODO 20: Create a comprehensive analysis function
# Define 'comprehensive_analysis' that takes a dictionary of students
# Format: {'Alice': [85, 90, 92], 'Bob': [78, 82, 88], 'Charlie': [92, 95, 98]}
# For each student:
# 1. Generate individual report
# 2. Calculate class rank based on average
# Print class statistics: class average, highest student average, lowest student average
# Write your code here:


# TODO 21: Test comprehensive analysis
# Create the dictionary from TODO 20 and call comprehensive_analysis
# Write your code here:


# BONUS TODO: Create an advanced grading system
# Define 'calculate_final_grade' that takes:
# - homework_scores (list)
# - quiz_scores (list)
# - exam_scores (list)
# - weights for each category (homework=30%, quizzes=30%, exams=40%)
# Calculate category averages
# Calculate weighted final grade
# Determine letter grade
# Return a dictionary with all information
# Test with sample data
# Write your code here:


"""
Mini-Program 6: Advanced Loop Challenges
Topic: Loops and Iteration

Learning Objectives:
- Combine multiple loop techniques in complex problems
- Implement real-world algorithms using loops
- Use loops with complex data structures
- Master loop control flow (break, continue)
- Solve multi-step algorithmic challenges

Instructions:
Complete these advanced loop challenges that combine everything you've learned.
This is the most challenging loops program!
"""

# TODO 1: Implement a Collatz Conjecture sequence generator
# Start with a number (try 27)
# If even: divide by 2
# If odd: multiply by 3 and add 1
# Continue until you reach 1
# Count how many steps it takes and print the sequence
# Write your code here:


# TODO 2: Find the longest consecutive sequence of numbers in a list
# numbers = [1, 2, 3, 7, 8, 9, 10, 11, 5, 6]
# Should find: [7, 8, 9, 10, 11] (length 5)
# Print the longest sequence and its length
# Hint: Sort the list first, then use a loop to find consecutive runs
# Write your code here:


# TODO 3: Generate the Fibonacci sequence up to a maximum value
# Keep generating Fibonacci numbers while they're less than 1000
# Store them in a list and print the list
# Print how many Fibonacci numbers are less than 1000
# Write your code here:


# TODO 4: Implement a simple spell checker
# dictionary = ['hello', 'world', 'python', 'programming', 'loop']
# text = ['helo', 'world', 'pythn', 'programing', 'loop']
# For each word in text, check if it's in dictionary
# If not, try to find close matches (words that differ by 1 character)
# Print corrections or "word is correct"
# Write your code here:


# TODO 5: Calculate statistics for a dataset using loops
# data = [23, 45, 67, 89, 12, 34, 56, 78, 90, 11, 22, 33, 44, 55]
# Calculate WITHOUT using built-in functions:
# - Mean (average)
# - Median (middle value when sorted)
# - Mode (most frequent value)
# - Range (max - min)
# - Standard deviation
# Print all statistics
# Write your code here:


# TODO 6: Implement a simple text analyzer
# text = "Python is awesome. Python is powerful. Python is fun."
# Using loops, calculate:
# - Total character count
# - Word count
# - Sentence count (count periods)
# - Frequency of each word (create a dictionary)
# Print all statistics
# Write your code here:


# TODO 7: Generate all prime factors of a number
# number = 315
# Find all prime factors (numbers that divide evenly and are prime)
# For 315: prime factors are 3, 3, 5, 7 (315 = 3 × 3 × 5 × 7)
# Print the prime factors and verify their product equals the original number
# Write your code here:


# TODO 8: Implement a simple encryption/decryption (Caesar Cipher)
# message = "HELLO"
# shift = 3
# Encrypt by shifting each letter by 'shift' positions
# H -> K, E -> H, L -> O, L -> O, O -> R
# Result: "KHOOR"
# Then decrypt it back to original
# Use loops and ASCII values (ord() and chr() functions)
# Write your code here:


# TODO 9: Find the longest word in a sentence
# sentence = "The quick brown fox jumps over the lazy dog"
# Split into words and find the longest one
# If there are multiple words with same max length, find all of them
# Write your code here:


# TODO 10: Implement run-length encoding
# text = "AAABBBCCCCCDDEEE"
# Encode as: "A3B3C5D2E3" (character followed by count)
# Use loops to count consecutive characters
# Print the encoded result
# Write your code here:


# TODO 11: Decode run-length encoded text
# encoded = "A3B3C5D2E3"
# Decode back to: "AAABBBCCCCCDDEEE"
# Parse the encoded string and reconstruct the original
# Write your code here:


# TODO 12: Generate all permutations of a small list using nested loops
# items = ['A', 'B', 'C']
# Generate all possible orderings (permutations)
# ABC, ACB, BAC, BCA, CAB, CBA
# Use three nested loops for 3 items
# Write your code here:


# TODO 13: Implement a sliding window algorithm
# numbers = [1, 3, 2, 6, -1, 4, 1, 8, 2]
# window_size = 3
# Calculate the sum of each window of 3 consecutive numbers
# Print each window and its sum
# Find the window with the maximum sum
# Write your code here:


# TODO 14: Find all Pythagorean triples up to a maximum value
# A Pythagorean triple: a² + b² = c²
# Example: 3, 4, 5 (because 9 + 16 = 25)
# Find all triples where a, b, c are all less than 50
# Use three nested loops
# Make sure a < b < c to avoid duplicates
# Write your code here:


# TODO 15: Implement a simple pattern matching
# text = "The rain in Spain stays mainly in the plain"
# pattern = "ain"
# Find all occurrences of pattern in text
# Print the position of each occurrence
# Don't use built-in find() - implement with loops
# Write your code here:


# TODO 16: Generate a spiral matrix
# Create a 5x5 matrix filled in spiral order:
# 1  2  3  4  5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9
# Use loops to fill the matrix in spiral pattern
# This is challenging!
# Write your code here:


# TODO 17: Implement an inventory management system using loops
# inventory = {'apples': 50, 'bananas': 30, 'oranges': 25, 'grapes': 40}
# transactions = [('apples', -10), ('bananas', 20), ('oranges', -15), ('apples', -5)]
# Process each transaction (positive = restock, negative = sale)
# Print inventory after each transaction
# Alert if any item goes below 15 units
# Calculate total value if apples=$2, bananas=$1.5, oranges=$3, grapes=$4
# Write your code here:


# TODO 18: Find the longest palindromic substring
# text = "babad"
# Find the longest substring that is a palindrome
# For "babad", answer could be "bab" or "aba"
# Use nested loops to check all substrings
# Write your code here:


# BONUS TODO: Implement a simple maze solver
# maze = [
#     [1, 1, 1, 1, 1],
#     [1, 0, 0, 0, 1],
#     [1, 0, 1, 0, 1],
#     [1, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1]
# ]
# 1 = wall, 0 = path
# Start at (1, 1), end at (3, 3)
# Find a path using loops
# Print the path coordinates
# This is very challenging!
# Write your code here:


"""
Mini-Program 5: Advanced Data Structure Operations
Topic: Tuples, Sets and Dictionaries

Learning Objectives:
- Combine tuples, sets, and dictionaries in complex operations
- Use data structures for efficient problem solving
- Implement set theory operations
- Work with nested and complex data structures
- Apply the right data structure for each problem

Instructions:
Complete this program exploring advanced operations with Python's
core data structures.
"""

# TODO 1: Create a dictionary from two lists (parallel lists)
# keys = ['name', 'age', 'city', 'occupation']
# values = ['Alice', 30, 'New York', 'Engineer']
# Create dictionary by pairing elements
# Use zip() and dict()
# Write your code here:


# TODO 2: Merge multiple dictionaries
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}
# dict3 = {'c': 5, 'd': 6}
# Merge all dictionaries (later values override earlier ones)
# Result: {'a': 1, 'b': 3, 'c': 5, 'd': 6}
# Write your code here:


# TODO 3: Find symmetric difference of multiple sets
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# set3 = {5, 6, 7, 8}
# Find elements that appear in exactly one set
# Use set operations
# Write your code here:


# TODO 4: Create inverted dictionary (swap keys and values)
# original = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
# Inverted: {1: ['a', 'c'], 2: ['b'], 3: ['d']}
# Values become keys, keys with same value grouped in list
# Write your code here:


# TODO 5: Count character frequency using dictionary
# text = "hello world"
# Create dictionary: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ...}
# Print sorted by frequency (most common first)
# Write your code here:


# TODO 6: Find common elements across multiple lists using sets
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# list3 = [5, 6, 7, 8, 9]
# Find elements present in all three lists
# Convert to sets and use intersection
# Write your code here:


# TODO 7: Group dictionary items by value ranges
# grades = {'Alice': 92, 'Bob': 78, 'Charlie': 95, 'David': 65, 'Eve': 88}
# Group by grade ranges:
# 'A' (90+): ['Alice', 'Charlie']
# 'B' (80-89): ['Eve']
# 'C' (70-79): ['Bob']
# 'D' (60-69): ['David']
# Create nested dictionary structure
# Write your code here:


# TODO 8: Implement a two-way dictionary (bidirectional mapping)
# Create a class or structure that allows:
# country_capital['USA'] = 'Washington'
# capital_country['Washington'] = 'USA'
# Use two dictionaries
# Write your code here:


# TODO 9: Find all subsets of a set (power set)
# original_set = {1, 2, 3}
# Power set: [{}, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}]
# Generate all possible subsets
# Use nested loops or bit manipulation concept
# Write your code here:


# TODO 10: Create a nested dictionary from paths
# paths = [
#     ('root', 'home', 'user', 'file.txt'),
#     ('root', 'home', 'user', 'data.csv'),
#     ('root', 'var', 'log', 'system.log')
# ]
# Create nested dictionary representing directory structure
# Result: {'root': {'home': {'user': {'file.txt': {}, 'data.csv': {}}}, 'var': {'log': {'system.log': {}}}}}
# Write your code here:


# TODO 11: Implement set-based duplicate finder
# lists = [
#     [1, 2, 3, 4],
#     [3, 4, 5, 6],
#     [5, 6, 7, 8],
#     [1, 2, 7, 8]
# ]
# Find elements that appear in multiple lists
# Count how many lists each element appears in
# Write your code here:


# TODO 12: Create a dictionary-based cache with expiration
# Implement a simple cache using a dictionary
# Store: key -> (value, timestamp)
# Items expire after certain time
# Check expiration when accessing
# Use tuple for values
# Write your code here:


# TODO 13: Implement dictionary sorting by multiple criteria
# students = {
#     'Alice': {'grade': 85, 'age': 20},
#     'Bob': {'grade': 90, 'age': 19},
#     'Charlie': {'grade': 85, 'age': 21}
# }
# Sort by grade (descending), then by age (ascending)
# Print sorted list
# Write your code here:


# TODO 14: Find longest common prefix using dictionary trie concept
# words = ["flower", "flow", "flight"]
# Use dictionary to represent trie structure
# Find longest common prefix: "fl"
# Build simple trie and traverse
# Write your code here:


# TODO 15: Implement set partitioning
# numbers = {1, 2, 3, 4, 5, 6}
# Partition into two subsets with equal sum (if possible)
# Use set operations and backtracking
# Check if subset sum equals half of total sum
# Write your code here:


# TODO 16: Create a multi-level dictionary flattener
# nested = {
#     'a': 1,
#     'b': {
#         'c': 2,
#         'd': {
#             'e': 3,
#             'f': 4
#         }
#     },
#     'g': 5
# }
# Flatten to: {'a': 1, 'b.c': 2, 'b.d.e': 3, 'b.d.f': 4, 'g': 5}
# Use recursion or iterative approach
# Write your code here:


# TODO 17: Implement graph representation using dictionary
# edges = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]
# Create adjacency list: {1: [2, 3], 2: [4], 3: [4], 4: [5], 5: []}
# Use dictionary where key is node, value is list of neighbors
# Write your code here:


# BONUS TODO: Implement a simple database using nested dictionaries
# Create a student database with operations:
# - Add student (with multiple attributes)
# - Query by attribute (find all students with age > 20)
# - Update student information
# - Delete student
# - List all students
# Use nested dictionaries and sets for indexing
# Write your code here:


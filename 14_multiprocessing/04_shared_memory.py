"""
Mini-Program 4: Shared Memory and Values
Topic: Multiprocessing

Learning Objectives:
- Use Value and Array for shared memory
- Use Manager for shared objects
- Synchronize access to shared memory
- Understand when to use shared memory vs queues

Instructions:
Complete this program to learn about shared memory in multiprocessing.
"""

import multiprocessing
import time

# TODO 1: Create a shared Value
# Use multiprocessing.Value('i', 0) for an integer
# 'i' is the type code (i=integer, d=double, etc.)
# Write your code here:


# TODO 2: Create a function that increments a shared value
# Takes the shared value as parameter
# Increments it multiple times
# Write your code here:


# TODO 3: Create multiple processes that increment the shared value
# Without locking, there will be a race condition
# The final value will be incorrect
# Write your code here:


# TODO 4: Fix the race condition using the value's lock
# Use value.get_lock() or with value.get_lock():
# Write your code here:


# TODO 5: Create a shared Array
# Use multiprocessing.Array('i', [1, 2, 3, 4, 5])
# Multiple processes can read and write to it
# Write your code here:


# TODO 6: Create a function that modifies the shared array
# Takes the array as parameter
# Modifies elements (with proper locking)
# Write your code here:


# TODO 7: Use Manager for more complex shared objects
# Manager provides shared lists, dicts, etc.
# Hint: manager = multiprocessing.Manager()
#       shared_list = manager.list()
# Write your code here:


# TODO 8: Create processes that append to a shared list
# Use Manager.list()
# Create multiple processes adding items
# Print the final list
# Write your code here:


# TODO 9: Use Manager for a shared dictionary
# Multiple processes update different keys
# Create a manager.dict()
# Write your code here:


# TODO 10: Create a shared counter using Value and Lock
# Implement a thread-safe counter class
# Use Value for the count and Lock for synchronization
# Write your code here:


# TODO 11: Compare performance: Queue vs Shared Memory
# For simple data sharing, shared memory can be faster
# For complex objects, Queue is easier
# Time both approaches
# Write your code here:


# TODO 12: Use Manager.Namespace for shared attributes
# Namespace allows setting arbitrary attributes
# Example: ns = manager.Namespace()
#          ns.x = 10
#          ns.y = 20
# Write your code here:


# TODO 13: Create a shared state object
# Use Manager to create a shared dict or namespace
# Multiple processes read and update the state
# Implement proper locking
# Write your code here:


# BONUS TODO: Implement a parallel merge sort
# Use shared arrays to store data
# Split work among processes
# Processes work on different sections simultaneously
# Write your code here:


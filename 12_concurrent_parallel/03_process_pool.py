"""
Mini-Program 3: Process Pool Executor
Topic: Concurrent and Parallel Programming

Learning Objectives:
- Understand ProcessPoolExecutor for CPU-bound tasks
- Differentiate between processes and threads
- Use multiprocessing for parallel computation
- Work with process pool executors

Instructions:
Complete this program to learn about process-based parallelism.
"""

import time
from concurrent.futures import ProcessPoolExecutor
import os

# TODO 1: Create a CPU-intensive function 'calculate_prime_count'
# Takes a number n
# Counts how many numbers from 2 to n are prime
# Return the count
# Hint: A simple prime check: for each number, check if divisible by any number from 2 to sqrt(number)
# Write your code here:


# TODO 2: Test calculate_prime_count sequentially
# Calculate prime count for [10000, 20000, 30000]
# Measure and print the time taken
# Write your code here:


# TODO 3: Use ProcessPoolExecutor to run the same calculations in parallel
# Create a ProcessPoolExecutor
# Use executor.map() to apply the function to the list
# Measure and print the time taken (should be faster!)
# Write your code here:


# TODO 4: Create a function 'get_process_info' that:
# - Takes a task_id
# - Returns the process ID using os.getpid()
# - Returns a message with task_id and process ID
# Write your code here:


# TODO 5: Submit multiple tasks to ProcessPoolExecutor
# Print the process IDs to see different processes being used
# Compare with the main process ID (os.getpid())
# Write your code here:


# TODO 6: Create a function 'factorial' that calculates factorial recursively
# Takes a number n
# Returns n! (factorial of n)
# Write your code here:


# TODO 7: Calculate factorials of [10, 15, 20, 25] using ProcessPoolExecutor
# Print the results
# Write your code here:


# TODO 8: Create a function 'sum_of_squares' that:
# - Takes a range (start, end)
# - Returns the sum of squares of all numbers in that range
# Write your code here:


# TODO 9: Split a large range into chunks
# Process each chunk with ProcessPoolExecutor
# Sum all the results to get the total
# Example: Split 1-10000 into 4 chunks: (1-2500), (2501-5000), etc.
# Write your code here:


# TODO 10: Create a function that simulates intensive computation
# 'process_data' that takes a data_list
# Performs some CPU-intensive operation on it
# Example: Sort the list multiple times, or perform complex calculations
# Write your code here:


# TODO 11: Compare ThreadPoolExecutor vs ProcessPoolExecutor
# For CPU-bound tasks, processes should be faster
# For I/O-bound tasks, threads are usually sufficient
# Test with a CPU-bound task
# Write your code here:


# TODO 12: Use ProcessPoolExecutor with a context manager
# Set max_workers to the number of CPU cores available
# Hint: import multiprocessing; multiprocessing.cpu_count()
# Write your code here:


# BONUS TODO: Create a map-reduce style computation
# Map: Apply a function to chunks of data in parallel
# Reduce: Combine all results into a final result
# Example: Calculate sum of squares of 1 to 100000
# Write your code here:


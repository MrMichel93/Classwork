"""
Mini-Program 1: Concurrent Programming Basics
Topic: Concurrent and Parallel Programming

Learning Objectives:
- Understand the difference between concurrent and parallel execution
- Learn about the concurrent.futures module
- Use ThreadPoolExecutor for concurrent tasks
- Work with futures and their results

Instructions:
Complete this program to learn concurrent programming basics.
"""

import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# TODO 1-2: Create and test a task function sequentially
# Build 'task' function that takes task_id, sleeps 1s, returns completion message
# Call it 3 times in a loop, timing the execution (should take ~3 seconds)
# Use time.time() to measure start/end
# Write your code here:


# TODO 3-5: Use ThreadPoolExecutor for concurrent execution
# Create ThreadPoolExecutor with 3 workers
# Submit 3 tasks using executor.submit()
# Store the Future objects and retrieve results with future.result()
# Measure total time (should be ~1 second due to concurrency)
# Write your code here:


# TODO 6-7: Use ThreadPoolExecutor.map() for batch processing
# Build 'calculate_square' function that takes number, sleeps 0.5s, returns square
# Use executor.map() to calculate squares of [1, 2, 3, 4, 5] concurrently
# Print results
# Hint: executor.map(calculate_square, [1, 2, 3, 4, 5])
# Write your code here:


# TODO 8-9: Handle results as they complete with as_completed()
# Build 'download_file' function simulating file download (2 second delay)
# Submit 5 download tasks to executor
# Use as_completed() to process results as soon as they're ready
# Hint: for future in as_completed(futures):
# Write your code here:


# TODO 10-11: Handle exceptions in concurrent tasks
# Build 'risky_task' function that raises ValueError if number is 0, else returns number * 2
# Submit multiple risky_tasks with [1, 2, 0, 3, 4]
# Use try-except when calling result() to handle exceptions
# Write your code here:


# BONUS TODO: Compare sequential vs concurrent performance
# Create I/O-bound tasks and run them both ways
# Measure and print the time difference to show concurrency speedup
# Write your code here:


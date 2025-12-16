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

# TODO 1: Create a simple function 'task' that:
# - Takes a task_id parameter
# - Sleeps for 1 second (simulating work)
# - Returns a message: "Task {task_id} completed"
# Write your code here:


# TODO 2: Test the task function sequentially
# Call it 3 times in a loop and measure the total time
# Hint: Use time.time() before and after
# Print the elapsed time (should be ~3 seconds)
# Write your code here:


# TODO 3: Create a ThreadPoolExecutor with 3 workers
# Use a with statement to ensure proper cleanup
# Hint: with ThreadPoolExecutor(max_workers=3) as executor:
# Write your code here:


# TODO 4: Submit 3 tasks to the executor
# Use executor.submit(task, task_id) for each task
# Store the Future objects in a list
# Write your code here:


# TODO 5: Get results from all futures
# Use future.result() to wait for and get each result
# Print each result
# Measure the total time (should be ~1 second, not 3!)
# Write your code here:


# TODO 6: Create a function 'calculate_square' that:
# - Takes a number
# - Sleeps for 0.5 seconds (simulating computation)
# - Returns the square of the number
# Write your code here:


# TODO 7: Use ThreadPoolExecutor to calculate squares of [1, 2, 3, 4, 5] concurrently
# Use executor.map() method
# Hint: executor.map(calculate_square, [1, 2, 3, 4, 5])
# Print the results
# Write your code here:


# TODO 8: Create a function 'download_file' that simulates downloading
# - Takes a file_id
# - Sleeps for 2 seconds
# - Returns "Downloaded file {file_id}"
# Write your code here:


# TODO 9: Submit multiple download tasks and process them as they complete
# Use as_completed() to process results as soon as they're ready
# Submit 5 download tasks
# Hint: for future in as_completed(futures):
# Write your code here:


# TODO 10: Create a function that might raise an exception
# Define 'risky_task' that takes a number
# If number is 0, raise ValueError("Cannot process zero")
# Otherwise, return number * 2
# Write your code here:


# TODO 11: Submit multiple risky_tasks to executor
# Use try-except when calling result() to handle exceptions
# Test with numbers [1, 2, 0, 3, 4]
# Write your code here:


# BONUS TODO: Compare sequential vs concurrent execution
# Create a function that performs multiple I/O-bound tasks
# Run it sequentially and then concurrently
# Print the time difference to see the speedup
# Write your code here:


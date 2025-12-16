"""
Mini-Program 4: Thread Pool Executor
Topic: Concurrent and Parallel Programming

Learning Objectives:
- Master ThreadPoolExecutor for I/O-bound tasks
- Understand when to use threads vs processes
- Manage thread pool size
- Handle shared resources safely

Instructions:
Complete this program to learn about thread pool executors.
"""

import time
from concurrent.futures import ThreadPoolExecutor
import threading

# TODO 1: Create a function 'fetch_data' that simulates fetching data
# Takes a url parameter
# Sleeps for 1 second (simulating network delay)
# Returns "Data from {url}"
# Write your code here:


# TODO 2: Fetch data from 5 URLs sequentially
# Measure and print the time (should be ~5 seconds)
# Write your code here:


# TODO 3: Use ThreadPoolExecutor to fetch data concurrently
# Create a list of 5 URLs
# Use executor.map() to fetch all concurrently
# Measure and print the time (should be ~1 second)
# Write your code here:


# TODO 4: Create a function 'get_thread_info' that:
# - Takes a task_id
# - Returns the thread name using threading.current_thread().name
# - Returns a message with task_id and thread name
# Write your code here:


# TODO 5: Submit multiple tasks to see different threads being used
# Use max_workers=3 to limit the thread pool size
# Submit 10 tasks and print thread names
# Write your code here:


# TODO 6: Create a shared counter variable
# Create a function 'increment_counter' that increments it
# WARNING: This will have race conditions (we'll fix this later)
# Submit 100 tasks to increment the counter
# Print the final value (may not be 100!)
# Write your code here:


# TODO 7: Fix the race condition using a threading.Lock
# Create a lock object
# Modify increment_counter to use the lock
# Now the final value should be exactly 100
# Write your code here:


# TODO 8: Create a function 'process_file' that simulates file processing
# Takes a filename
# Sleeps for 0.5 seconds (simulating I/O)
# Returns "Processed {filename}"
# Write your code here:


# TODO 9: Process 20 files using ThreadPoolExecutor
# Experiment with different max_workers values (1, 5, 10, 20)
# Measure and compare execution times
# Write your code here:


# TODO 10: Create a function 'api_call' that:
# - Takes an endpoint name
# - Sleeps for random time between 0.5 and 2 seconds
# - Returns response data
# Write your code here:


# TODO 11: Make 10 API calls concurrently
# Handle any potential exceptions
# Use try-except in a wrapper function
# Write your code here:


# TODO 12: Implement a rate limiter
# Create a function that can only be called N times per second
# Use threading.Semaphore to limit concurrent calls
# Write your code here:


# TODO 13: Create a producer-consumer pattern
# Producer: Generate work items
# Consumer: Process work items using ThreadPoolExecutor
# Use a queue to pass work between them
# Write your code here:


# BONUS TODO: Create a thread pool that processes tasks in priority order
# Tasks have different priorities
# Higher priority tasks should be processed first
# Use a priority queue and ThreadPoolExecutor
# Write your code here:


"""
Mini-Program 2: Process Pools
Topic: Multiprocessing

Learning Objectives:
- Use multiprocessing.Pool for parallel execution
- Apply functions to multiple inputs in parallel
- Understand pool.map(), pool.apply(), and pool.starmap()
- Manage a pool of worker processes

Instructions:
Complete this program to learn about process pools.
"""

import multiprocessing
import time

# TODO 1: Create a function 'square' that:
# - Takes a number
# - Returns the square of the number
# Write your code here:


# TODO 2: Use Pool.map() to calculate squares in parallel
# Create a pool with 4 workers
# Calculate squares of [1, 2, 3, 4, 5, 6, 7, 8]
# Hint: with multiprocessing.Pool(4) as pool:
#           results = pool.map(square, numbers)
# Write your code here:


# TODO 3: Compare sequential vs parallel execution time
# Create a slow function that sleeps before returning
# Time both sequential and parallel execution
# Write your code here:


# TODO 4: Use Pool.map() with a larger dataset
# Process a list of 100 numbers
# Use pool.map() to apply a function to all
# Write your code here:


# TODO 5: Create a function 'add' that takes two parameters
# Use Pool.starmap() to apply it to pairs of numbers
# Hint: starmap unpacks tuples as arguments
# Example: pool.starmap(add, [(1,2), (3,4), (5,6)])
# Write your code here:


# TODO 6: Use Pool.apply() for a single task
# apply() blocks until the result is ready
# Hint: result = pool.apply(function, args=(arg1, arg2))
# Write your code here:


# TODO 7: Use Pool.apply_async() for asynchronous execution
# apply_async() returns immediately with a AsyncResult object
# Use result.get() to retrieve the value
# Write your code here:


# TODO 8: Process multiple tasks asynchronously
# Submit several tasks with apply_async()
# Collect results from all AsyncResult objects
# Write your code here:


# TODO 9: Create a function that processes a chunk of data
# Use Pool.map() to process chunks in parallel
# Combine results from all chunks
# Write your code here:


# TODO 10: Set the number of processes based on CPU count
# Use multiprocessing.cpu_count()
# Create a pool with that many workers
# Write your code here:


# TODO 11: Use Pool.imap() for lazy iteration
# imap() returns an iterator, results as they become available
# Good for large datasets that don't fit in memory
# Write your code here:


# TODO 12: Use Pool.map_async() for non-blocking map
# map_async() returns AsyncResult immediately
# Use callback parameter to process results
# Write your code here:


# TODO 13: Handle errors in pool workers
# Create a function that sometimes raises an exception
# Use try-except when getting results
# Write your code here:


# BONUS TODO: Implement a parallel file processor
# Given a list of files, process each file in parallel
# Use Pool.map() to distribute work
# Combine results from all files
# Write your code here:


"""
Mini-Program 4: Async Gathering and Coordination
Topic: Asyncio

Learning Objectives:
- Use asyncio.gather() for concurrent execution
- Handle exceptions in gather()
- Use return_exceptions parameter
- Coordinate multiple async operations

Instructions:
Complete this program to learn about async gathering and coordination.
"""

import asyncio
import random

# TODO 1: Create async functions for different operations
# Define 'fetch_weather', 'fetch_news', 'fetch_stocks'
# Each takes 1-2 seconds and returns data
# Write your code here:


# TODO 2: Use gather() to fetch all data concurrently
# Hint: results = await asyncio.gather(fetch_weather(), fetch_news(), fetch_stocks())
# Print all results
# Write your code here:


# TODO 3: Create an async function that sometimes fails
# Define 'unreliable_fetch' that randomly raises an exception
# Use random.random() < 0.5 to decide
# Write your code here:


# TODO 4: Use gather() without return_exceptions (default)
# If any task fails, gather raises the exception immediately
# Use try-except to handle it
# Write your code here:


# TODO 5: Use gather() with return_exceptions=True
# Failed tasks return exceptions as values
# Check each result to see if it's an exception
# Hint: results = await asyncio.gather(*tasks, return_exceptions=True)
#       if isinstance(result, Exception):
# Write your code here:


# TODO 6: Gather results with different return types
# Some coroutines return strings, some return numbers
# Collect all results in a list
# Write your code here:


# TODO 7: Use gather with unpacking
# Pass multiple coroutines as arguments
# Hint: await asyncio.gather(*[coro() for _ in range(5)])
# Write your code here:


# TODO 8: Implement scatter-gather pattern
# Scatter: Send requests to multiple services
# Gather: Collect all responses
# Write your code here:


# TODO 9: Use asyncio.gather() vs asyncio.wait()
# gather: Returns results in order
# wait: Returns done and pending sets
# Compare both approaches
# Write your code here:


# TODO 10: Implement timeout for gather()
# Use asyncio.wait_for() to wrap gather() with timeout
# Write your code here:


# TODO 11: Create a fan-out/fan-in pattern
# Fan-out: Split work into multiple tasks
# Fan-in: Combine results from all tasks
# Write your code here:


# TODO 12: Gather nested coroutines
# Coroutines that themselves use gather
# Create a hierarchy of async operations
# Write your code here:


# TODO 13: Process results as they complete with as_completed
# Instead of waiting for all, process each as it finishes
# Hint: for coro in asyncio.as_completed([coro1(), coro2(), coro3()]):
# Write your code here:


# TODO 14: Implement partial failure handling
# Continue with successful results even if some tasks fail
# Use return_exceptions=True and filter results
# Write your code here:


# BONUS TODO: Create an async aggregator
# Fetches data from multiple sources concurrently
# Combines and processes all results
# Handles failures gracefully
# Returns aggregated result
# Write your code here:


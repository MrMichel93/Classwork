"""
Mini-Program 2: Async/Await Patterns
Topic: Asyncio

Learning Objectives:
- Master async/await syntax
- Run multiple coroutines concurrently
- Use asyncio.create_task() for concurrent execution
- Understand when to use await

Instructions:
Complete this program to learn async/await patterns.
"""

import asyncio
import time

# TODO 1: Create an async function 'fetch_user' that:
# - Takes a user_id
# - Simulates API call with await asyncio.sleep(1)
# - Returns "User {user_id}"
# Write your code here:


# TODO 2: Create an async main that fetches 3 users sequentially
# Time the execution (should be ~3 seconds)
# Write your code here:


# TODO 3: Use asyncio.create_task() to run tasks concurrently
# Create tasks for each user fetch
# Await all tasks
# Time the execution (should be ~1 second!)
# Hint: task1 = asyncio.create_task(fetch_user(1))
# Write your code here:


# TODO 4: Create multiple tasks and await them
# Store tasks in a list
# Await each task to get results
# Write your code here:


# TODO 5: Create an async function 'process_data' that:
# - Takes data and delay parameters
# - Awaits asyncio.sleep(delay)
# - Returns processed data
# Write your code here:


# TODO 6: Process multiple data items concurrently
# Create tasks for different data with different delays
# Collect all results
# Write your code here:


# TODO 7: Demonstrate the difference:
# Sequential: await func1(); await func2(); await func3()
# Concurrent: Create tasks first, then await all
# Show the time difference
# Write your code here:


# TODO 8: Create an async function that awaits another async function
# Chain async calls: async_func1 awaits async_func2
# Write your code here:


# TODO 9: Handle task results
# Create tasks, store them
# Get results using await task
# Print results in order of completion
# Write your code here:


# TODO 10: Create an async function that doesn't need await
# An async function that does only synchronous work
# Notice it still needs to be awaited when called
# Write your code here:


# TODO 11: Use asyncio.gather() to run multiple coroutines
# gather() is an alternative to creating individual tasks
# Hint: results = await asyncio.gather(coro1(), coro2(), coro3())
# Write your code here:


# TODO 12: Compare create_task vs gather
# create_task: More control, can cancel individual tasks
# gather: Simpler for running many coroutines
# Write your code here:


# TODO 13: Cancel a task
# Create a long-running task
# Cancel it using task.cancel()
# Handle the CancelledError exception
# Write your code here:


# BONUS TODO: Create a async function that retries on failure
# If an operation fails, retry up to 3 times
# Use await and exception handling
# Write your code here:


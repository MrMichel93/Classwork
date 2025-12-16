"""
Mini-Program 1: Asyncio Basics
Topic: Asyncio

Learning Objectives:
- Understand asynchronous programming concepts
- Create coroutines using async/await syntax
- Run coroutines with asyncio.run()
- Understand the event loop

Instructions:
Complete this program to learn the basics of asyncio.
"""

import asyncio
import time

# TODO 1: Create a simple async function (coroutine)
# Use 'async def' to define it
# Make it print a message and await asyncio.sleep(1)
# Hint: async def say_hello():
#           print("Hello")
#           await asyncio.sleep(1)
# Write your code here:


# TODO 2: Run the coroutine using asyncio.run()
# Hint: asyncio.run(say_hello())
# Write your code here:


# TODO 3: Create an async function that returns a value
# Define 'fetch_data' that simulates fetching data
# await asyncio.sleep(2) then return "Data fetched"
# Write your code here:


# TODO 4: Run fetch_data and print the result
# Store the result from asyncio.run() and print it
# Write your code here:


# TODO 5: Create an async function with parameters
# Define 'greet' that takes a name
# Awaits asyncio.sleep(1) then prints greeting
# Write your code here:


# TODO 6: Run the greet function with different names
# Call it multiple times sequentially
# Notice the total time is sum of all sleeps
# Write your code here:


# TODO 7: Understand the difference between sync and async sleep
# Create two functions: one with time.sleep(), one with await asyncio.sleep()
# Try to run them and observe the difference
# Write your code here:


# TODO 8: Create an async function 'count' that:
# - Takes a name and counts from 1 to 3
# - Awaits asyncio.sleep(1) between counts
# - Prints: "{name}: {count}"
# Write your code here:


# TODO 9: Try to call an async function without await (won't work!)
# Call count("test") directly without asyncio.run()
# See the warning about coroutine never being awaited
# Write your code here:


# TODO 10: Create an async main function
# Inside, await multiple calls to count with different names
# This is still sequential (we'll fix this next)
# Write your code here:


# TODO 11: Measure execution time for sequential async calls
# Time how long it takes to await count() three times
# Should be ~3 seconds (sequential)
# Write your code here:


# TODO 12: Create a function that demonstrates async is not parallel by default
# Without proper concurrency, async functions run sequentially
# Write your code here:


# BONUS TODO: Create a chain of async functions
# Function A awaits function B, which awaits function C
# Run function A and see how they all execute
# Write your code here:


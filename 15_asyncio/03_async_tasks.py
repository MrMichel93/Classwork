"""
Mini-Program 3: Managing Async Tasks
Topic: Asyncio

Learning Objectives:
- Create and manage asyncio tasks
- Cancel and timeout tasks
- Handle task exceptions
- Monitor task status

Instructions:
Complete this program to learn about managing async tasks.
"""

import asyncio

# TODO 1: Create an async function 'long_task' that:
# - Takes a task_id
# - Runs for 5 seconds (await asyncio.sleep(5))
# - Returns completion message
# Write your code here:


# TODO 2: Create a task and check its status
# Use task.done() to check if completed
# Check before and after awaiting
# Write your code here:


# TODO 3: Create a task and cancel it
# Create task, wait 1 second, then cancel with task.cancel()
# Check task.cancelled()
# Write your code here:


# TODO 4: Handle CancelledError in a task
# Modify long_task to catch CancelledError
# Perform cleanup when cancelled
# Write your code here:


# TODO 5: Use asyncio.wait_for() with timeout
# Wrap a coroutine with a timeout
# Hint: await asyncio.wait_for(long_task(1), timeout=2)
# Handle TimeoutError
# Write your code here:


# TODO 6: Create a function that times out and retries
# Try to complete a task with a timeout
# If it times out, try again with longer timeout
# Write your code here:


# TODO 7: Get task name
# Create tasks with names
# Use task.get_name() and task.set_name()
# Write your code here:


# TODO 8: Create a background task
# A task that runs in the background while main code continues
# Main coroutine creates task but doesn't immediately await it
# Write your code here:


# TODO 9: Use asyncio.shield() to protect a task from cancellation
# Shield a task so it completes even if parent is cancelled
# Write your code here:


# TODO 10: Handle exceptions in tasks
# Create a task that raises an exception
# Get the exception with task.exception()
# Write your code here:


# TODO 11: Create multiple tasks with different completion times
# Use asyncio.as_completed() to process them as they finish
# Hint: for coro in asyncio.as_completed(tasks):
# Write your code here:


# TODO 12: Use asyncio.wait() with different return conditions
# FIRST_COMPLETED: Return when first task completes
# ALL_COMPLETED: Return when all complete (default)
# Hint: done, pending = await asyncio.wait(tasks, return_when=FIRST_COMPLETED)
# Write your code here:


# TODO 13: Implement task result caching
# Store task results so they don't need to be recomputed
# Use a dictionary to cache results by task parameters
# Write your code here:


# BONUS TODO: Create a task manager class
# Methods: add_task, cancel_all, wait_all, get_results
# Manages a collection of tasks
# Write your code here:


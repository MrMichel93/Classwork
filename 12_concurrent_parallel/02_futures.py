"""
Mini-Program 2: Working with Futures
Topic: Concurrent and Parallel Programming

Learning Objectives:
- Understand Future objects
- Check future status (done, running, cancelled)
- Add callbacks to futures
- Handle future timeouts

Instructions:
Complete this program to learn about working with futures.
"""

import time
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED, ALL_COMPLETED

# TODO 1: Create a function 'slow_task' that:
# - Takes task_id and duration parameters
# - Sleeps for the specified duration
# - Returns "Task {task_id} completed after {duration} seconds"
# Write your code here:


# TODO 2: Create a ThreadPoolExecutor
# Submit a slow_task with duration=2
# Check if the future is done immediately (it shouldn't be)
# Use future.done()
# Write your code here:


# TODO 3: Wait for the future to complete using result()
# Check if it's done after calling result()
# Print the result
# Write your code here:


# TODO 4: Submit a task and use a timeout when getting the result
# Use future.result(timeout=1) with a task that takes 2 seconds
# Catch TimeoutError and print a message
# Write your code here:


# TODO 5: Create a callback function 'task_completed_callback'
# It should take a future as parameter
# Print "Callback: Task completed with result: {future.result()}"
# Write your code here:


# TODO 6: Submit a task and add the callback to it
# Use future.add_done_callback(callback_function)
# Wait for the task to complete
# Write your code here:


# TODO 7: Submit multiple tasks with different durations
# Use wait() with return_when=FIRST_COMPLETED
# Print which task completed first
# Hint: done, not_done = wait(futures, return_when=FIRST_COMPLETED)
# Write your code here:


# TODO 8: Submit multiple tasks
# Use wait() with return_when=ALL_COMPLETED
# Process all results after they're all done
# Write your code here:


# TODO 9: Create a function 'check_website' that simulates checking a website
# Takes a url parameter
# Sleeps for random time (0.5 to 2 seconds)
# Returns "Website {url} is up"
# Write your code here:


# TODO 10: Submit checks for multiple websites concurrently
# Use as_completed to process results as they finish
# Print results with timestamps to show order of completion
# Hint: Use time.time() to get timestamps
# Write your code here:


# TODO 11: Implement cancellation
# Submit a slow task (5+ seconds)
# Wait for 1 second
# Try to cancel the future using future.cancel()
# Check if it was cancelled using future.cancelled()
# Write your code here:


# TODO 12: Create a function 'process_batch' that:
# - Takes a batch_id and list of items
# - Processes each item (simulate with sleep)
# - Returns the number of items processed
# Write your code here:


# TODO 13: Submit multiple batch processing tasks
# Get results with a timeout for each
# If timeout occurs, cancel remaining tasks
# Write your code here:


# BONUS TODO: Create a progress tracking system
# Submit multiple tasks, periodically check how many are done
# Print progress percentage every second until all complete
# Write your code here:


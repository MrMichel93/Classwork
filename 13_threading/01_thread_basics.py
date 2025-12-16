"""
Mini-Program 1: Threading Basics
Topic: Threading

Learning Objectives:
- Create and start threads using threading module
- Understand the difference between main thread and child threads
- Use Thread class for concurrent execution
- Pass arguments to threads

Instructions:
Complete this program to learn the basics of threading.
"""

import threading
import time

# TODO 1: Create a simple function 'print_numbers' that:
# - Prints numbers 1 to 5
# - Sleeps for 0.5 seconds between each number
# - Prints the thread name for each iteration
# Hint: Use threading.current_thread().name
# Write your code here:


# TODO 2: Run print_numbers in the main thread
# Observe the sequential execution
# Write your code here:


# TODO 3: Create a thread to run print_numbers
# Use threading.Thread(target=print_numbers)
# Start the thread using thread.start()
# Write your code here:


# TODO 4: Create two threads running print_numbers simultaneously
# Start both threads
# See how they execute concurrently
# Write your code here:


# TODO 5: Create a function 'print_letters' that:
# - Takes a letter parameter
# - Prints the letter 5 times with 0.5 second delays
# Write your code here:


# TODO 6: Create multiple threads with different arguments
# Pass different letters to each thread
# Hint: threading.Thread(target=print_letters, args=('A',))
# Write your code here:


# TODO 7: Use thread.join() to wait for threads to complete
# Create 3 threads
# Start all of them
# Call join() on each to wait for completion
# Print "All threads completed" at the end
# Write your code here:


# TODO 8: Demonstrate the difference with and without join()
# Without join: Main thread finishes before worker threads
# With join: Main thread waits for worker threads
# Write your code here:


# TODO 9: Set custom thread names
# Create threads with name parameter
# Hint: threading.Thread(target=func, name="CustomName")
# Write your code here:


# TODO 10: Create a function 'worker' that takes a worker_id
# The function should print start message, work for 2 seconds, print done message
# Create 3 worker threads with different IDs
# Write your code here:


# TODO 11: Check if a thread is alive
# Create a thread, start it
# Print thread.is_alive() before and after it completes
# Write your code here:


# TODO 12: Get all active threads
# Create several threads
# Use threading.enumerate() to list all threads
# Print the count and names of active threads
# Write your code here:


# TODO 13: Create daemon threads
# Daemon threads automatically terminate when main program exits
# Create a thread with daemon=True
# Compare behavior with regular threads
# Write your code here:


# BONUS TODO: Create a thread that runs indefinitely
# Make it a daemon thread so it doesn't prevent program exit
# Use a while loop and check for termination condition
# Write your code here:


"""
Mini-Program 1: Multiprocessing Basics
Topic: Multiprocessing

Learning Objectives:
- Create and start processes using multiprocessing module
- Understand the difference between processes and threads
- Pass arguments to processes
- Wait for processes to complete

Instructions:
Complete this program to learn the basics of multiprocessing.
"""

import multiprocessing
import os
import time

# TODO 1: Create a simple function 'print_info' that:
# - Prints the process name using multiprocessing.current_process().name
# - Prints the process ID using os.getpid()
# - Prints the parent process ID using os.getppid()
# Write your code here:


# TODO 2: Run print_info in the main process
# Observe the process information
# Write your code here:


# TODO 3: Create a process to run print_info
# Use multiprocessing.Process(target=print_info)
# Start the process using process.start()
# Wait for it using process.join()
# Write your code here:


# TODO 4: Create multiple processes running the same function
# Create 3 processes
# Start all of them
# Notice they have different process IDs
# Write your code here:


# TODO 5: Create a function 'calculate_square' that:
# - Takes a number as parameter
# - Prints the number and its square
# - Sleeps for 1 second
# Write your code here:


# TODO 6: Create processes with arguments
# Create 5 processes calculating squares of different numbers
# Hint: multiprocessing.Process(target=calculate_square, args=(5,))
# Write your code here:


# TODO 7: Set custom process names
# Create processes with the name parameter
# Hint: multiprocessing.Process(target=func, name="CustomName")
# Write your code here:


# TODO 8: Demonstrate the difference with and without join()
# Without join: Main process may finish before child processes
# With join: Main process waits for child processes
# Write your code here:


# TODO 9: Check if a process is alive
# Create a process that runs for 3 seconds
# Check process.is_alive() before, during, and after execution
# Write your code here:


# TODO 10: Get the exit code of a process
# Use process.exitcode
# None: still running, 0: successful, other: error code
# Write your code here:


# TODO 11: Terminate a process
# Create a long-running process
# Use process.terminate() to stop it
# Check if it's still alive after termination
# Write your code here:


# TODO 12: Create daemon processes
# Daemon processes automatically terminate when main process exits
# Set daemon=True when creating the process
# Write your code here:


# TODO 13: Get the number of CPU cores
# Use multiprocessing.cpu_count()
# Create that many processes for parallel work
# Write your code here:


# BONUS TODO: Create a worker process that runs a loop
# Use a flag or signal to gracefully stop the process
# Compare with terminate() which is forceful
# Write your code here:


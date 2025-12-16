"""
Mini-Program 2: Thread Synchronization
Topic: Threading

Learning Objectives:
- Understand race conditions in multi-threaded programs
- Use synchronization primitives to avoid race conditions
- Work with shared resources safely
- Understand the importance of thread-safe code

Instructions:
Complete this program to learn about thread synchronization.
"""

import threading
import time

# Global counter for demonstrating race conditions
counter = 0

# TODO 1: Create a function 'increment_counter' that:
# - Increments the global counter 100000 times
# - Use a loop: for _ in range(100000)
# Write your code here:


# TODO 2: Create two threads that both run increment_counter
# Start both threads and wait for completion using join()
# Print the final counter value
# Expected: 200000, Actual: Likely less due to race condition!
# Write your code here:


# TODO 3: Create a Lock to fix the race condition
# Create a lock: lock = threading.Lock()
# Modify increment_counter to acquire/release the lock
# Hint: lock.acquire() ... lock.release()
# or use: with lock:
# Write your code here:


# TODO 4: Test with the lock
# Reset counter to 0
# Create two threads with the fixed increment_counter
# The final value should now be exactly 200000
# Write your code here:


# TODO 5: Demonstrate lock contention
# Create a function that holds a lock for different durations
# Show how one thread must wait for another
# Write your code here:


# TODO 6: Create a shared list
# Create a function 'add_items' that appends items to the list
# Use a lock to make it thread-safe
# Create multiple threads adding items
# Write your code here:


# TODO 7: Implement a thread-safe counter class
# Create a class ThreadSafeCounter with:
# - __init__ initializing value to 0 and creating a lock
# - increment() method (thread-safe)
# - get_value() method (thread-safe)
# Write your code here:


# TODO 8: Test the ThreadSafeCounter with multiple threads
# Create several threads incrementing the counter
# Verify the final value is correct
# Write your code here:


# TODO 9: Demonstrate deadlock (and how to avoid it)
# Create two locks: lock1, lock2
# Thread1: acquire lock1, then lock2
# Thread2: acquire lock2, then lock1
# This causes deadlock! (Comment out after demonstrating)
# Write your code here:


# TODO 10: Fix the deadlock by acquiring locks in the same order
# Both threads should acquire lock1 first, then lock2
# Write your code here:


# TODO 11: Create a bounded resource using Semaphore
# Example: A resource that allows only 3 concurrent users
# Create semaphore: semaphore = threading.Semaphore(3)
# Create a function that uses the resource
# Write your code here:


# TODO 12: Test the semaphore with more threads than the limit
# Create 10 threads that try to access a resource with limit 3
# Only 3 should be able to access at a time
# Write your code here:


# BONUS TODO: Implement a simple thread-safe queue
# Create a class with methods: put(), get()
# Use locks to make it thread-safe
# Create producer and consumer threads
# Write your code here:


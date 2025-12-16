"""
Mini-Program 3: Thread Locks and RLocks
Topic: Threading

Learning Objectives:
- Master different types of locks
- Use RLock for reentrant locking
- Understand when to use each lock type
- Implement complex synchronization patterns

Instructions:
Complete this program to learn about thread locks.
"""

import threading
import time

# TODO 1: Create a function demonstrating Lock usage
# Create a lock and use it to protect a critical section
# Use both lock.acquire()/release() and with statement
# Write your code here:


# TODO 2: Demonstrate Lock non-reentrant behavior
# Try to acquire the same lock twice in the same thread
# This will cause a deadlock (comment out after demonstrating)
# Hint:
# lock = threading.Lock()
# lock.acquire()
# lock.acquire()  # This will block forever!
# Write your code here:


# TODO 3: Create an RLock (Reentrant Lock)
# RLock can be acquired multiple times by the same thread
# Demonstrate acquiring it multiple times
# Write your code here:


# TODO 4: Create a function that uses RLock recursively
# Example: A recursive function that needs to maintain a lock
# Write your code here:


# TODO 5: Implement a Bank Account class with Lock
# Methods: deposit, withdraw, get_balance
# All methods should be thread-safe using a lock
# Write your code here:


# TODO 6: Test the Bank Account with multiple threads
# Create threads that deposit and withdraw simultaneously
# Verify the balance is correct at the end
# Write your code here:


# TODO 7: Create a Reader-Writer scenario
# Multiple threads can read simultaneously
# Only one thread can write at a time
# Use locks to implement this pattern
# Write your code here:


# TODO 8: Implement timeout for lock acquisition
# Use lock.acquire(timeout=1)
# Handle the case when lock cannot be acquired
# Write your code here:


# TODO 9: Create a function that tries to acquire a lock
# If it can't acquire immediately, it does something else
# Use lock.acquire(blocking=False)
# Write your code here:


# TODO 10: Demonstrate lock.locked() method
# Check if a lock is currently held
# Write your code here:


# TODO 11: Create a priority lock system
# Threads with higher priority should acquire lock first
# Use a custom implementation with conditions
# Write your code here:


# TODO 12: Implement a two-phase locking protocol
# Acquire all locks before starting work
# Release all locks after completing work
# Prevents deadlocks in complex scenarios
# Write your code here:


# TODO 13: Create a fair lock implementation
# Ensure threads get the lock in FIFO order
# Use a queue and condition variable
# Write your code here:


# BONUS TODO: Implement a read-write lock class
# Allow multiple readers or one writer
# Use RLock and counters to track readers
# Write your code here:


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

# TODO 1-4: Demonstrate a race condition and then repair it with synchronization
# Suggested piece: increment_counter(...) operating on shared state, plus a locked variant of the same workload.
# Make the before/after outcome visible so learners can see what synchronization changes.
# Write your code here:


# TODO 5-8: Explore contention and safer shared abstractions
# Include one example of several threads competing for a shared resource and one thread-safe counter-style class.
# Show the class or function signatures you choose, but keep the implementation path open-ended.
# Write your code here:


# TODO 9-10: Contrast deadlock with a safer locking discipline
# Use two resources or locks so the failure mode is easy to reason about.
# Focus on what property makes one version risky and the other version safer.
# Write your code here:


# TODO 11-12: Model limited-capacity access with a semaphore
# Suggested structure: a shared resource function plus more worker threads than available slots.
# Emphasize bounded concurrency rather than exact timing details.
# Write your code here:


# BONUS TODO: Build a small thread-safe queue abstraction
# Suggested shape: put(item) and get() methods with producer and consumer examples.
# Write your code here:

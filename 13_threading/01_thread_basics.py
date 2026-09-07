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

# TODO 1-4: Introduce thread creation by reusing one simple worker function
# Suggested piece: print_numbers() with visible timing and thread-name output.
# Compare calling it directly, running it on one thread, and running it on two threads at once.
# Write your code here:


# TODO 5-6: Pass arguments into thread targets
# Suggested piece: print_letters(letter) so each thread can do similar work with different input.
# Make the thread setup easy to read by showing the target signature.
# Write your code here:


# TODO 7-8: Show why joining threads changes program behavior
# Build one example where the main thread waits and one where it does not.
# Focus on the observable difference in completion order rather than the mechanics of the loop.
# Write your code here:


# TODO 9-10: Give threads clearer identities and responsibilities
# Suggested piece: worker(worker_id) that announces when it starts and finishes.
# Use names or IDs so learners can match each message to the correct thread.
# Write your code here:


# TODO 11-13: Inspect the lifecycle of active and daemon threads
# Include one example using is_alive(), one using threading.enumerate(), and one daemon-thread example.
# Emphasize what the runtime can tell you about currently running work.
# Write your code here:


# BONUS TODO: Add a long-running background thread example
# Keep the focus on why a daemon-style background worker does not block program exit.
# Write your code here:

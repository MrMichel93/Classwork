"""
Mini-Program 4: Shared Memory and Values
Topic: Multiprocessing

Learning Objectives:
- Use Value and Array for shared memory
- Use Manager for shared objects
- Synchronize access to shared memory
- Understand when to use shared memory vs queues

Instructions:
Complete this program to learn about shared memory in multiprocessing.
"""

import multiprocessing
import time

# TODO 1-4: Use a shared scalar value and make its synchronization needs visible
# Suggested pieces: a shared Value plus one worker that updates it, first unsafely and then with coordination.
# Focus on what changes when multiple processes mutate the same memory location.
# Write your code here:


# TODO 5-6: Work with a shared array across processes
# Suggested piece: a worker that transforms or annotates part of the array.
# Make the array shape and worker signature easy to recognize from the hints.
# Write your code here:


# TODO 7-9: Share richer state with a Manager
# Include a shared list example and a shared dictionary example.
# Emphasize when manager-backed objects are more expressive than low-level shared memory.
# Write your code here:


# TODO 10-13: Compare ways to coordinate mutable shared state
# Cover a counter abstraction, a queue-versus-shared-memory comparison, a namespace-style object, and one shared-state design of your choice.
# Focus on trade-offs between simplicity, structure, and performance.
# Write your code here:


# BONUS TODO: Apply shared memory to a parallel algorithm
# Suggested target: a merge-sort style workload that benefits from processes working on separate regions of shared data.
# Write your code here:

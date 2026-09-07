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

# TODO 1-4: Compare basic locks and reentrant locks
# Suggested pieces: a simple critical-section example and a recursive function that benefits from an RLock.
# Show the target signatures or helper names so the learner can see the intended structure at a glance.
# Write your code here:


# TODO 5-6: Protect a small shared object with a lock
# Suggested piece: a BankAccount-style class with methods such as deposit(...) and withdraw(...).
# Focus on preserving consistent state when several threads use the object at once.
# Write your code here:


# TODO 7-10: Explore practical lock usage patterns
# Include a reader/writer-style scenario, timed lock acquisition, a non-blocking acquisition attempt, and lock state inspection.
# Emphasize what information or guarantees each pattern gives the program.
# Write your code here:


# TODO 11-13: Design higher-level lock policies
# Cover priority-aware access, a two-phase workflow, and one fairness-oriented lock idea.
# Keep the hints conceptual so learners decide how to represent waiting threads and turn-taking.
# Write your code here:


# BONUS TODO: Create a read-write lock abstraction
# Suggested shape: separate reader and writer entry/exit methods or context-manager style helpers.
# Write your code here:

"""
Mini-Program 4: Thread Pool Executor
Topic: Concurrent and Parallel Programming

Learning Objectives:
- Master ThreadPoolExecutor for I/O-bound tasks
- Understand when to use threads vs processes
- Manage thread pool size
- Handle shared resources safely

Instructions:
Complete this program to learn about thread pool executors.
"""

import time
from concurrent.futures import ThreadPoolExecutor
import threading

# TODO 1-3: Compare sequential and thread-pool handling of I/O-shaped work
# Suggested piece: fetch_data(url) -> str.
# Use the same workload in both styles so learners can see when a ThreadPoolExecutor improves responsiveness.
# Write your code here:


# TODO 4-5: Inspect how a thread pool reuses worker threads
# Suggested piece: get_thread_info(task_id) -> str.
# Make the output reveal task identity and thread identity without prescribing the exact formatting.
# Write your code here:


# TODO 6-7: Demonstrate a shared-state race and then protect it
# Suggested pieces: a shared counter and a lock-aware update path.
# Focus on why thread coordination matters when several tasks touch the same state.
# Write your code here:


# TODO 8-9: Use the pool for a larger batch of independent file-style tasks
# Suggested piece: process_file(file_name) -> result summary.
# Keep the scenario conceptual: many small jobs, limited workers, collected results.
# Write your code here:


# TODO 10-13: Model an API workload with concurrency controls
# Suggested piece: api_call(endpoint) -> response summary, plus a rate-limiting or producer-consumer layer.
# Emphasize safe throughput and coordination rather than step-by-step implementation details.
# Write your code here:


# BONUS TODO: Build a priority-aware thread-pool workflow
# Surface the idea that not every task must be treated equally when work enters the system.
# Write your code here:

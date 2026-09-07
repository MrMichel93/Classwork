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

# TODO 1-4: Explore the lifecycle of a Future from submission to completion
# Suggested pieces: slow_task(task_id, duration) and a small executor workflow.
# Show what changes when work is pending, when a result is retrieved, and when a timeout occurs.
# Write your code here:


# TODO 5-8: Compare callback-driven and wait-based coordination
# Suggested pieces: task_completed_callback(future), several submitted tasks, and both FIRST_COMPLETED and ALL_COMPLETED cases.
# Focus on how the program learns that work is finished and when it chooses to handle results.
# Write your code here:


# TODO 9-10: Build a small concurrent website-status checker
# Suggested piece: check_website(url) plus a batch of URLs.
# Surface completion order and timing so learners can see that finished work may arrive out of submission order.
# Write your code here:


# TODO 11: Investigate what cancellation can and cannot do for futures
# Use one example where work has not started yet and one where work is already running.
# Highlight the difference between direct cancellation and cooperative stop signaling.
# Write your code here:


# TODO 12-13: Model batch-oriented work with per-batch result handling
# Suggested piece: process_batch(batch_id, items) returning a batch summary.
# Emphasize coordinating several batches, applying time limits, and deciding what to do with unfinished work.
# Write your code here:


# BONUS TODO: Add lightweight progress reporting for a set of futures
# Report how much of the workload has finished over time without prescribing a specific display style.
# Write your code here:

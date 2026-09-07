"""
Mini-Program 3: Process Pool Executor
Topic: Concurrent and Parallel Programming

Learning Objectives:
- Understand ProcessPoolExecutor for CPU-bound tasks
- Differentiate between processes and threads
- Use multiprocessing for parallel computation
- Work with process pool executors

Instructions:
Complete this program to learn about process-based parallelism.
"""

import time
from concurrent.futures import ProcessPoolExecutor
import os

# TODO 1-3: Compare sequential and process-based execution for a CPU-heavy task
# Suggested piece: calculate_prime_count(n) returning how much prime work was found for an input size.
# Keep the mathematical hint light and focus on measuring the difference between one-process and multi-process execution.
# Write your code here:


# TODO 4-5: Show how process pool tasks run in worker processes
# Suggested piece: get_process_info(task_id) -> str.
# Make the output reveal which PID handled each task and how that differs from the main process.
# Write your code here:


# TODO 6-7: Practice sending pure computation to the process pool
# Suggested piece: factorial(n) -> int.
# Use a few inputs to reinforce that process pools are a good fit for independent CPU-bound work.
# Write your code here:


# TODO 8-9: Split a large numeric job into chunks and combine the partial results
# Suggested piece: sum_of_squares(start, end) or sum_of_squares(range_chunk).
# Highlight the structure of chunking, parallel processing, and reduction into one final answer.
# Write your code here:


# TODO 10-12: Compare executor choices and size a process pool intentionally
# Suggested piece: process_data(data_list) for repeatable CPU-heavy work.
# Contrast thread and process pools conceptually, then create a pool sized to available CPU resources.
# Write your code here:


# BONUS TODO: Create a small map-reduce style computation
# Keep the focus on the map stage producing partial results and the reduce stage combining them.
# Write your code here:

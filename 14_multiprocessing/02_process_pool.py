"""
Mini-Program 2: Process Pools
Topic: Multiprocessing

Learning Objectives:
- Use multiprocessing.Pool for parallel execution
- Apply functions to multiple inputs in parallel
- Understand pool.map(), pool.apply(), and pool.starmap()
- Manage a pool of worker processes

Instructions:
Complete this program to learn about process pools.
"""

import multiprocessing
import time

# TODO 1-4: Compare sequential and pooled processing for the same pure function
# Suggested piece: square(number) -> number.
# Use both small and larger datasets so learners can see how Pool.map(...) changes the shape of the workload.
# Write your code here:


# TODO 5-8: Explore single-task and asynchronous pool interactions
# Suggested piece: add(a, b) -> number, plus a batch of async submissions.
# Focus on the difference between immediate blocking calls and result objects that complete later.
# Write your code here:


# TODO 9-12: Work with chunked data and alternative pool iteration styles
# Include a chunk-processing function, deliberate process-count selection, a lazy iteration example, and a non-blocking bulk map.
# Emphasize how each API changes when results become available.
# Write your code here:


# TODO 13: Handle worker-side failures in a process pool
# Use a task that can fail for some inputs and make the resulting behavior visible.
# Write your code here:


# BONUS TODO: Sketch a parallel file-processing workflow
# Focus on how files are partitioned, processed independently, and collected into one final summary.
# Write your code here:

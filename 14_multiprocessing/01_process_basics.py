"""
Mini-Program 1: Multiprocessing Basics
Topic: Multiprocessing

Learning Objectives:
- Create and start processes using multiprocessing module
- Understand the difference between processes and threads
- Pass arguments to processes
- Wait for processes to complete

Instructions:
Complete this program to learn the basics of multiprocessing.
"""

import multiprocessing
import os
import time

# TODO 1-4: Introduce process creation with one reusable worker function
# Suggested piece: print_info() that reports process identity information.
# Compare calling it in the main process with running it in one or several child processes.
# Write your code here:


# TODO 5-7: Pass data and names into processes
# Suggested piece: calculate_square(number) or another small pure function, plus custom process names.
# Make the target signatures visible so learners can see how arguments travel into child processes.
# Write your code here:


# TODO 8-12: Explore the lifecycle and control surface of a Process
# Include waiting with join(), checking alive state, inspecting exit status, terminating work, and using daemon processes.
# Focus on what each control tells you about a running or finished child process.
# Write your code here:


# TODO 13: Size parallel work using the available CPU count
# Suggested structure: query the machine capacity, then launch a matching set of independent workers.
# Write your code here:


# BONUS TODO: Add a long-running worker that can stop gracefully
# Contrast cooperative shutdown with forceful termination at a conceptual level.
# Write your code here:

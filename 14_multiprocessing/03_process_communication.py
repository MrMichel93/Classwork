"""
Mini-Program 3: Process Communication
Topic: Multiprocessing

Learning Objectives:
- Use Queue for inter-process communication
- Use Pipe for bidirectional communication
- Share data between processes safely
- Implement producer-consumer pattern with processes

Instructions:
Complete this program to learn about process communication.
"""

import multiprocessing
import time

# TODO 1: Create a Queue for process communication
# Producer process puts items in the queue
# Consumer process gets items from the queue
# Hint: queue = multiprocessing.Queue()
# Write your code here:


# TODO 2: Create a producer function that:
# - Takes a queue as parameter
# - Puts 5 items into the queue
# - Puts None to signal completion
# Write your code here:


# TODO 3: Create a consumer function that:
# - Takes a queue as parameter
# - Gets items from queue until it receives None
# - Processes each item (print it)
# Write your code here:


# TODO 4: Create and run producer and consumer processes
# Create a queue
# Create producer process with the queue
# Create consumer process with the queue
# Start both and wait for completion
# Write your code here:


# TODO 5: Create multiple producers and consumers
# 2 producers adding items to the same queue
# 2 consumers processing items from the same queue
# Write your code here:


# TODO 6: Use Pipe for two-way communication
# Create a pipe: parent_conn, child_conn = multiprocessing.Pipe()
# Parent sends data through parent_conn
# Child receives and responds through child_conn
# Write your code here:


# TODO 7: Create a function that communicates through a pipe
# Receives a message, processes it, sends response
# Write your code here:


# TODO 8: Create a process that uses the pipe
# Send a message from parent to child
# Receive and print the response
# Write your code here:


# TODO 9: Use Queue.qsize() to check queue size
# Note: qsize() is not reliable on all platforms
# Use it to monitor queue status
# Write your code here:


# TODO 10: Implement a task queue pattern
# Main process adds tasks to queue
# Worker processes pull tasks and execute them
# Write your code here:


# TODO 11: Use Queue.empty() and Queue.full()
# Check if queue is empty before getting
# Create a bounded queue with maxsize
# Write your code here:


# TODO 12: Pass complex objects through Queue
# Create a class and pass instances through the queue
# Objects must be picklable
# Write your code here:


# TODO 13: Handle Queue.Empty and Queue.Full exceptions
# Use queue.get(timeout=1) to avoid blocking forever
# Use queue.put(timeout=1) for bounded queues
# Write your code here:


# BONUS TODO: Implement a parallel web scraper
# Main process adds URLs to a queue
# Worker processes fetch URLs and put results in result queue
# Main process collects and saves results
# Write your code here:


"""
Mini-Program 4: Thread Communication
Topic: Threading

Learning Objectives:
- Use Events for thread signaling
- Implement producer-consumer with Queue
- Use Condition variables for complex synchronization
- Create threads that communicate with each other

Instructions:
Complete this program to learn about thread communication.
"""

import threading
import time
from queue import Queue

# TODO 1: Create an Event for simple signaling
# One thread waits for the event
# Another thread sets the event after some work
# Hint: event = threading.Event()
#       event.wait() to wait, event.set() to signal
# Write your code here:


# TODO 2: Create a waiter function that waits for an event
# Create a setter function that sets the event after 2 seconds
# Run both in separate threads
# Write your code here:


# TODO 3: Use Event for coordinating multiple threads
# Create multiple threads that all wait for the same event
# One thread sets the event, all others proceed
# Write your code here:


# TODO 4: Implement a simple producer-consumer with Queue
# Producer: Adds items to the queue
# Consumer: Takes items from the queue
# Hint: queue = Queue()
#       queue.put(item), queue.get()
# Write your code here:


# TODO 5: Create a producer function that:
# - Produces 10 items
# - Puts each item in the queue
# - Sleeps briefly between items
# Write your code here:


# TODO 6: Create a consumer function that:
# - Continuously gets items from the queue
# - Processes each item
# - Stops when it gets a special "STOP" signal
# Write your code here:


# TODO 7: Run one producer and multiple consumers
# Start 3 consumer threads
# Start 1 producer thread
# See how work is distributed among consumers
# Write your code here:


# TODO 8: Use Queue.task_done() and Queue.join()
# Producer puts items and waits with queue.join()
# Consumer calls queue.task_done() after processing
# Write your code here:


# TODO 9: Create a priority queue for thread communication
# Use queue.PriorityQueue()
# Items with lower numbers have higher priority
# Write your code here:


# TODO 10: Use Condition variable for complex signaling
# Create a condition: condition = threading.Condition()
# One thread waits for a condition
# Another thread notifies when condition is met
# Write your code here:


# TODO 11: Implement a bounded buffer with Condition
# Buffer has maximum size
# Producer waits if buffer is full
# Consumer waits if buffer is empty
# Write your code here:


# TODO 12: Use Condition.notify_all() vs Condition.notify()
# notify() wakes one waiting thread
# notify_all() wakes all waiting threads
# Demonstrate the difference
# Write your code here:


# TODO 13: Create a barrier for thread synchronization
# Use threading.Barrier(n)
# n threads must reach the barrier before any can proceed
# Write your code here:


# BONUS TODO: Implement a thread pool with communication
# Workers wait for tasks in a queue
# Main thread submits tasks and collects results
# Use Queue for bidirectional communication
# Write your code here:


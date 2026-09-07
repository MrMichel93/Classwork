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

# TODO 1-3: Use events for one-to-one and one-to-many signaling
# Suggested piece: waiter(event) or another clearly named listener function.
# Focus on how threads coordinate around a shared signal rather than on the exact print sequence.
# Write your code here:


# TODO 4-8: Build a queue-based producer/consumer workflow
# Suggested pieces: producer(queue, ...) and consumer(queue, ...), with at least one example using task completion tracking.
# Emphasize ownership of work items, completion acknowledgement, and scaling from one producer to many consumers.
# Write your code here:


# TODO 9-12: Compare richer communication primitives
# Include a priority-based queue example and one or more Condition-based coordination scenarios such as a bounded buffer.
# Highlight what extra control these primitives provide compared with a basic queue or event.
# Write your code here:


# TODO 13: Coordinate a fixed group with a barrier
# Make the structure visible by naming the participant function and the shared synchronization point.
# Write your code here:


# BONUS TODO: Combine communication patterns into a simple thread pool
# Show how tasks enter the system, how workers receive them, and how completion is signaled back.
# Write your code here:

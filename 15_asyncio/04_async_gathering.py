"""
Mini-Program 4: Async Gathering and Coordination
Topic: Asyncio

Learning Objectives:
- Use asyncio.gather() for concurrent execution
- Handle exceptions in gather()
- Use return_exceptions parameter
- Coordinate multiple async operations

Instructions:
Complete this program to learn about async gathering and coordination.
"""

import asyncio
import random

# TODO 1-2: Gather several independent async operations at once
# Suggested pieces: fetch_weather(), fetch_news(), and fetch_stocks().
# Make the individual coroutine signatures visible, then show how one await point can collect all of their results.
# Write your code here:


# TODO 3-5: Explore how gather behaves when some coroutines fail
# Use one task that can raise and compare default gather behavior with return_exceptions-style collection.
# Focus on what the caller receives back in each case.
# Write your code here:


# TODO 6-10: Compare several result-collection strategies
# Include mixed result types, argument unpacking, a scatter-gather pattern, a gather-versus-wait comparison, and a timeout-aware example.
# Emphasize the orchestration differences rather than the exact helper code.
# Write your code here:


# TODO 11-14: Process many coroutines with richer completion logic
# Cover fan-out/fan-in, nested coroutine gathering, handling results as they complete, and partial-failure recovery.
# Show the stage or helper names you choose so the flow is easy to follow.
# Write your code here:


# BONUS TODO: Create an async aggregator
# Focus on collecting results from multiple sources and combining them into one structured outcome.
# Write your code here:

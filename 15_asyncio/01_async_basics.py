"""
Mini-Program 1: Asyncio Basics
Topic: Asyncio

Learning Objectives:
- Understand asynchronous programming concepts
- Create coroutines using async/await syntax
- Run coroutines with asyncio.run()
- Understand the event loop

Instructions:
Complete this program to learn the basics of asyncio.
"""

import asyncio
import time

# TODO 1-4: Create and run your first coroutines
# Suggested pieces: async def say_hello() and async def fetch_data() -> str.
# Show both a coroutine that mainly waits and one that returns a value when awaited.
# Write your code here:


# TODO 5-6: Reuse one async function with different inputs
# Suggested piece: async def greet(name: str) -> None.
# Keep the calls sequential so learners can notice the accumulated waiting time.
# Write your code here:


# TODO 7-9: Contrast blocking sleep, non-blocking sleep, and un-awaited coroutines
# Suggested piece: async def count(name: str) -> None.
# Focus on what the runtime expects from coroutine objects and why simply calling them is not enough.
# Write your code here:


# TODO 10-12: Use an async main function to show that awaiting one coroutine at a time is still sequential
# Measure a small sequence of awaited calls and make the timing visible.
# Emphasize that async syntax alone does not create concurrency.
# Write your code here:


# BONUS TODO: Build a short chain of coroutines
# Suggested shape: one async function awaiting a second, which awaits a third.
# Write your code here:

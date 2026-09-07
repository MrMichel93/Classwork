"""
Mini-Program 2: Async/Await Patterns
Topic: Asyncio

Learning Objectives:
- Master async/await syntax
- Run multiple coroutines concurrently
- Use asyncio.create_task() for concurrent execution
- Understand when to use await

Instructions:
Complete this program to learn async/await patterns.
"""

import asyncio
import time

# TODO 1-4: Compare sequential awaits with scheduled async tasks
# Suggested piece: async def fetch_user(user_id: int) -> str, plus a main coroutine that runs several fetches.
# Show the structure of both approaches so learners can contrast one-at-a-time waiting with overlapping work.
# Write your code here:


# TODO 5-8: Reuse a second coroutine to study composition and concurrency choices
# Suggested pieces: async def process_data(item) -> result and one coroutine that awaits another.
# Focus on what changes when work is merely awaited versus turned into independently running tasks.
# Write your code here:


# TODO 9-10: Inspect task results and simple async function shapes
# Include one example that reports task outcomes and one async function that returns immediately without additional awaits.
# Emphasize coroutine structure rather than complex logic.
# Write your code here:


# TODO 11-13: Contrast gather-based coordination, explicit tasks, and cancellation
# Use a small set of coroutines so the difference in orchestration style is easy to observe.
# Highlight what each pattern is better at expressing.
# Write your code here:


# BONUS TODO: Add a retrying async operation
# Suggested shape: an async function that may fail, plus a wrapper that retries and reports the final outcome.
# Write your code here:

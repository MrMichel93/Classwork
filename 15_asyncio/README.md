# Asyncio - Asynchronous Programming

## 📖 What is Asyncio?

**Asyncio** is Python's built-in library for writing asynchronous, concurrent code using the `async/await` syntax. It allows you to write code that handles many I/O operations concurrently without using threads or processes.

### Understanding Asyncio

- **Asynchronous** - Code that doesn't block while waiting for operations
- **Coroutine** - A function defined with `async def` that can be paused and resumed
- **Event loop** - The core of asyncio, manages and executes coroutines
- **await** - Keyword that pauses a coroutine until result is ready
- **Task** - A wrapped coroutine scheduled to run on the event loop
- **Single-threaded** - All coroutines run in one thread (cooperative multitasking)

### Why Use Asyncio?

✅ **Efficient I/O** - Handle thousands of concurrent connections  
✅ **No thread overhead** - Lighter than threads  
✅ **Readable code** - async/await is cleaner than callbacks  
✅ **Scalable** - Great for web servers, APIs, websockets  
✅ **Non-blocking** - Don't waste time waiting  

### When to Use Asyncio?

- **I/O-bound** operations (network requests, file I/O, database queries)
- **Many concurrent** connections (web servers, chat servers)
- **Real-time** applications (websockets, streaming)
- **APIs and microservices**

### When NOT to Use Asyncio?

❌ **CPU-bound tasks** - Use multiprocessing instead  
❌ **Blocking libraries** - Need async versions  
❌ **Simple scripts** - Adds complexity  
❌ **Legacy code** - Hard to convert  

## 🚀 Basic Async/Await

### Your First Coroutine

```python
import asyncio

# Define coroutine with async def
async def say_hello():
    print("Hello")
    await asyncio.sleep(1)  # Non-blocking sleep
    print("World")

# Run coroutine
asyncio.run(say_hello())
# Output:
# Hello
# (1 second pause)
# World
```

### Async Function vs Regular Function

```python
import asyncio
import time

# Regular function - blocking
def blocking_sleep():
    print("Blocking sleep start")
    time.sleep(2)  # Blocks entire program
    print("Blocking sleep end")
    return "Done"

# Async function - non-blocking
async def async_sleep():
    print("Async sleep start")
    await asyncio.sleep(2)  # Doesn't block other coroutines
    print("Async sleep end")
    return "Done"

# Regular function blocks
blocking_sleep()

# Async function needs event loop
asyncio.run(async_sleep())
```

### Awaiting Coroutines

```python
import asyncio

async def get_data():
    """Simulate fetching data"""
    print("Fetching data...")
    await asyncio.sleep(2)
    return {"name": "Alice", "age": 25}

async def process_data():
    """Process fetched data"""
    # await pauses until get_data() completes
    data = await get_data()
    print(f"Processed: {data}")
    return data

# Run the coroutine
asyncio.run(process_data())
```

## 🎯 Running Multiple Coroutines

### Sequential Execution

```python
import asyncio
import time

async def task(name, duration):
    print(f"{name} starting")
    await asyncio.sleep(duration)
    print(f"{name} finished")
    return f"{name} result"

async def sequential():
    """Run tasks one after another"""
    start = time.time()
    
    # Sequential - waits for each to finish
    result1 = await task("Task 1", 2)
    result2 = await task("Task 2", 2)
    result3 = await task("Task 3", 2)
    
    print(f"Total time: {time.time() - start:.2f}s")  # ~6 seconds
    return [result1, result2, result3]

asyncio.run(sequential())
```

### Concurrent Execution

```python
import asyncio
import time

async def task(name, duration):
    print(f"{name} starting")
    await asyncio.sleep(duration)
    print(f"{name} finished")
    return f"{name} result"

async def concurrent():
    """Run tasks concurrently"""
    start = time.time()
    
    # Concurrent - all run at the same time
    results = await asyncio.gather(
        task("Task 1", 2),
        task("Task 2", 2),
        task("Task 3", 2)
    )
    
    print(f"Total time: {time.time() - start:.2f}s")  # ~2 seconds
    return results

asyncio.run(concurrent())
```

## 📦 Creating Tasks

### What are Tasks?

Tasks wrap coroutines and schedule them to run on the event loop.

```python
import asyncio

async def my_coroutine(name):
    print(f"{name} starting")
    await asyncio.sleep(2)
    print(f"{name} finished")
    return f"{name} done"

async def main():
    # Create task (starts running immediately)
    task1 = asyncio.create_task(my_coroutine("Task 1"))
    task2 = asyncio.create_task(my_coroutine("Task 2"))
    
    # Do other work while tasks run
    print("Tasks are running in background")
    await asyncio.sleep(1)
    print("Still running...")
    
    # Wait for tasks to complete
    result1 = await task1
    result2 = await task2
    
    print(f"Results: {result1}, {result2}")

asyncio.run(main())
```

### Task Methods

```python
import asyncio

async def long_task():
    await asyncio.sleep(5)
    return "Completed"

async def main():
    # Create task
    task = asyncio.create_task(long_task())
    
    # Check if done
    print(f"Done: {task.done()}")  # False
    
    # Get task name
    print(f"Name: {task.get_name()}")
    
    # Cancel task
    task.cancel()
    
    try:
        await task
    except asyncio.CancelledError:
        print("Task was cancelled")

asyncio.run(main())
```

### Task Cancellation

```python
import asyncio

async def cancellable_task():
    try:
        print("Task starting")
        await asyncio.sleep(10)
        print("Task finished")
    except asyncio.CancelledError:
        print("Task was cancelled")
        raise  # Re-raise to mark as cancelled

async def main():
    # Create task
    task = asyncio.create_task(cancellable_task())
    
    # Let it run for 2 seconds
    await asyncio.sleep(2)
    
    # Cancel the task
    task.cancel()
    
    try:
        await task
    except asyncio.CancelledError:
        print("Main: Task cancelled")

asyncio.run(main())
```

## 🎭 asyncio.gather()

### Gather Multiple Coroutines

```python
import asyncio

async def fetch_data(data_id):
    """Simulate fetching data"""
    await asyncio.sleep(1)
    return f"Data {data_id}"

async def main():
    # Run multiple coroutines concurrently
    results = await asyncio.gather(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3),
        fetch_data(4),
        fetch_data(5)
    )
    
    print(results)
    # ['Data 1', 'Data 2', 'Data 3', 'Data 4', 'Data 5']

asyncio.run(main())
```

### Gather with Error Handling

```python
import asyncio

async def successful_task(n):
    await asyncio.sleep(1)
    return f"Success {n}"

async def failing_task():
    await asyncio.sleep(0.5)
    raise ValueError("Task failed!")

async def main():
    # By default, gather raises on first exception
    try:
        results = await asyncio.gather(
            successful_task(1),
            failing_task(),
            successful_task(2)
        )
    except ValueError as e:
        print(f"Error: {e}")
    
    # return_exceptions=True to get exceptions in results
    results = await asyncio.gather(
        successful_task(1),
        failing_task(),
        successful_task(2),
        return_exceptions=True
    )
    
    for result in results:
        if isinstance(result, Exception):
            print(f"Exception: {result}")
        else:
            print(f"Result: {result}")

asyncio.run(main())
```

### Gather vs TaskGroup

```python
import asyncio

async def task(n):
    await asyncio.sleep(1)
    return n * 2

async def with_gather():
    """Using gather (Python 3.7+)"""
    results = await asyncio.gather(
        task(1),
        task(2),
        task(3)
    )
    return results

async def with_taskgroup():
    """Using TaskGroup (Python 3.11+)"""
    async with asyncio.TaskGroup() as group:
        task1 = group.create_task(task(1))
        task2 = group.create_task(task(2))
        task3 = group.create_task(task(3))
    
    # Tasks completed when exiting context
    return [task1.result(), task2.result(), task3.result()]

# Run either version
asyncio.run(with_gather())
```

## ⏱️ Timeouts and Waiting

### Timeout with wait_for

```python
import asyncio

async def slow_operation():
    await asyncio.sleep(5)
    return "Done"

async def main():
    try:
        # Wait maximum 2 seconds
        result = await asyncio.wait_for(slow_operation(), timeout=2.0)
        print(result)
    except asyncio.TimeoutError:
        print("Operation timed out!")

asyncio.run(main())
```

### Wait for Multiple Tasks

```python
import asyncio

async def task(name, duration):
    await asyncio.sleep(duration)
    return f"{name} done"

async def main():
    # Create tasks
    task1 = asyncio.create_task(task("Task 1", 1))
    task2 = asyncio.create_task(task("Task 2", 2))
    task3 = asyncio.create_task(task("Task 3", 3))
    
    # Wait for first to complete
    done, pending = await asyncio.wait(
        [task1, task2, task3],
        return_when=asyncio.FIRST_COMPLETED
    )
    
    print(f"First completed: {done}")
    
    # Cancel remaining tasks
    for task in pending:
        task.cancel()

asyncio.run(main())
```

### as_completed()

```python
import asyncio

async def fetch_url(url, delay):
    """Simulate fetching URL"""
    await asyncio.sleep(delay)
    return f"Content from {url}"

async def main():
    urls = [
        ("url1.com", 3),
        ("url2.com", 1),
        ("url3.com", 2)
    ]
    
    # Create coroutines
    coroutines = [fetch_url(url, delay) for url, delay in urls]
    
    # Process results as they complete (not in order)
    for coro in asyncio.as_completed(coroutines):
        result = await coro
        print(result)
    # Output: url2.com (1s), url3.com (2s), url1.com (3s)

asyncio.run(main())
```

## 🔄 Async Context Managers

### Async with Statement

```python
import asyncio

class AsyncResource:
    async def __aenter__(self):
        print("Acquiring resource")
        await asyncio.sleep(1)
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Releasing resource")
        await asyncio.sleep(1)
    
    async def use(self):
        print("Using resource")

async def main():
    async with AsyncResource() as resource:
        await resource.use()
    print("Resource released")

asyncio.run(main())
```

## 🔁 Async Iterators

### Async for Loop

```python
import asyncio

class AsyncRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __aiter__(self):
        self.current = self.start
        return self
    
    async def __anext__(self):
        if self.current >= self.end:
            raise StopAsyncIteration
        
        await asyncio.sleep(0.5)  # Simulate async operation
        value = self.current
        self.current += 1
        return value

async def main():
    async for num in AsyncRange(1, 5):
        print(num)

asyncio.run(main())
```

## 🎯 Common Patterns

### Producer-Consumer

```python
import asyncio
import random

async def producer(queue, producer_id):
    """Produce items"""
    for i in range(5):
        item = f"P{producer_id}-Item{i}"
        await queue.put(item)
        print(f"Produced: {item}")
        await asyncio.sleep(random.uniform(0.1, 0.5))
    await queue.put(None)  # Signal completion

async def consumer(queue, consumer_id):
    """Consume items"""
    while True:
        item = await queue.get()
        if item is None:
            await queue.put(None)  # Re-queue for others
            break
        print(f"Consumer {consumer_id} consumed: {item}")
        await asyncio.sleep(random.uniform(0.5, 1.0))
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    
    # Create producers and consumers
    producers = [
        asyncio.create_task(producer(queue, i))
        for i in range(2)
    ]
    
    consumers = [
        asyncio.create_task(consumer(queue, i))
        for i in range(3)
    ]
    
    # Wait for producers
    await asyncio.gather(*producers)
    
    # Wait for queue to be empty
    await queue.join()
    
    # Wait for consumers
    await asyncio.gather(*consumers)

asyncio.run(main())
```

### Parallel API Calls

```python
import asyncio

async def fetch_api(api_name, delay):
    """Simulate API call"""
    print(f"Calling {api_name} API...")
    await asyncio.sleep(delay)
    return {"api": api_name, "status": "success"}

async def main():
    # Call multiple APIs concurrently
    results = await asyncio.gather(
        fetch_api("users", 1),
        fetch_api("posts", 2),
        fetch_api("comments", 1.5)
    )
    
    for result in results:
        print(result)

asyncio.run(main())
```

### Rate Limiting

```python
import asyncio
import time

class RateLimiter:
    def __init__(self, max_calls, period):
        self.max_calls = max_calls
        self.period = period
        self.calls = []
    
    async def __aenter__(self):
        while len(self.calls) >= self.max_calls:
            # Remove old calls outside period
            now = time.time()
            self.calls = [t for t in self.calls if now - t < self.period]
            
            if len(self.calls) >= self.max_calls:
                # Wait until oldest call expires
                sleep_time = self.period - (now - self.calls[0])
                await asyncio.sleep(sleep_time)
        
        self.calls.append(time.time())
        return self
    
    async def __aexit__(self, *args):
        pass

async def api_call(call_id, limiter):
    async with limiter:
        print(f"API call {call_id} at {time.time():.2f}")
        await asyncio.sleep(0.1)

async def main():
    # Max 3 calls per 2 seconds
    limiter = RateLimiter(max_calls=3, period=2)
    
    # Try to make 10 calls
    await asyncio.gather(*[
        api_call(i, limiter) for i in range(10)
    ])

asyncio.run(main())
```

## 🔧 Working with Blocking Code

### Running Blocking Code

```python
import asyncio
import time

def blocking_operation():
    """CPU-intensive or blocking I/O"""
    time.sleep(2)
    return "Blocking done"

async def main():
    # Don't do this - blocks event loop!
    # result = blocking_operation()
    
    # Do this - run in thread pool
    result = await asyncio.to_thread(blocking_operation)
    print(result)

asyncio.run(main())
```

### Run in Executor

```python
import asyncio
import concurrent.futures
import time

def cpu_bound_task(n):
    """CPU-intensive task"""
    total = 0
    for i in range(n):
        total += i ** 2
    return total

async def main():
    # Run in process pool for CPU-bound work
    loop = asyncio.get_event_loop()
    
    with concurrent.futures.ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(
            pool,
            cpu_bound_task,
            1_000_000
        )
    
    print(f"Result: {result}")

asyncio.run(main())
```

## 📚 Mini-Programs in This Folder

Apply these concepts in the following programs:

1. **01_async_basics.py** - Asyncio fundamentals
   - Define coroutines with async def
   - Use await keyword
   - Run coroutines with asyncio.run()
   - Understand event loop
   - Compare sync vs async execution
   - Handle basic async operations

2. **02_async_await.py** - Async/await patterns
   - Chain multiple coroutines
   - Run coroutines concurrently
   - Use asyncio.create_task()
   - Handle task results
   - Cancel tasks
   - Master async/await syntax

3. **03_async_tasks.py** - Managing async tasks
   - Create and manage tasks
   - Check task status
   - Cancel tasks with timeouts
   - Handle task exceptions
   - Use wait_for() for timeouts
   - Coordinate multiple tasks

4. **04_async_gathering.py** - Gathering results
   - Use asyncio.gather() for concurrent execution
   - Handle exceptions with return_exceptions
   - Process results as they complete
   - Use as_completed() for streaming results
   - Implement rate limiting
   - Build concurrent applications

## 💡 Quick Tips

✅ **Best Practices:**
- Use async/await for I/O-bound operations
- Create tasks with asyncio.create_task()
- Use asyncio.gather() for concurrent execution
- Handle timeouts with asyncio.wait_for()
- Use asyncio.Queue for producer-consumer
- Run blocking code with asyncio.to_thread()
- Always await coroutines

❌ **Common Mistakes:**
- Forgetting await (coroutine never runs)
- Using time.sleep() instead of asyncio.sleep()
- Running blocking code in event loop
- Not handling task cancellation
- Using async for CPU-bound tasks
- Creating too many concurrent tasks
- Mixing sync and async code incorrectly

## 🎓 Key Takeaways

1. **Asyncio** enables efficient I/O-bound concurrent programming
2. **async def** defines coroutines
3. **await** pauses coroutine until result is ready
4. **asyncio.run()** starts the event loop
5. **Tasks** wrap coroutines for concurrent execution
6. **asyncio.gather()** runs multiple coroutines concurrently
7. **asyncio.wait_for()** adds timeouts
8. Use **asyncio.Queue** for async communication
9. Run **blocking code** in threads/processes
10. Asyncio is **single-threaded** cooperative multitasking

# Concurrent and Parallel Programming

## 📖 What is Concurrent and Parallel Programming?

**Concurrent programming** allows multiple tasks to make progress without necessarily running at the same time. **Parallel programming** runs multiple tasks simultaneously on multiple CPU cores. Python provides several tools to write efficient concurrent and parallel code.

### Understanding Concurrency vs Parallelism

- **Concurrency** - Multiple tasks making progress (not necessarily at same time)
- **Parallelism** - Multiple tasks running simultaneously (at same time)
- **Threading** - Concurrent execution (good for I/O-bound tasks)
- **Multiprocessing** - Parallel execution (good for CPU-bound tasks)
- **Asyncio** - Cooperative multitasking (good for I/O-bound tasks)

### Why Use Concurrent/Parallel Programming?

✅ **Performance** - Do more work in less time  
✅ **Responsiveness** - Don't block while waiting for I/O  
✅ **Resource utilization** - Use all CPU cores  
✅ **Scalability** - Handle more requests simultaneously  
✅ **Efficiency** - Better use of waiting time  

### Concurrency Analogy

```
Concurrency: You're cooking alone, switching between tasks
- Chop vegetables
- Check oven
- Stir pot
- Check oven again
- One person, multiple tasks in progress

Parallelism: Multiple chefs cooking simultaneously
- Chef 1: Chops vegetables
- Chef 2: Manages oven
- Chef 3: Stirs pot
- Multiple people, multiple tasks at same time
```

## 🎯 The concurrent.futures Module

Python's `concurrent.futures` module provides a high-level interface for concurrent execution.

### ThreadPoolExecutor - For I/O-Bound Tasks

```python
from concurrent.futures import ThreadPoolExecutor
import time

def download_file(file_id):
    """Simulate downloading a file (I/O-bound)"""
    print(f"Starting download {file_id}")
    time.sleep(2)  # Simulate network delay
    print(f"Finished download {file_id}")
    return f"file_{file_id}.txt"

# Sequential execution - slow
start = time.time()
for i in range(5):
    download_file(i)
print(f"Sequential: {time.time() - start:.2f} seconds")  # ~10 seconds

# Concurrent execution with ThreadPoolExecutor - fast
start = time.time()
with ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(download_file, range(5))
    files = list(results)
print(f"Concurrent: {time.time() - start:.2f} seconds")  # ~2 seconds
```

### ProcessPoolExecutor - For CPU-Bound Tasks

```python
from concurrent.futures import ProcessPoolExecutor
import time

def calculate_square(n):
    """CPU-intensive calculation"""
    total = 0
    for i in range(n):
        total += i ** 2
    return total

numbers = [10_000_000] * 8

# Sequential execution - slow
start = time.time()
results = [calculate_square(n) for n in numbers]
print(f"Sequential: {time.time() - start:.2f} seconds")

# Parallel execution with ProcessPoolExecutor - fast
start = time.time()
with ProcessPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(calculate_square, numbers))
print(f"Parallel: {time.time() - start:.2f} seconds")
```

## 🔮 Future Objects

### What are Futures?

A **Future** represents a computation that may not have completed yet. It's a promise to provide a result later.

```python
from concurrent.futures import ThreadPoolExecutor
import time

def slow_task(n):
    """Simulate slow task"""
    time.sleep(2)
    return n * 2

# Submit tasks and get Future objects
with ThreadPoolExecutor(max_workers=3) as executor:
    # submit() returns a Future immediately
    future1 = executor.submit(slow_task, 5)
    future2 = executor.submit(slow_task, 10)
    future3 = executor.submit(slow_task, 15)
    
    # Futures returned immediately, tasks running in background
    print("Tasks submitted")
    
    # Get results (blocks until complete)
    result1 = future1.result()  # Wait for completion
    result2 = future2.result()
    result3 = future3.result()
    
    print(f"Results: {result1}, {result2}, {result3}")
```

### Checking Future Status

```python
from concurrent.futures import ThreadPoolExecutor
import time

def slow_task(n):
    time.sleep(n)
    return n * 2

with ThreadPoolExecutor() as executor:
    future = executor.submit(slow_task, 3)
    
    # Check if future is complete
    print(f"Running: {future.running()}")    # True
    print(f"Done: {future.done()}")          # False
    
    # Wait a bit
    time.sleep(1)
    print(f"Running: {future.running()}")    # True
    print(f"Done: {future.done()}")          # False
    
    # Wait for completion
    result = future.result()
    print(f"Running: {future.running()}")    # False
    print(f"Done: {future.done()}")          # True
    print(f"Result: {result}")
```

### Future with Timeout

```python
from concurrent.futures import ThreadPoolExecutor, TimeoutError
import time

def very_slow_task():
    time.sleep(5)
    return "Done"

with ThreadPoolExecutor() as executor:
    future = executor.submit(very_slow_task)
    
    try:
        # Wait maximum 2 seconds
        result = future.result(timeout=2)
    except TimeoutError:
        print("Task took too long!")
        future.cancel()  # Try to cancel
```

### Multiple Futures with as_completed

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import random

def task(task_id):
    """Task with random duration"""
    duration = random.uniform(1, 3)
    time.sleep(duration)
    return f"Task {task_id} completed in {duration:.2f}s"

with ThreadPoolExecutor(max_workers=5) as executor:
    # Submit multiple tasks
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Process results as they complete (not in submission order)
    for future in as_completed(futures):
        result = future.result()
        print(result)
```

## 🔄 Executor Methods

### submit() vs map()

```python
from concurrent.futures import ThreadPoolExecutor

def square(x):
    return x * x

with ThreadPoolExecutor(max_workers=4) as executor:
    # submit() - For individual tasks, returns Future
    future1 = executor.submit(square, 5)
    future2 = executor.submit(square, 10)
    result1 = future1.result()  # 25
    result2 = future2.result()  # 100
    
    # map() - For multiple inputs, returns results in order
    results = executor.map(square, [1, 2, 3, 4, 5])
    print(list(results))  # [1, 4, 9, 16, 25]
```

### Collecting Results

```python
from concurrent.futures import ThreadPoolExecutor
import time

def process_item(item):
    time.sleep(1)
    return item * 2

items = [1, 2, 3, 4, 5]

# Method 1: Using map() - results in order
with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(process_item, items))
    print(results)  # [2, 4, 6, 8, 10]

# Method 2: Using submit() and gathering results
with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(process_item, item) for item in items]
    results = [future.result() for future in futures]
    print(results)  # [2, 4, 6, 8, 10]
```

## ⚡ When to Use What?

### I/O-Bound vs CPU-Bound

```python
# I/O-Bound: Waiting for external resources (network, disk, database)
# Use: ThreadPoolExecutor or asyncio
def io_bound_task():
    # Reading files
    with open("large_file.txt") as f:
        data = f.read()
    
    # Network requests
    import requests
    response = requests.get("https://api.example.com")
    
    # Database queries
    result = database.query("SELECT * FROM users")

# CPU-Bound: Heavy computation
# Use: ProcessPoolExecutor
def cpu_bound_task():
    # Heavy math
    result = sum(i**2 for i in range(10_000_000))
    
    # Data processing
    large_list = [complex_calculation(x) for x in range(1_000_000)]
    
    # Image processing
    processed_image = apply_filters(image)
```

### ThreadPoolExecutor Use Cases

```python
from concurrent.futures import ThreadPoolExecutor
import requests

# Good for: Multiple network requests
def download_url(url):
    response = requests.get(url)
    return response.status_code

urls = [
    "https://www.python.org",
    "https://www.github.com",
    "https://www.stackoverflow.com"
]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(download_url, urls)
    print(list(results))

# Good for: Multiple file operations
def read_file(filename):
    with open(filename) as f:
        return len(f.read())

files = ["file1.txt", "file2.txt", "file3.txt"]
with ThreadPoolExecutor(max_workers=3) as executor:
    sizes = list(executor.map(read_file, files))
```

### ProcessPoolExecutor Use Cases

```python
from concurrent.futures import ProcessPoolExecutor

# Good for: CPU-intensive calculations
def calculate_prime_factors(n):
    """CPU-intensive task"""
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

numbers = [12345, 67890, 111111, 222222, 333333]
with ProcessPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(calculate_prime_factors, numbers))

# Good for: Data processing
def process_chunk(data_chunk):
    """Process large dataset chunk"""
    return [transform(item) for item in data_chunk]

data_chunks = [chunk1, chunk2, chunk3, chunk4]
with ProcessPoolExecutor(max_workers=4) as executor:
    processed = list(executor.map(process_chunk, data_chunks))
```

## 🎯 Error Handling

### Handling Exceptions in Futures

```python
from concurrent.futures import ThreadPoolExecutor
import random

def risky_task(task_id):
    """Task that might fail"""
    if random.random() < 0.5:
        raise ValueError(f"Task {task_id} failed!")
    return f"Task {task_id} succeeded"

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(risky_task, i) for i in range(5)]
    
    for future in futures:
        try:
            result = future.result()
            print(result)
        except ValueError as e:
            print(f"Error: {e}")
```

### Exception Propagation

```python
from concurrent.futures import ThreadPoolExecutor

def failing_task():
    raise RuntimeError("Something went wrong!")

with ThreadPoolExecutor() as executor:
    future = executor.submit(failing_task)
    
    # Exception is raised when calling result()
    try:
        result = future.result()
    except RuntimeError as e:
        print(f"Caught exception: {e}")
```

## 🔧 Context Managers and Cleanup

### Proper Resource Management

```python
from concurrent.futures import ThreadPoolExecutor

# With context manager (recommended)
with ThreadPoolExecutor(max_workers=4) as executor:
    # Tasks run here
    results = executor.map(some_function, items)
# Executor automatically shuts down here

# Without context manager (manual cleanup)
executor = ThreadPoolExecutor(max_workers=4)
try:
    results = executor.map(some_function, items)
finally:
    executor.shutdown(wait=True)  # Clean up
```

### Shutdown Options

```python
from concurrent.futures import ThreadPoolExecutor
import time

def task(n):
    time.sleep(n)
    return n

executor = ThreadPoolExecutor(max_workers=2)

# Submit tasks
future1 = executor.submit(task, 3)
future2 = executor.submit(task, 5)

# Shutdown options
executor.shutdown(wait=True)   # Wait for all tasks to complete (default)
# executor.shutdown(wait=False)  # Don't wait, return immediately

# Can't submit new tasks after shutdown
# executor.submit(task, 1)  # RuntimeError!
```

## 📊 Performance Patterns

### Optimal Worker Count

```python
import multiprocessing
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# For I/O-bound (ThreadPoolExecutor):
# More workers = better (up to a point)
optimal_threads = 2 * multiprocessing.cpu_count()

# For CPU-bound (ProcessPoolExecutor):
# Workers = CPU cores (or cpu_count - 1)
optimal_processes = multiprocessing.cpu_count()

# Examples
with ThreadPoolExecutor(max_workers=optimal_threads) as executor:
    # I/O-bound tasks
    pass

with ProcessPoolExecutor(max_workers=optimal_processes) as executor:
    # CPU-bound tasks
    pass
```

### Chunking Large Jobs

```python
from concurrent.futures import ProcessPoolExecutor

def process_items(items):
    """Process multiple items in one worker"""
    return [item * 2 for item in items]

# Instead of 1 million tasks (overhead!)
large_dataset = list(range(1_000_000))

# Create chunks (e.g., 10,000 chunks of 100 items each)
chunk_size = 1000
chunks = [large_dataset[i:i+chunk_size] 
          for i in range(0, len(large_dataset), chunk_size)]

# Process chunks in parallel
with ProcessPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(process_items, chunks))
    
# Flatten results
final_results = [item for chunk in results for item in chunk]
```

## 📚 Mini-Programs in This Folder

Apply these concepts in the following programs:

1. **01_concurrent_basics.py** - Introduction to concurrency
   - Understand concurrency vs parallelism
   - Use ThreadPoolExecutor for I/O-bound tasks
   - Use ProcessPoolExecutor for CPU-bound tasks
   - Compare sequential vs concurrent execution
   - Measure performance improvements
   - Choose appropriate executor type

2. **02_futures.py** - Working with Future objects
   - Submit tasks with executor.submit()
   - Get results from Future objects
   - Check Future status (running, done)
   - Handle timeouts with result(timeout)
   - Process results with as_completed()
   - Cancel futures when needed

3. **03_process_pool.py** - Parallel processing
   - Use ProcessPoolExecutor for CPU-bound work
   - Parallelize computations across cores
   - Use map() for multiple inputs
   - Handle large datasets efficiently
   - Understand process overhead
   - Measure parallel speedup

4. **04_thread_pool.py** - Thread pool patterns
   - Use ThreadPoolExecutor for I/O-bound work
   - Set optimal number of workers
   - Handle multiple concurrent requests
   - Manage thread pool lifecycle
   - Handle exceptions in threads
   - Use context managers properly

## 💡 Quick Tips

✅ **Best Practices:**
- Use ThreadPoolExecutor for I/O-bound tasks
- Use ProcessPoolExecutor for CPU-bound tasks
- Use context managers (`with` statement) for executors
- Set reasonable max_workers (don't overdo it)
- Handle exceptions from Future.result()
- Use map() for simple parallel operations
- Use submit() for more control

❌ **Common Mistakes:**
- Using threads for CPU-bound tasks (GIL limits parallelism)
- Using processes for I/O-bound tasks (unnecessary overhead)
- Too many workers (diminishing returns, overhead)
- Not handling exceptions from futures
- Forgetting to shutdown executors
- Not using context managers
- Ignoring task granularity (too fine = overhead)

## 🎓 Key Takeaways

1. **Concurrency** allows tasks to make progress together
2. **Parallelism** runs tasks simultaneously on multiple cores
3. **ThreadPoolExecutor** for I/O-bound tasks (network, files)
4. **ProcessPoolExecutor** for CPU-bound tasks (heavy computation)
5. **Futures** represent results that aren't ready yet
6. **submit()** for individual tasks, **map()** for batches
7. Use **context managers** for proper cleanup
8. Handle **exceptions** from Future.result()
9. Choose worker count based on task type
10. Concurrent/parallel programming **improves performance** significantly

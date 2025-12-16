# Multiprocessing

## 📖 What is Multiprocessing?

**Multiprocessing** runs code in separate processes, each with its own Python interpreter and memory space. This bypasses Python's Global Interpreter Lock (GIL) and enables true parallel execution on multiple CPU cores.

### Understanding Multiprocessing

- **Process** - A separate program with its own memory space
- **Parallel execution** - Multiple processes run simultaneously on different cores
- **No GIL** - Each process has its own Python interpreter (no GIL limitation)
- **Separate memory** - Processes don't share memory (must use IPC)
- **IPC** - Inter-Process Communication (pipes, queues, shared memory)
- **Heavyweight** - Processes have more overhead than threads

### Why Use Multiprocessing?

✅ **True parallelism** - Use all CPU cores simultaneously  
✅ **CPU-bound tasks** - Heavy computation benefits from parallelism  
✅ **No GIL** - Each process has its own GIL  
✅ **Isolation** - Crash in one process doesn't affect others  
✅ **Security** - Processes can't access each other's memory  

### When to Use Multiprocessing?

- **CPU-intensive** calculations (math, data processing, image processing)
- **Parallel algorithms** (map-reduce, parallel sorting)
- **Independent tasks** (batch processing, simulations)
- **Isolating** unstable code

### When NOT to Use Multiprocessing?

❌ **I/O-bound tasks** - Use threading or asyncio instead  
❌ **Shared state** - Hard to share data between processes  
❌ **Quick tasks** - Process creation overhead not worth it  
❌ **Windows** - Some features work differently on Windows  

## 🚀 Creating and Starting Processes

### Basic Process Creation

```python
import multiprocessing
import time
import os

def worker(name):
    """Simple worker function"""
    print(f"{name} starting (PID: {os.getpid()})")
    time.sleep(2)
    print(f"{name} finished")

if __name__ == '__main__':
    # Main process
    print(f"Main process PID: {os.getpid()}")
    
    # Create process
    process = multiprocessing.Process(target=worker, args=("Worker-1",))
    
    # Start process
    process.start()
    
    # Wait for process to complete
    process.join()
    
    print("Main process finished")
```

### Multiple Processes

```python
import multiprocessing
import time

def task(task_id):
    print(f"Task {task_id} starting")
    time.sleep(2)
    print(f"Task {task_id} finished")

if __name__ == '__main__':
    # Create multiple processes
    processes = []
    for i in range(4):
        process = multiprocessing.Process(target=task, args=(i,))
        processes.append(process)
        process.start()
    
    # Wait for all processes
    for process in processes:
        process.join()
    
    print("All processes completed")
```

### Process with Return Values

```python
import multiprocessing

def calculate_square(n):
    """Calculate square of number"""
    return n * n

if __name__ == '__main__':
    # Processes can't return values directly
    # Use Queue or Pipe instead
    
    queue = multiprocessing.Queue()
    
    def worker(n, q):
        result = calculate_square(n)
        q.put(result)
    
    process = multiprocessing.Process(target=worker, args=(5, queue))
    process.start()
    process.join()
    
    result = queue.get()
    print(f"Result: {result}")  # 25
```

## 🏊 Process Pools

### Using Pool

```python
import multiprocessing
import time

def calculate_square(n):
    """CPU-intensive calculation"""
    time.sleep(1)
    return n * n

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    
    # Create pool with 4 worker processes
    with multiprocessing.Pool(processes=4) as pool:
        # Map function to inputs
        results = pool.map(calculate_square, numbers)
    
    print(f"Results: {results}")
    # [1, 4, 9, 16, 25, 36, 49, 64]
```

### Pool Methods

```python
import multiprocessing

def square(n):
    return n * n

def cube(n):
    return n * n * n

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    
    with multiprocessing.Pool(processes=4) as pool:
        # map() - Process all inputs, return results in order
        squares = pool.map(square, numbers)
        print(f"Squares: {squares}")
        
        # apply() - Process single input
        result = pool.apply(square, (5,))
        print(f"Single result: {result}")
        
        # apply_async() - Non-blocking single input
        async_result = pool.apply_async(square, (10,))
        print(f"Async result: {async_result.get()}")
        
        # map_async() - Non-blocking map
        async_results = pool.map_async(cube, numbers)
        print(f"Cubes: {async_results.get()}")
        
        # starmap() - For functions with multiple arguments
        pairs = [(1, 2), (3, 4), (5, 6)]
        sums = pool.starmap(lambda a, b: a + b, pairs)
        print(f"Sums: {sums}")
```

### Pool with Timeout

```python
import multiprocessing
import time

def slow_task(n):
    time.sleep(n)
    return n * 2

if __name__ == '__main__':
    with multiprocessing.Pool(processes=2) as pool:
        # Start task
        result = pool.apply_async(slow_task, (5,))
        
        try:
            # Wait maximum 2 seconds
            output = result.get(timeout=2)
            print(f"Result: {output}")
        except multiprocessing.TimeoutError:
            print("Task took too long!")
```

## 📨 Inter-Process Communication (IPC)

### Queue

```python
import multiprocessing
import time

def producer(queue):
    """Put items in queue"""
    for i in range(5):
        print(f"Producing {i}")
        queue.put(i)
        time.sleep(0.5)
    queue.put(None)  # Signal completion

def consumer(queue):
    """Get items from queue"""
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"Consuming {item}")
        time.sleep(1)

if __name__ == '__main__':
    # Create queue
    queue = multiprocessing.Queue()
    
    # Create processes
    prod = multiprocessing.Process(target=producer, args=(queue,))
    cons = multiprocessing.Process(target=consumer, args=(queue,))
    
    # Start processes
    prod.start()
    cons.start()
    
    # Wait for completion
    prod.join()
    cons.join()
```

### Pipe

```python
import multiprocessing

def sender(conn):
    """Send data through pipe"""
    messages = ["Hello", "World", "From", "Process"]
    for msg in messages:
        conn.send(msg)
    conn.close()

def receiver(conn):
    """Receive data through pipe"""
    while True:
        try:
            msg = conn.recv()
            print(f"Received: {msg}")
        except EOFError:
            break

if __name__ == '__main__':
    # Create pipe (returns two connection objects)
    parent_conn, child_conn = multiprocessing.Pipe()
    
    # Create processes
    sender_proc = multiprocessing.Process(target=sender, args=(child_conn,))
    receiver_proc = multiprocessing.Process(target=receiver, args=(parent_conn,))
    
    # Start processes
    sender_proc.start()
    receiver_proc.start()
    
    # Wait for completion
    sender_proc.join()
    receiver_proc.join()
```

### Bidirectional Pipe Communication

```python
import multiprocessing

def process_worker(conn):
    """Worker that sends and receives"""
    # Receive request
    request = conn.recv()
    print(f"Worker received: {request}")
    
    # Process and send response
    response = f"Processed: {request.upper()}"
    conn.send(response)
    conn.close()

if __name__ == '__main__':
    # Create bidirectional pipe
    parent_conn, child_conn = multiprocessing.Pipe()
    
    # Create and start process
    process = multiprocessing.Process(target=process_worker, args=(child_conn,))
    process.start()
    
    # Send request
    parent_conn.send("hello world")
    
    # Receive response
    response = parent_conn.recv()
    print(f"Main received: {response}")
    
    process.join()
```

## 💾 Shared Memory

### Value and Array

```python
import multiprocessing
import time

def increment_counter(counter, array):
    """Increment shared counter and modify array"""
    for i in range(5):
        with counter.get_lock():  # Lock for thread-safe access
            counter.value += 1
        
        array[i] = counter.value

if __name__ == '__main__':
    # Shared value (single value)
    counter = multiprocessing.Value('i', 0)  # 'i' = integer
    
    # Shared array (fixed size)
    array = multiprocessing.Array('i', 5)  # Array of 5 integers
    
    # Create processes
    processes = []
    for _ in range(3):
        p = multiprocessing.Process(target=increment_counter, args=(counter, array))
        processes.append(p)
        p.start()
    
    # Wait for all
    for p in processes:
        p.join()
    
    print(f"Final counter: {counter.value}")
    print(f"Array: {list(array)}") 
```

### Shared Memory Types

```python
import multiprocessing

if __name__ == '__main__':
    # Different types for Value and Array
    # 'i' - signed integer
    # 'd' - double (float)
    # 'c' - char
    
    shared_int = multiprocessing.Value('i', 10)
    shared_float = multiprocessing.Value('d', 3.14)
    shared_char = multiprocessing.Value('c', b'A')
    
    int_array = multiprocessing.Array('i', [1, 2, 3, 4, 5])
    float_array = multiprocessing.Array('d', [1.1, 2.2, 3.3])
    
    print(f"Integer: {shared_int.value}")
    print(f"Float: {shared_float.value}")
    print(f"Char: {shared_char.value}")
    print(f"Int array: {list(int_array)}")
    print(f"Float array: {list(float_array)}")
```

### Manager Objects

```python
import multiprocessing

def modify_dict(shared_dict, key, value):
    """Modify shared dictionary"""
    shared_dict[key] = value
    print(f"Added {key}: {value}")

def modify_list(shared_list, item):
    """Modify shared list"""
    shared_list.append(item)
    print(f"Added {item}")

if __name__ == '__main__':
    # Manager allows sharing complex objects
    manager = multiprocessing.Manager()
    
    # Shared dictionary
    shared_dict = manager.dict()
    
    # Shared list
    shared_list = manager.list()
    
    # Create processes
    processes = []
    
    # Dictionary processes
    for i in range(3):
        p = multiprocessing.Process(
            target=modify_dict, 
            args=(shared_dict, f"key{i}", i)
        )
        processes.append(p)
        p.start()
    
    # List processes
    for i in range(3):
        p = multiprocessing.Process(
            target=modify_list,
            args=(shared_list, i)
        )
        processes.append(p)
        p.start()
    
    # Wait for all
    for p in processes:
        p.join()
    
    print(f"Final dict: {dict(shared_dict)}")
    print(f"Final list: {list(shared_list)}")
```

## 🔒 Process Synchronization

### Lock

```python
import multiprocessing
import time

def write_to_file(lock, filename, process_id):
    """Write to file with lock"""
    for i in range(3):
        with lock:
            with open(filename, 'a') as f:
                f.write(f"Process {process_id}: Message {i}\n")
                print(f"Process {process_id} wrote message {i}")
        time.sleep(0.1)

if __name__ == '__main__':
    lock = multiprocessing.Lock()
    filename = "output.txt"
    
    # Clear file
    open(filename, 'w').close()
    
    # Create processes
    processes = []
    for i in range(3):
        p = multiprocessing.Process(
            target=write_to_file,
            args=(lock, filename, i)
        )
        processes.append(p)
        p.start()
    
    # Wait for all
    for p in processes:
        p.join()
    
    # Read file
    with open(filename, 'r') as f:
        print("\nFile contents:")
        print(f.read())
```

### Semaphore

```python
import multiprocessing
import time

def access_resource(semaphore, process_id):
    """Limited concurrent access"""
    print(f"Process {process_id} waiting")
    with semaphore:
        print(f"Process {process_id} accessing resource")
        time.sleep(2)
        print(f"Process {process_id} releasing resource")

if __name__ == '__main__':
    # Allow only 2 processes at a time
    semaphore = multiprocessing.Semaphore(2)
    
    # Create 5 processes
    processes = []
    for i in range(5):
        p = multiprocessing.Process(
            target=access_resource,
            args=(semaphore, i)
        )
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
```

## 🎯 Process Patterns

### Map-Reduce Pattern

```python
import multiprocessing

def mapper(data_chunk):
    """Map phase - process chunk of data"""
    return [x * 2 for x in data_chunk]

def reducer(results):
    """Reduce phase - combine results"""
    return sum(sum(chunk) for chunk in results)

if __name__ == '__main__':
    # Large dataset
    data = list(range(1000))
    
    # Split into chunks
    chunk_size = 100
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
    
    # Map phase
    with multiprocessing.Pool(processes=4) as pool:
        mapped_results = pool.map(mapper, chunks)
    
    # Reduce phase
    final_result = reducer(mapped_results)
    print(f"Final result: {final_result}")
```

### Producer-Consumer with Multiprocessing

```python
import multiprocessing
import time
import random

def producer(queue, producer_id):
    """Produce items"""
    for i in range(5):
        item = f"P{producer_id}-Item{i}"
        queue.put(item)
        print(f"Producer {producer_id} produced {item}")
        time.sleep(random.uniform(0.1, 0.5))
    queue.put(None)  # Signal completion

def consumer(queue, consumer_id):
    """Consume items"""
    while True:
        item = queue.get()
        if item is None:
            queue.put(None)  # Re-queue for other consumers
            break
        print(f"Consumer {consumer_id} consuming {item}")
        time.sleep(random.uniform(0.5, 1.0))

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    
    # Create producers
    producers = []
    for i in range(2):
        p = multiprocessing.Process(target=producer, args=(queue, i))
        producers.append(p)
        p.start()
    
    # Create consumers
    consumers = []
    for i in range(3):
        p = multiprocessing.Process(target=consumer, args=(queue, i))
        consumers.append(p)
        p.start()
    
    # Wait for all
    for p in producers:
        p.join()
    for p in consumers:
        p.join()
```

## 🔍 Process Information

### Getting Process Info

```python
import multiprocessing
import os
import time

def worker(name):
    """Display process info"""
    current = multiprocessing.current_process()
    print(f"Process name: {current.name}")
    print(f"Process PID: {current.pid}")
    print(f"Parent PID: {os.getppid()}")
    print(f"Is alive: {current.is_alive()}")
    time.sleep(1)

if __name__ == '__main__':
    # Main process info
    print(f"Main PID: {os.getpid()}")
    print(f"CPU count: {multiprocessing.cpu_count()}")
    
    # Create and start process
    p = multiprocessing.Process(target=worker, args=("Worker",), name="MyWorker")
    print(f"Before start - alive: {p.is_alive()}")
    
    p.start()
    print(f"After start - alive: {p.is_alive()}")
    
    p.join()
    print(f"After join - alive: {p.is_alive()}")
    print(f"Exit code: {p.exitcode}")
```

## ⚠️ Important Considerations

### The if __name__ == '__main__' Guard

```python
import multiprocessing

def worker():
    print("Worker process")

# ALWAYS use this guard with multiprocessing
if __name__ == '__main__':
    # This code only runs when script is executed directly
    # Not when imported or when child processes are created
    p = multiprocessing.Process(target=worker)
    p.start()
    p.join()

# Without the guard on Windows:
# - Child processes will re-import the module
# - Creates infinite process loop
# - Program crashes
```

### Pickling Limitations

```python
import multiprocessing

# Functions must be picklable (serializable)
# ✅ Module-level functions work
def good_function(x):
    return x * 2

# ❌ Lambda functions don't work (can't be pickled)
# bad = lambda x: x * 2

# ❌ Nested functions don't work
def outer():
    def inner(x):
        return x * 2
    return inner

if __name__ == '__main__':
    with multiprocessing.Pool() as pool:
        # Works
        results = pool.map(good_function, [1, 2, 3])
        
        # Doesn't work (PicklingError)
        # results = pool.map(lambda x: x * 2, [1, 2, 3])
```

## 📚 Mini-Programs in This Folder

Apply these concepts in the following programs:

1. **01_process_basics.py** - Multiprocessing fundamentals
   - Create processes with multiprocessing.Process
   - Start processes with start()
   - Wait for processes with join()
   - Pass arguments to processes
   - Get process information (PID, name)
   - Understand process vs thread differences

2. **02_process_pool.py** - Process pools
   - Use multiprocessing.Pool for parallel execution
   - Apply map() to parallelize work
   - Use apply() and apply_async()
   - Handle results from multiple processes
   - Set optimal pool size
   - Compare performance with sequential execution

3. **03_process_communication.py** - Inter-process communication
   - Use Queue for process communication
   - Use Pipe for bidirectional communication
   - Implement producer-consumer pattern
   - Pass data between processes
   - Handle process synchronization
   - Avoid deadlocks in IPC

4. **04_shared_memory.py** - Shared memory
   - Use Value for shared single values
   - Use Array for shared arrays
   - Use Manager for complex shared objects
   - Synchronize access with locks
   - Share dictionaries and lists
   - Handle concurrent modifications

## 💡 Quick Tips

✅ **Best Practices:**
- Always use `if __name__ == '__main__'` guard
- Use Pool for CPU-bound parallel tasks
- Use Queue or Pipe for IPC
- Lock shared resources
- Set appropriate pool size (usually cpu_count())
- Handle exceptions in worker processes
- Clean up resources properly

❌ **Common Mistakes:**
- Forgetting `if __name__ == '__main__'` (breaks on Windows)
- Using lambdas or nested functions (can't pickle)
- Not joining processes (zombies)
- Sharing mutable objects without locks
- Using processes for I/O-bound tasks (use threads)
- Creating too many processes (overhead)
- Not handling process exceptions

## 🎓 Key Takeaways

1. **Multiprocessing** enables true parallel execution
2. Each **process** has its own memory and GIL
3. Use for **CPU-bound** tasks, not I/O-bound
4. **Pool** simplifies parallel processing
5. **Queue** and **Pipe** enable IPC
6. **Shared memory** requires synchronization
7. **Manager** allows sharing complex objects
8. Always use `if __name__ == '__main__'` guard
9. Process creation has **overhead**
10. Multiprocessing scales with CPU cores

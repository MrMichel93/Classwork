# Threading

## 📖 What is Threading?

**Threading** allows a program to run multiple operations concurrently within a single process. Threads share the same memory space and are lightweight, making them ideal for I/O-bound tasks.

### Understanding Threads

- **Thread** - A separate flow of execution within a program
- **Main thread** - The primary thread that starts when program runs
- **Worker threads** - Additional threads created to perform tasks
- **Concurrent** - Threads make progress together (not necessarily simultaneously)
- **Shared memory** - All threads share the same variables and objects
- **GIL (Global Interpreter Lock)** - Python's lock that limits parallel execution

### Why Use Threading?

✅ **I/O operations** - Don't wait for network/disk operations  
✅ **Responsiveness** - Keep GUI responsive during long operations  
✅ **Concurrent downloads** - Download multiple files at once  
✅ **Lightweight** - Threads are lighter than processes  
✅ **Shared memory** - Easy data sharing between threads  

### When NOT to Use Threading

❌ **CPU-bound tasks** - GIL prevents true parallelism (use multiprocessing)  
❌ **Simple sequential code** - Threading adds complexity  
❌ **Short-running tasks** - Thread overhead not worth it  

## 🚀 Creating and Starting Threads

### Basic Thread Creation

```python
import threading
import time

def worker(name, duration):
    """Simple worker function"""
    print(f"{name} starting")
    time.sleep(duration)
    print(f"{name} finished")

# Create thread
thread1 = threading.Thread(target=worker, args=("Thread-1", 2))

# Start thread
thread1.start()

# Main thread continues
print("Main thread continuing")

# Wait for thread to complete
thread1.join()
print("All done")
```

### Multiple Threads

```python
import threading
import time

def task(task_id):
    print(f"Task {task_id} starting")
    time.sleep(2)
    print(f"Task {task_id} finished")

# Create multiple threads
threads = []
for i in range(5):
    thread = threading.Thread(target=task, args=(i,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All tasks completed")
```

### Thread with Keyword Arguments

```python
import threading

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Using args tuple
thread1 = threading.Thread(target=greet, args=("Alice",))

# Using kwargs dictionary
thread2 = threading.Thread(
    target=greet, 
    kwargs={"name": "Bob", "greeting": "Hi"}
)

thread1.start()
thread2.start()
thread1.join()
thread2.join()
```

## 🎯 Thread Objects and Methods

### Thread Attributes

```python
import threading
import time

def worker():
    print(f"Worker thread: {threading.current_thread().name}")
    time.sleep(2)

# Create thread with custom name
thread = threading.Thread(target=worker, name="MyWorker")

# Thread attributes
print(f"Thread name: {thread.name}")
print(f"Thread alive: {thread.is_alive()}")  # False (not started)
print(f"Thread daemon: {thread.daemon}")     # False

# Start thread
thread.start()
print(f"Thread alive: {thread.is_alive()}")  # True

# Wait for completion
thread.join()
print(f"Thread alive: {thread.is_alive()}")  # False
```

### Getting Current Thread

```python
import threading
import time

def worker():
    current = threading.current_thread()
    print(f"Thread name: {current.name}")
    print(f"Thread ID: {current.ident}")
    time.sleep(1)

# Main thread info
main_thread = threading.current_thread()
print(f"Main thread: {main_thread.name}")

# Worker thread
thread = threading.Thread(target=worker, name="Worker-1")
thread.start()
thread.join()

# Count active threads
print(f"Active threads: {threading.active_count()}")
```

### Daemon Threads

```python
import threading
import time

def daemon_worker():
    """Daemon thread - stops when main program exits"""
    while True:
        print("Daemon working...")
        time.sleep(1)

def normal_worker():
    """Normal thread - program waits for it to finish"""
    for i in range(3):
        print(f"Normal working {i}")
        time.sleep(1)

# Daemon thread
daemon = threading.Thread(target=daemon_worker, daemon=True)
daemon.start()

# Normal thread
normal = threading.Thread(target=normal_worker)
normal.start()

normal.join()  # Wait for normal thread
# Daemon thread is killed when main exits (no join needed)
print("Main exiting (daemon thread will be killed)")
```

## 🔒 Thread Synchronization

### The Race Condition Problem

```python
import threading

# Shared variable - DANGEROUS without synchronization!
counter = 0

def increment():
    """Increment counter 100,000 times"""
    global counter
    for _ in range(100000):
        counter += 1  # NOT thread-safe!

# Create multiple threads
threads = []
for _ in range(10):
    thread = threading.Thread(target=increment)
    threads.append(thread)
    thread.start()

# Wait for all threads
for thread in threads:
    thread.join()

# Expected: 1,000,000 (10 threads × 100,000)
# Actual: Less than 1,000,000 (race condition!)
print(f"Counter: {counter}")
```

### Using Locks

```python
import threading

counter = 0
lock = threading.Lock()

def increment_safe():
    """Thread-safe increment using lock"""
    global counter
    for _ in range(100000):
        lock.acquire()
        try:
            counter += 1  # Protected by lock
        finally:
            lock.release()

# Better: Use with statement
def increment_better():
    global counter
    for _ in range(100000):
        with lock:  # Automatically acquires and releases
            counter += 1

# Run threads with locks
threads = []
for _ in range(10):
    thread = threading.Thread(target=increment_better)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Counter: {counter}")  # Now: 1,000,000 (correct!)
```

### Lock Patterns

```python
import threading

lock = threading.Lock()
data = []

def add_item(item):
    """Add item to shared list (thread-safe)"""
    with lock:
        data.append(item)
        print(f"Added {item}")

def process_items():
    """Process all items (thread-safe)"""
    with lock:
        items_copy = data.copy()  # Copy while holding lock
    
    # Process without holding lock (don't block other threads)
    for item in items_copy:
        print(f"Processing {item}")

# Create multiple threads
threads = []
for i in range(5):
    t = threading.Thread(target=add_item, args=(i,))
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()

process_items()
```

## 🔐 Advanced Locks

### RLock (Reentrant Lock)

```python
import threading

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.RLock()  # Reentrant lock
    
    def deposit(self, amount):
        with self.lock:
            self.balance += amount
    
    def withdraw(self, amount):
        with self.lock:
            self.balance -= amount
    
    def transfer_to(self, other_account, amount):
        """Can acquire lock multiple times (reentrant)"""
        with self.lock:  # Acquire lock
            self.withdraw(amount)  # acquire lock again (OK with RLock)
            other_account.deposit(amount)

account1 = BankAccount(1000)
account2 = BankAccount(500)

account1.transfer_to(account2, 200)
print(f"Account 1: {account1.balance}")  # 800
print(f"Account 2: {account2.balance}")  # 700
```

### Semaphore

```python
import threading
import time

# Limit to 3 concurrent threads
semaphore = threading.Semaphore(3)

def access_resource(thread_id):
    """Limited concurrent access"""
    print(f"Thread {thread_id} waiting for access")
    
    with semaphore:
        print(f"Thread {thread_id} accessing resource")
        time.sleep(2)  # Simulate work
        print(f"Thread {thread_id} releasing resource")

# Create 10 threads (but only 3 can run at a time)
threads = []
for i in range(10):
    thread = threading.Thread(target=access_resource, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
```

### Event

```python
import threading
import time

event = threading.Event()

def waiter(name):
    """Wait for event"""
    print(f"{name} waiting for event")
    event.wait()  # Block until event is set
    print(f"{name} received event!")

def setter():
    """Set event after delay"""
    print("Setter sleeping...")
    time.sleep(3)
    print("Setter setting event")
    event.set()  # Wake up all waiting threads

# Create waiting threads
for i in range(3):
    thread = threading.Thread(target=waiter, args=(f"Waiter-{i}",))
    thread.start()

# Create setter thread
setter_thread = threading.Thread(target=setter)
setter_thread.start()
```

## 📨 Thread Communication

### Using Queue

```python
import threading
import queue
import time

def producer(q, producer_id):
    """Produce items and put in queue"""
    for i in range(5):
        item = f"Item-{producer_id}-{i}"
        print(f"Producer {producer_id} producing {item}")
        q.put(item)
        time.sleep(0.5)
    q.put(None)  # Signal completion

def consumer(q, consumer_id):
    """Consume items from queue"""
    while True:
        item = q.get()  # Block until item available
        if item is None:
            q.task_done()
            break
        print(f"Consumer {consumer_id} consuming {item}")
        time.sleep(1)
        q.task_done()

# Create queue
work_queue = queue.Queue()

# Start producers
producers = []
for i in range(2):
    thread = threading.Thread(target=producer, args=(work_queue, i))
    producers.append(thread)
    thread.start()

# Start consumers
consumers = []
for i in range(3):
    thread = threading.Thread(target=consumer, args=(work_queue, i))
    consumers.append(thread)
    thread.start()

# Wait for producers
for thread in producers:
    thread.join()

# Signal consumers to stop
for _ in consumers:
    work_queue.put(None)

# Wait for consumers
for thread in consumers:
    thread.join()

work_queue.join()  # Wait for all tasks to be processed
```

### Condition Variables

```python
import threading
import time

condition = threading.Condition()
data = []

def producer():
    """Produce data and notify consumers"""
    for i in range(5):
        time.sleep(1)
        with condition:
            data.append(i)
            print(f"Produced: {i}")
            condition.notify()  # Wake up one waiting consumer

def consumer(consumer_id):
    """Wait for data and consume"""
    while True:
        with condition:
            while not data:  # Wait while no data
                condition.wait()
            
            item = data.pop(0)
            print(f"Consumer {consumer_id} consumed: {item}")
            
            if item >= 4:  # Stop after consuming 4
                break

# Start threads
producer_thread = threading.Thread(target=producer)
consumer_thread1 = threading.Thread(target=consumer, args=(1,))
consumer_thread2 = threading.Thread(target=consumer, args=(2,))

consumer_thread1.start()
consumer_thread2.start()
producer_thread.start()

producer_thread.join()
consumer_thread1.join()
consumer_thread2.join()
```

## 🎯 Thread Patterns

### Worker Pool Pattern

```python
import threading
import queue
import time

class WorkerPool:
    def __init__(self, num_workers):
        self.queue = queue.Queue()
        self.workers = []
        
        for _ in range(num_workers):
            worker = threading.Thread(target=self._worker)
            worker.daemon = True
            worker.start()
            self.workers.append(worker)
    
    def _worker(self):
        """Worker thread that processes tasks"""
        while True:
            task, args = self.queue.get()
            try:
                task(*args)
            finally:
                self.queue.task_done()
    
    def submit(self, task, *args):
        """Submit task to pool"""
        self.queue.put((task, args))
    
    def wait_completion(self):
        """Wait for all tasks to complete"""
        self.queue.join()

def process_item(item):
    print(f"Processing {item}")
    time.sleep(1)

# Create pool with 3 workers
pool = WorkerPool(3)

# Submit tasks
for i in range(10):
    pool.submit(process_item, i)

# Wait for completion
pool.wait_completion()
print("All tasks completed")
```

### Producer-Consumer Pattern

```python
import threading
import queue
import time
import random

def producer(queue, producer_id):
    """Generate items"""
    for i in range(5):
        item = f"P{producer_id}-Item{i}"
        queue.put(item)
        print(f"Producer {producer_id} produced {item}")
        time.sleep(random.uniform(0.1, 0.5))

def consumer(queue, consumer_id):
    """Process items"""
    while True:
        try:
            item = queue.get(timeout=2)
            print(f"Consumer {consumer_id} processing {item}")
            time.sleep(random.uniform(0.5, 1.0))
            queue.task_done()
        except queue.Empty:
            break

# Create queue
q = queue.Queue(maxsize=10)

# Start producers
producers = [
    threading.Thread(target=producer, args=(q, i))
    for i in range(2)
]
for p in producers:
    p.start()

# Start consumers
consumers = [
    threading.Thread(target=consumer, args=(q, i))
    for i in range(3)
]
for c in consumers:
    c.start()

# Wait for completion
for p in producers:
    p.join()
q.join()
for c in consumers:
    c.join()
```

## ⚠️ Common Threading Issues

### Deadlock

```python
import threading

lock1 = threading.Lock()
lock2 = threading.Lock()

def thread1_work():
    """Thread 1 acquires lock1 then lock2"""
    with lock1:
        print("Thread 1 has lock1")
        time.sleep(0.1)
        with lock2:
            print("Thread 1 has lock2")

def thread2_work():
    """Thread 2 acquires lock2 then lock1 - DEADLOCK!"""
    with lock2:
        print("Thread 2 has lock2")
        time.sleep(0.1)
        with lock1:  # Will wait forever!
            print("Thread 2 has lock1")

# This will deadlock!
# t1 = threading.Thread(target=thread1_work)
# t2 = threading.Thread(target=thread2_work)
# t1.start()
# t2.start()

# Solution: Always acquire locks in same order
```

## 📚 Mini-Programs in This Folder

Apply these concepts in the following programs:

1. **01_thread_basics.py** - Threading fundamentals
   - Create threads with threading.Thread
   - Start threads with start()
   - Wait for threads with join()
   - Pass arguments to threads
   - Use daemon threads
   - Get thread information

2. **02_thread_synchronization.py** - Synchronizing threads
   - Understand race conditions
   - Use Lock to prevent race conditions
   - Use with statement for locks
   - Protect shared data
   - Use RLock for reentrant locking
   - Apply proper synchronization patterns

3. **03_thread_locks.py** - Advanced locking
   - Use different lock types (Lock, RLock)
   - Use Semaphore for limited access
   - Implement timeouts for locks
   - Avoid deadlocks
   - Use context managers
   - Handle lock exceptions

4. **04_thread_communication.py** - Thread communication
   - Use Queue for thread-safe communication
   - Implement producer-consumer pattern
   - Use Event for signaling
   - Use Condition variables
   - Coordinate multiple threads
   - Handle thread completion

## 💡 Quick Tips

✅ **Best Practices:**
- Always use locks when sharing data between threads
- Use `with` statement for automatic lock release
- Keep critical sections small (minimize lock holding time)
- Avoid holding multiple locks when possible
- Use Queue for thread communication
- Set daemon=True for background threads
- Use join() to wait for thread completion

❌ **Common Mistakes:**
- Forgetting to use locks (race conditions!)
- Holding locks too long (blocks other threads)
- Acquiring locks in different orders (deadlock)
- Not joining threads (program exits early)
- Using threads for CPU-bound tasks (use multiprocessing)
- Sharing mutable objects without locks
- Not handling exceptions in threads

## 🎓 Key Takeaways

1. **Threads** allow concurrent execution in same process
2. **start()** begins thread execution, **join()** waits for completion
3. **Race conditions** occur when threads access shared data without locks
4. **Lock** provides mutual exclusion for shared resources
5. **RLock** allows thread to acquire same lock multiple times
6. **Semaphore** limits number of concurrent accesses
7. **Queue** provides thread-safe communication
8. **Event** signals between threads
9. Use threading for **I/O-bound** tasks, not CPU-bound
10. Always **synchronize** access to shared data

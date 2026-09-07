# Enrichment Challenge Catalog

Topics 11-15 are optional exploration after the AP CSP core. Choose one
challenge at a time, read its prerequisites, and set a timebox before coding.
These projects are not required for AP CSP proficiency.

## Choosing a Path

### Advanced High-School Path

Choose **one** challenge from the following list. Aim for a working program,
three deliberate test cases, and a short reflection on one design choice.

| Challenge | Prerequisites | Timebox | Deliverable |
|---|---|---:|---|
| Properties and validation | Classes, methods, conditionals | 1-2 periods | A class that rejects invalid state with clear error messages. |
| Magic methods | Classes and lists | 1-2 periods | A small `Vector`, `Book`, or `ShoppingCart` class with useful special methods. |
| Abstract classes | Inheritance and polymorphism | 1-2 periods | Two concrete subclasses that satisfy one abstract contract. |
| Futures | Functions and basic timing | 1-2 periods | A program that runs independent simulated tasks and handles a timeout. |
| Thread basics | Functions and lists | 1-2 periods | A program that starts, joins, and compares two independent I/O-like tasks. |
| Async basics | Functions and timing | 1-2 periods | Two coroutines that demonstrate sequential and concurrent waiting. |

### University Path

Choose a topic sequence, complete the listed introductory lessons first, then
select one capstone. Plan the program's data flow and error handling before
implementation.

| Sequence | Complete first | Then choose one capstone |
|---|---|---|
| Advanced OOP | Topic 11 lessons 01-04 | A descriptor, plugin registry, or serialization design. |
| Executor-based concurrency | Topic 12 lessons 01-04 | A bounded concurrent pipeline or performance comparison. |
| Threading | Topic 13 lessons 01-04 | A thread-safe worker pool with cooperative shutdown. |
| Multiprocessing | Topic 14 lessons 01-04 | A CPU-bound parallel algorithm with measured speedup. |
| Asyncio | Topic 15 lessons 01-04 | A bounded async queue, rate limiter, or resilient async client. |

## Topic 11: Advanced OOP

| Lesson | Challenge | Prerequisites | Timebox | Suggested evidence |
|---|---|---|---:|---|
| `11_advanced_oop/01_properties.py` | Validated and computed properties | Basic classes and methods | 1 period | Valid and invalid assignments with expected results. |
| `11_advanced_oop/02_class_methods_static.py` | Alternative constructors and utility methods | Classes and type conversion | 1 period | Objects created through each constructor. |
| `11_advanced_oop/03_magic_methods.py` | User-friendly custom objects | Classes, lists, comparisons | 1-2 periods | `str`, equality, and one arithmetic or container operation. |
| `11_advanced_oop/04_abstract_classes.py` | Shared contracts with subclasses | Inheritance and overriding | 1-2 periods | Two implementations used through the same base type. |
| `11_advanced_oop/05_metaclasses_descriptors.py` | Reusable validation descriptors | Properties and class attributes | 2-4 periods | A descriptor plus tests for valid and invalid values. |
| `11_advanced_oop/06_advanced_python_oop.py` | Python OOP patterns and mini-frameworks | All prior topic 11 lessons | 4+ periods | A scoped design document, tests, and one complete feature. |

Do not begin with descriptors, metaclasses, or framework tasks. They are
Python-specific enrichment, not prerequisites for learning OOP or preparing
for AP CSA.

## Topic 12: Concurrent and Parallel Programming

| Lesson | Challenge | Prerequisites | Timebox | Suggested evidence |
|---|---|---|---:|---|
| `12_concurrent_parallel/01_concurrent_basics.py` | Compare sequential and executor-based tasks | Functions and timing | 1 period | A timing comparison for simulated I/O work. |
| `12_concurrent_parallel/02_futures.py` | Futures, timeouts, and cancellation limits | Lesson 01 | 1-2 periods | Timeout handling and cooperative cancellation evidence. |
| `12_concurrent_parallel/03_process_pool.py` | CPU-bound process pool | Functions and performance measurement | 1-2 periods | Correct results and a speedup discussion. |
| `12_concurrent_parallel/04_thread_pool.py` | Bounded I/O-style worker pool | Lists, functions, exceptions | 1-2 periods | Results, errors, and a justified worker count. |
| `12_concurrent_parallel/05_advanced_concurrency.py` | Concurrent pipeline or priority queue | Futures and queues | 3-4 periods | Clean shutdown and error propagation. |
| `12_concurrent_parallel/06_parallel_algorithms.py` | Parallel algorithm study | Process pools and benchmarking | 4+ periods | Sequential baseline, parallel version, and measured tradeoffs. |

Use simulated tasks unless an assignment explicitly provides safe local data.
Do not make unbounded network requests or benchmark on shared school systems.

## Topic 13: Threading

| Lesson | Challenge | Prerequisites | Timebox | Suggested evidence |
|---|---|---|---:|---|
| `13_threading/01_thread_basics.py` | Creating and joining threads | Functions | 1 period | Correctly joined threads and understandable output. |
| `13_threading/02_thread_synchronization.py` | Race condition and lock repair | Shared state and conditionals | 1-2 periods | A reproducible race plus a lock-protected version. |
| `13_threading/03_thread_locks.py` | Locks, RLocks, and deadlock prevention | Lesson 02 | 1-2 periods | Consistent lock ordering and a reason for each lock type. |
| `13_threading/04_thread_communication.py` | Producer-consumer with `Queue` | Loops and functions | 1-2 periods | Sentinel-based completion and `task_done()` correctness. |
| `13_threading/05_advanced_threading.py` | Thread-safe pool or cancellation design | Lessons 01-04 | 3-4 periods | Bounded work, graceful shutdown, and no blocked workers. |
| `13_threading/06_threading_challenges.py` | Classic synchronization problem | Locks, conditions, queues | 4+ periods | A written deadlock/starvation argument and repeated test runs. |

Threading projects must include a bounded workload, a shutdown strategy, and
no intentionally deadlocking code left enabled.

## Topic 14: Multiprocessing

| Lesson | Challenge | Prerequisites | Timebox | Suggested evidence |
|---|---|---|---:|---|
| `14_multiprocessing/01_process_basics.py` | Process lifecycle and process identity | Functions | 1 period | Correct process creation, joining, and main guard. |
| `14_multiprocessing/02_process_pool.py` | Map and asynchronous pool operations | Lists and functions | 1-2 periods | Ordered results and worker error handling. |
| `14_multiprocessing/03_process_communication.py` | Queue or pipe communication | Loops and serialization basics | 1-2 periods | Timeout/sentinel handling without `empty()` pre-checks. |
| `14_multiprocessing/04_shared_memory.py` | Shared state with synchronization | Process communication | 1-2 periods | A correct locked shared-counter example. |
| `14_multiprocessing/05_advanced_multiprocessing.py` | Multi-process pipeline | Lessons 01-04 | 3-4 periods | Clear ownership of queues, sentinels, and process cleanup. |
| `14_multiprocessing/06_parallel_computing.py` | Parallel computing case study | Process pools and benchmarks | 4+ periods | Correct baseline, measured result, and overhead analysis. |

Every multiprocessing project must use `if __name__ == "__main__":` around
process creation. Keep workers and functions at module scope so they can be
serialized across platforms.

## Topic 15: Asyncio

| Lesson | Challenge | Prerequisites | Timebox | Suggested evidence |
|---|---|---|---:|---|
| `15_asyncio/01_async_basics.py` | Coroutines and non-blocking waits | Functions and timing | 1 period | Sequential versus concurrent elapsed time. |
| `15_asyncio/02_async_await.py` | Tasks and dependent coroutines | Lesson 01 | 1-2 periods | Correct task creation, awaiting, and returned values. |
| `15_asyncio/03_async_tasks.py` | Timeouts and cooperative cancellation | Tasks and exceptions | 1-2 periods | Cancellation cleanup and an explained timeout result. |
| `15_asyncio/04_async_gathering.py` | Gather, partial failure, and result order | Lessons 01-03 | 1-2 periods | Successes and failures handled deliberately. |
| `15_asyncio/05_advanced_asyncio.py` | Bounded async queue or rate limiter | Queues, tasks, timing | 3-4 periods | Backpressure and bounded concurrency. |
| `15_asyncio/06_async_applications.py` | Scoped async service component | All prior topic 15 lessons | 4+ periods | A small, local simulation with tests and cancellation behavior. |

Asyncio works best for I/O-like waiting. Do not use it to speed up CPU-bound
calculations; use a process pool for those tasks.

## Completion Checklist

1. State the problem, inputs, outputs, and one non-goal before coding.
2. Implement a small sequential baseline when performance is part of the task.
3. Test a normal case, a boundary case, and one failure or cancellation case.
4. Explain one tradeoff, such as complexity versus speed or safety versus
   throughput.
5. Stop at the timebox and record the next improvement instead of expanding
   the project indefinitely.

# Classwork - Python Programming Practice

A collection of mini-assignments and programs for students to do quickly in class after learning about basic programming concepts in Python.

## 📚 Overview

This repository contains **90 mini-programs** organized into 15 major topics, each with 6 practice programs. Each program includes:
- Clear learning objectives
- Step-by-step TODO instructions
- Extensive comments to guide students
- Bonus challenges for advanced practice
- Progressive difficulty from simple to challenging

### Course Tracks

Use the folders as a differentiated course library rather than one required,
linear sequence:

- **AP CSP core:** Complete the foundation exercises in topics 1-8. Prioritize
  programs 01-04, procedures, lists, data analysis, and program design.
- **AP CSA preparation:** Continue with basic OOP and selected inheritance and
  polymorphism exercises in topics 9-10. Focus on object state, constructors,
  methods, composition, and collections of objects.
- **University enrichment:** Treat programs 05-06, advanced OOP, and
  concurrency topics as opt-in challenges. They introduce algorithms, systems
  design, and Python-specific features beyond the AP CSP curriculum.

### Difficulty Labels

Each topic includes six exercises with a consistent starting point:

- **Programs 1-2:** Foundation - simple, guided practice.
- **Programs 3-4:** Application - realistic combinations of the topic's core
  ideas.
- **Programs 5-6:** Extension - optional advanced challenges that may require
  independent research, additional algorithms, or multiple class periods.

## 🗂️ Program Categories

### 1. Variables, Expressions and Statements
**Location:** `01_variables_expressions_statements/`

Learn the fundamentals of Python variables, data types, and basic operations.

- **01_calculator.py** - Practice arithmetic operations and expressions
  - Create variables and perform calculations (addition, subtraction, multiplication, division)
  - Use modulo and power operators
  - Print formatted results

- **02_temperature_converter.py** - Convert between temperature scales
  - Work with float variables
  - Apply conversion formulas (Celsius, Fahrenheit, Kelvin)
  - Format numeric output

- **03_shopping_cart.py** - Calculate shopping cart totals with tax
  - Use multiple variables for related data
  - Calculate subtotals and tax amounts
  - Work with currency values

- **04_area_calculator.py** - Calculate areas and perimeters of shapes
  - Use variables in geometric formulas
  - Work with the constant pi
  - Calculate rectangle, circle, and triangle measurements

- **05_compound_interest.py** - Calculate compound interest over time
  - Apply complex mathematical formulas with multiple operations
  - Work with exponents and order of operations
  - Compare different compounding frequencies
  - Understand financial calculations

- **06_physics_simulator.py** - Simulate physics motion and energy
  - Combine multiple physics formulas
  - Chain calculations where results feed into subsequent steps
  - Work with kinetic and potential energy
  - Calculate motion under acceleration

### 2. Conditionals
**Location:** `02_conditionals/`

Master decision-making in Python using if, elif, and else statements.

- **01_grade_checker.py** - Assign letter grades based on scores
  - Use if-elif-else statements
  - Compare values with comparison operators
  - Validate input ranges

- **02_age_classifier.py** - Classify people into age groups
  - Work with multiple conditions
  - Use logical operators (and, or)
  - Apply age-based rules

- **03_number_comparator.py** - Compare and analyze numbers
  - Determine relationships between numbers
  - Practice nested if statements
  - Use comparison operators

- **04_password_validator.py** - Validate passwords based on rules
  - Work with string comparisons
  - Use the 'in' operator
  - Apply multiple validation conditions

### 3. Functions
**Location:** `03_functions/`

Learn to create reusable code with functions, parameters, and return values.

- **01_basic_functions.py** - Introduction to function basics
  - Define functions with def keyword
  - Use parameters and return statements
  - Understand function scope

- **02_temperature_functions.py** - Temperature conversion functions
  - Create functions that perform calculations
  - Call functions with different arguments
  - Build complex functions from simple ones

- **03_string_functions.py** - String manipulation functions
  - Work with string methods inside functions
  - Return modified strings
  - Practice parameter passing

- **04_math_functions.py** - Mathematical utility functions
  - Create functions for common math operations
  - Find maximum, minimum, and averages
  - Calculate areas and other measurements

### 4. Loops and Iteration
**Location:** `04_loops_iteration/`

Master repetition in Python using for loops and while loops.

- **01_counting_loops.py** - Basic loop counting and iteration
  - Use for loops with range()
  - Create counting sequences
  - Work with loop variables and steps

- **02_while_loops.py** - Conditional iteration with while loops
  - Understand loop conditions
  - Update loop variables correctly
  - Know when to use while vs for loops

- **03_loop_patterns.py** - Create visual patterns with loops
  - Use nested loops
  - Print shapes and patterns
  - Work with characters in loops

- **04_loop_accumulation.py** - Accumulate values using loops
  - Calculate sums and products
  - Track maximum and minimum values
  - Build lists using loops

### 5. Strings
**Location:** `05_strings/`

Explore string manipulation, formatting, and analysis.

- **01_string_basics.py** - String creation and manipulation
  - Use string indexing and slicing
  - Access individual characters
  - Concatenate strings

- **02_string_methods.py** - Built-in string methods
  - Transform strings (upper, lower, title)
  - Search within strings
  - Replace and split strings

- **03_string_formatting.py** - Format strings with f-strings
  - Create dynamic string output
  - Format numbers in strings
  - Combine variables in strings

- **04_string_iteration.py** - Iterate through and analyze strings
  - Loop through string characters
  - Count specific characters
  - Build new strings from existing ones

### 6. Lists
**Location:** `06_lists/`

Work with Python's most versatile data structure - lists.

- **01_list_basics.py** - List creation and basic operations
  - Create and initialize lists
  - Access and modify list elements
  - Understand list indexing

- **02_list_methods.py** - Built-in list methods
  - Add and remove elements (append, insert, remove, pop)
  - Sort and reverse lists
  - Search for elements

- **03_list_operations.py** - List operations and slicing
  - Concatenate and repeat lists
  - Extract sublists using slicing
  - Use built-in functions (sum, max, min)

- **04_list_iteration.py** - Iterate through and process lists
  - Loop through list elements
  - Create new lists from existing ones
  - Perform calculations on list data

### 7. Tuples, Sets and Dictionaries
**Location:** `07_tuples_sets_dictionaries/`

Master Python's essential data structures beyond lists.

- **01_tuple_basics.py** - Tuple creation and immutability
  - Create and access tuple elements
  - Understand tuple immutability
  - Unpack tuples and work with tuple methods

- **02_set_operations.py** - Set operations and uniqueness
  - Create sets and understand uniqueness
  - Perform union, intersection, and difference operations
  - Add and remove elements from sets

- **03_dictionary_basics.py** - Dictionary fundamentals
  - Create dictionaries with key-value pairs
  - Access and modify dictionary values
  - Work with nested dictionaries

- **04_dict_methods.py** - Advanced dictionary operations
  - Use dictionary methods (keys, values, items)
  - Iterate through dictionaries
  - Update and manipulate dictionary data

### 8. Exceptions & Files
**Location:** `08_exceptions_files/`

Learn to handle errors gracefully and work with files.

- **01_exception_handling.py** - Exception handling basics
  - Use try-except blocks
  - Handle specific exception types
  - Implement finally clause for cleanup

- **02_file_reading.py** - Reading files in Python
  - Open and read files with context managers
  - Read files line by line
  - Handle file-related exceptions

- **03_file_writing.py** - Writing data to files
  - Write and append to files
  - Use different file modes
  - Write lists and dictionaries to files

- **04_json_files.py** - Working with JSON data
  - Parse and generate JSON
  - Read and write JSON files
  - Handle JSON exceptions

### 9. Basic OOP
**Location:** `09_basic_oop/`

Introduction to Object-Oriented Programming concepts.

- **01_simple_class.py** - Creating simple classes
  - Define classes and create instances
  - Use __init__ method for initialization
  - Access and modify object attributes

- **02_class_attributes.py** - Class vs instance attributes
  - Understand the difference between class and instance attributes
  - Share data across all instances
  - Track class-level information

- **03_class_methods.py** - Methods and behavior
  - Define methods inside classes
  - Use the self parameter
  - Return values from methods

- **04_multiple_objects.py** - Working with multiple objects
  - Create and manage multiple instances
  - Store objects in lists
  - Iterate through and compare objects
- **05_composition_aggregation.py** - Object composition and aggregation
  - Model "has-a" relationships with collaborating objects
  - Manage collections owned by another object

### 10. Intermediate OOP
**Location:** `10_intermediate_oop/`

Advanced OOP concepts for code reuse and organization.

- **01_inheritance.py** - Class inheritance basics
  - Create parent and child classes
  - Inherit attributes and methods
  - Extend parent class functionality

- **02_method_overriding.py** - Overriding parent methods
  - Override methods in child classes
  - Customize inherited behavior
  - Create specialized implementations

- **03_super_function.py** - Using super()
  - Call parent class methods
  - Extend parent functionality
  - Work with multi-level inheritance

- **04_multiple_inheritance.py** - Multiple inheritance
  - Inherit from multiple parent classes
  - Combine functionality from different sources
  - Understand method resolution order
- **05_polymorphism_interfaces.py** - Polymorphism and interfaces
  - Design shared behavior contracts
  - Use different objects through the same methods

### 11. Advanced OOP
**Location:** `11_advanced_oop/`

Professional OOP patterns and techniques.

- **01_properties.py** - Properties and getters/setters
  - Use @property decorator
  - Create computed properties
  - Validate attribute access

- **02_class_methods_static.py** - Class and static methods
  - Use @classmethod decorator
  - Use @staticmethod decorator
  - Know when to use each method type

- **03_magic_methods.py** - Special methods (dunder methods)
  - Override __str__ and __repr__
  - Implement comparison operators
  - Overload arithmetic operators

- **04_abstract_classes.py** - Abstract base classes
  - Use ABC and @abstractmethod
  - Create interfaces
  - Enforce method implementation

### 12. Concurrent and Parallel Programming
**Location:** `12_concurrent_parallel/`

Learn to write concurrent and parallel code for better performance.

- **01_concurrent_basics.py** - Concurrency fundamentals
  - Understand concurrent vs parallel execution
  - Use ThreadPoolExecutor
  - Work with Future objects

- **02_futures.py** - Working with futures
  - Check future status
  - Add callbacks to futures
  - Handle timeouts and cancellation

- **03_process_pool.py** - Process-based parallelism
  - Use ProcessPoolExecutor for CPU-bound tasks
  - Compare threads vs processes
  - Parallelize computational work

- **04_thread_pool.py** - Thread pool management
  - Master ThreadPoolExecutor
  - Handle shared resources
  - Manage thread pool size

### 13. Threading
**Location:** `13_threading/`

Deep dive into Python threading for concurrent execution.

- **01_thread_basics.py** - Threading fundamentals
  - Create and start threads
  - Pass arguments to threads
  - Use join() to wait for completion

- **02_thread_synchronization.py** - Synchronizing threads
  - Understand race conditions
  - Use locks to prevent race conditions
  - Work with semaphores

- **03_thread_locks.py** - Locks and RLocks
  - Master different lock types
  - Use reentrant locks
  - Implement timeout for locks

- **04_thread_communication.py** - Thread communication
  - Use Events for signaling
  - Implement producer-consumer with Queue
  - Use Condition variables

### 14. Multiprocessing
**Location:** `14_multiprocessing/`

Leverage multiple CPU cores with multiprocessing.

- **01_process_basics.py** - Multiprocessing fundamentals
  - Create and manage processes
  - Understand process vs thread
  - Pass arguments to processes

- **02_process_pool.py** - Process pools
  - Use Pool for parallel execution
  - Apply functions to multiple inputs
  - Manage worker processes

- **03_process_communication.py** - Inter-process communication
  - Use Queue for process communication
  - Use Pipe for bidirectional communication
  - Implement producer-consumer pattern

- **04_shared_memory.py** - Shared memory
  - Use Value and Array for shared memory
  - Use Manager for shared objects
  - Synchronize access to shared memory

### 15. Asyncio
**Location:** `15_asyncio/`

Master asynchronous programming with asyncio.

- **01_async_basics.py** - Asyncio fundamentals
  - Create coroutines with async/await
  - Run coroutines with asyncio.run()
  - Understand the event loop

- **02_async_await.py** - Async/await patterns
  - Use asyncio.create_task()
  - Run multiple coroutines concurrently
  - Master async/await syntax

- **03_async_tasks.py** - Managing async tasks
  - Create and manage tasks
  - Cancel and timeout tasks
  - Monitor task status

- **04_async_gathering.py** - Gathering results
  - Use asyncio.gather()
  - Handle exceptions in concurrent operations
  - Coordinate multiple async operations

## 🚀 How to Use This Repository

### For Students:

1. **Choose a topic** you want to practice
2. **Open the corresponding folder** (e.g., `01_variables_expressions_statements/`)
3. **Start with program 01** and work through sequentially
4. **Read the learning objectives** at the top of each file
5. **Follow the TODO comments** - they guide you step by step
6. **Complete each TODO** by writing code where indicated
7. **Run your program** to test your solutions
8. **Try the BONUS TODO** for extra practice

### Running a Program:

```bash
# Navigate to the repository
cd Classwork

# Run any program with Python
# Beginner topics:
python 01_variables_expressions_statements/01_calculator.py
python 02_conditionals/01_grade_checker.py
python 03_functions/01_basic_functions.py

# Intermediate topics:
python 07_tuples_sets_dictionaries/01_tuple_basics.py
python 08_exceptions_files/01_exception_handling.py
python 09_basic_oop/01_simple_class.py

# Advanced topics:
python 12_concurrent_parallel/01_concurrent_basics.py
python 13_threading/01_thread_basics.py
python 15_asyncio/01_async_basics.py
# ... and so on
```

### Reference Solutions and Tests

Completed reference implementations are in `solutions/`, with the same topic
and lesson filenames as the starter worksheets. They cover AP CSP core topics
01-08 and the AP CSA-prep OOP lessons:

- `09_basic_oop/01_simple_class.py` through `05_composition_aggregation.py`
- `10_intermediate_oop/01_inheritance.py`, `02_method_overriding.py`,
  `03_super_function.py`, and `05_polymorphism_interfaces.py`

Run an individual solution directly, for example:

```bash
python solutions/03_functions/02_temperature_functions.py
```

Run the complete standard-library test suite with:

```bash
python -m unittest discover -s tests
```

That command validates the completed reference implementations in `solutions/`,
including the AP CSA-prep OOP lessons; it does not check your worksheet work.
Students can run their separate self-checks with:

```bash
python -m unittest discover -s starter_tests
```

See [starter_tests/README.md](starter_tests/README.md) for how those
incomplete-until-finished checks work.

### For Educators

See [TEACHER_GUIDE.md](TEACHER_GUIDE.md) for a suggested AP CSP pacing
sequence, AP CSA-prep extensions, university enrichment boundaries, and an
assessment rubric.

### Optional Enrichment

See [ENRICHMENT_CATALOG.md](ENRICHMENT_CATALOG.md) to choose an advanced OOP
or concurrency challenge with prerequisites, a timebox, and clear deliverable
expectations.

### AP CSP Companion Activities

The programming sequence is supplemented by
[ap_csp_companion/](ap_csp_companion/README.md): short activities on data
representation, networks, cybersecurity and privacy, and computing impacts.

### Tips for Success:

- ✅ **Complete programs in order** - each builds on previous concepts
- ✅ **Read all comments carefully** - they contain important hints
- ✅ **Test your code frequently** - run the program after completing each TODO
- ✅ **Experiment** - try different values and see what happens
- ✅ **Attempt the bonus challenges** - they reinforce your learning
- ✅ **Don't skip ahead** - foundational concepts are important

## 📖 Learning Path

### AP CSP Core

Use this recommended order for the core sequence:

1. **Variables, Expressions and Statements** (Foundation)
2. **Conditionals** (Decision Making)
3. **Loops and Iteration** (Repetition)
4. **Functions** (Code Organization)
5. **Strings** (Text Processing)
6. **Lists** (Data Collections)
7. **Tuples, Sets and Dictionaries** (Collections and Data Modeling)
8. **Exceptions & Files** (Error Handling and Data Persistence)

Programs 01-04 are the intended core exercises. Programs 05-06 are optional
extensions, especially when they introduce recursion, advanced algorithms, or
multi-part systems.

### AP CSA Preparation

9. **Basic OOP** (Object-Oriented Basics)
10. **Intermediate OOP** (Inheritance & Polymorphism)

Use programs 01-04 in Basic OOP and selected inheritance, overriding, `super`,
and polymorphism exercises. Reference solutions and self-checks are available
for Basic OOP lessons 01-05 and Intermediate OOP lessons 01-03 and 05. These
reinforce the transferable OOP concepts that students will use in Java.

### University Enrichment

11. **Advanced OOP** (Python-Specific OOP Features)
12. **Concurrent and Parallel Programming** (Performance Optimization)
13. **Threading** (Concurrent Execution)
14. **Multiprocessing** (Parallel Execution)
15. **Asyncio** (Asynchronous Programming)

These topics are optional extensions for students ready to research
prerequisites and tackle longer projects.

## 🎯 Program Difficulty

Each folder contains 6 programs that increase in difficulty:
- **Program 01**: Very simple - introduction to basic concepts
- **Program 02**: Simple - basic practice with minor variations
- **Program 03**: Moderate - combining multiple concepts
- **Program 04**: Intermediate - more complex scenarios and applications
- **Program 05**: Extension - advanced, multi-step problem; may require
  independent research
- **Program 06**: University challenge - comprehensive application beyond the
  standard AP CSP sequence
- **BONUS TODOs**: Extra challenges for additional practice in each program

## 💡 Getting Help

If you get stuck:
1. Re-read the TODO comment and any hints provided
2. Review the learning objectives at the top of the file
3. Check earlier TODOs in the same file for similar examples
4. Try running the program to see what happens
5. Look at programs in earlier folders for simpler examples

## 🤝 Contributing

Students and educators are welcome to contribute:
- Report issues or bugs
- Suggest new mini-programs
- Improve existing comments and instructions
- Add more BONUS challenges

## 📝 License

This repository is intended for educational purposes. Feel free to use these programs in your classroom or for personal learning.

---

**Happy Coding! 🐍✨**

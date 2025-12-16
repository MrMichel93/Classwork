# Tuples, Sets and Dictionaries

## 📖 What Are These Data Structures?

Python provides several built-in data structures beyond lists. **Tuples**, **sets**, and **dictionaries** each have unique characteristics and use cases that make them essential tools for different programming scenarios.

### Understanding These Data Structures

- **Tuples** are **immutable** sequences (can't be changed after creation)
- **Sets** store **unique** values (no duplicates) and are **unordered**
- **Dictionaries** store **key-value pairs** for fast lookups
- Each structure has specific strengths for different situations
- Choosing the right data structure improves code efficiency

### Why Use Different Data Structures?

✅ **Tuples** - Protect data from modification, return multiple values, use as dictionary keys  
✅ **Sets** - Remove duplicates, test membership quickly, perform mathematical set operations  
✅ **Dictionaries** - Fast lookups by key, store related data, represent real-world objects  
✅ **Performance** - Each structure is optimized for specific operations  
✅ **Clarity** - Using the right structure makes your intent clear  

## 📦 Tuples

### What Are Tuples?

A **tuple** is an immutable sequence of values. Once created, a tuple cannot be modified.

```python
# Create tuples with parentheses
coordinates = (10, 20, 30)
point = (3.5, 7.2)
empty = ()

# Parentheses are optional (but recommended for clarity)
also_tuple = 1, 2, 3

# Single-element tuple (comma is required!)
single = (5,)          # This is a tuple
not_tuple = (5)        # This is just the number 5 in parentheses

# Mixed types
person = ("Alice", 25, "Engineer")

# Nested tuples
matrix = ((1, 2), (3, 4), (5, 6))
```

### Accessing Tuple Elements

```python
coordinates = (10, 20, 30, 40, 50)

# Indexing (same as lists)
print(coordinates[0])       # 10 (first element)
print(coordinates[-1])      # 50 (last element)

# Slicing (same as lists)
print(coordinates[1:3])     # (20, 30)
print(coordinates[:2])      # (10, 20)
print(coordinates[::2])     # (10, 30, 50) (every 2nd element)
```

### Tuple Operations

```python
# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2      # (1, 2, 3, 4, 5, 6)

# Repetition
repeated = (1, 2) * 3           # (1, 2, 1, 2, 1, 2)

# Membership testing
print(2 in tuple1)              # True
print(10 not in tuple1)         # True

# Length
print(len(tuple1))              # 3
```

### Tuple Methods

Tuples have only two methods (because they're immutable):

```python
numbers = (1, 2, 3, 2, 4, 2, 5)

# count() - Count occurrences of a value
count = numbers.count(2)        # 3

# index() - Find first index of value
position = numbers.index(4)     # 4
# position = numbers.index(10)  # ValueError! (not found)
```

### Tuple Unpacking

```python
# Unpack tuple into variables
point = (10, 20)
x, y = point                    # x=10, y=20

# Works with any iterable
coordinates = (10, 20, 30)
x, y, z = coordinates           # x=10, y=20, z=30

# Swap variables easily
a, b = 1, 2
a, b = b, a                     # Now a=2, b=1

# Ignore values with underscore
name, age, _ = ("Alice", 25, "Engineer")  # Ignore third value

# Extended unpacking (Python 3+)
first, *middle, last = (1, 2, 3, 4, 5)
# first=1, middle=[2, 3, 4], last=5
```

### Why Use Tuples?

```python
# ✅ Return multiple values from functions
def get_dimensions():
    return 10, 20, 30           # Returns a tuple

length, width, height = get_dimensions()

# ✅ Protect data from accidental modification
DAYS_OF_WEEK = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
# DAYS_OF_WEEK[0] = "Monday"  # TypeError! Can't modify

# ✅ Use as dictionary keys (tuples are hashable)
locations = {
    (0, 0): "origin",
    (1, 2): "point A",
    (3, 4): "point B"
}

# ✅ Slightly faster than lists for iteration
```

### Tuple vs List

```python
# List - mutable, use when data needs to change
shopping_list = ["eggs", "milk", "bread"]
shopping_list.append("butter")      # OK - can modify

# Tuple - immutable, use when data should be fixed
coordinates = (10, 20)
# coordinates.append(30)            # Error! No append method
# coordinates[0] = 15               # Error! Can't modify
```

## 🎲 Sets

### What Are Sets?

A **set** is an unordered collection of unique elements. Sets automatically remove duplicates.

```python
# Create sets with curly braces
numbers = {1, 2, 3, 4, 5}

# Create from list (removes duplicates)
numbers_with_dupes = [1, 2, 2, 3, 3, 3, 4, 5]
unique_numbers = set(numbers_with_dupes)    # {1, 2, 3, 4, 5}

# Empty set (must use set(), not {})
empty = set()                               # Empty set
empty_dict = {}                             # This is an empty dictionary!

# Mixed types (but all must be hashable)
mixed = {1, "hello", 3.14, True}
```

### Set Characteristics

```python
# Sets are UNORDERED - no indexing
my_set = {3, 1, 4, 1, 5, 9}
# print(my_set[0])                  # Error! Sets don't support indexing

# Sets contain UNIQUE values only
numbers = {1, 2, 3, 2, 1}
print(numbers)                      # {1, 2, 3} (duplicates removed)

# Sets are MUTABLE - can add/remove elements
my_set.add(10)
my_set.remove(3)
```

### Adding and Removing Elements

```python
fruits = {"apple", "banana", "cherry"}

# add() - Add single element
fruits.add("date")
print(fruits)                       # {'apple', 'banana', 'cherry', 'date'}

# add() ignores duplicates
fruits.add("apple")                 # No effect (already exists)

# update() - Add multiple elements
fruits.update(["elderberry", "fig"])
fruits.update({"grape", "honeydew"})

# remove() - Remove element (raises error if not found)
fruits.remove("banana")
# fruits.remove("kiwi")             # KeyError! (doesn't exist)

# discard() - Remove element (no error if not found)
fruits.discard("cherry")
fruits.discard("kiwi")              # OK - no error

# pop() - Remove and return arbitrary element
item = fruits.pop()
print(item)                         # Some element from the set

# clear() - Remove all elements
fruits.clear()
print(fruits)                       # set()
```

### Set Operations

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union - all elements from both sets
union = set1 | set2                 # {1, 2, 3, 4, 5, 6, 7, 8}
union = set1.union(set2)            # Same result

# Intersection - elements in both sets
intersection = set1 & set2          # {4, 5}
intersection = set1.intersection(set2)  # Same result

# Difference - elements in first but not second
difference = set1 - set2            # {1, 2, 3}
difference = set1.difference(set2)  # Same result

# Symmetric difference - elements in either but not both
sym_diff = set1 ^ set2              # {1, 2, 3, 6, 7, 8}
sym_diff = set1.symmetric_difference(set2)  # Same result

# Subset - all elements of set1 in set2?
small = {1, 2}
print(small <= set1)                # True (small is subset of set1)
print(small.issubset(set1))         # True

# Superset - set1 contains all elements of small?
print(set1 >= small)                # True
print(set1.issuperset(small))       # True

# Disjoint - no common elements?
print(set1.isdisjoint({10, 11}))    # True (no overlap)
```

### Set Comprehensions

```python
# Create sets with comprehensions
squares = {x**2 for x in range(10)}
# {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# With condition
evens = {x for x in range(20) if x % 2 == 0}
# {0, 2, 4, 6, 8, 10, 12, 14, 16, 18}
```

### Why Use Sets?

```python
# ✅ Remove duplicates from a list
numbers = [1, 2, 2, 3, 3, 3, 4, 5]
unique = list(set(numbers))         # [1, 2, 3, 4, 5]

# ✅ Fast membership testing (faster than lists)
large_set = set(range(1000000))
print(999999 in large_set)          # Very fast!

# ✅ Mathematical set operations
students_math = {"Alice", "Bob", "Charlie"}
students_science = {"Bob", "Charlie", "David"}

# Students in both classes
both = students_math & students_science         # {"Bob", "Charlie"}

# Students in at least one class
either = students_math | students_science       # {"Alice", "Bob", "Charlie", "David"}

# Students only in math
only_math = students_math - students_science    # {"Alice"}
```

## 📚 Dictionaries

### What Are Dictionaries?

A **dictionary** is an unordered collection of key-value pairs. Keys must be unique and immutable.

```python
# Create dictionaries with curly braces
person = {
    "name": "Alice",
    "age": 25,
    "city": "NYC"
}

# Create with dict() constructor
person2 = dict(name="Bob", age=30, city="LA")

# Empty dictionary
empty = {}
also_empty = dict()

# Mixed value types
mixed = {
    "name": "Alice",
    "age": 25,
    "scores": [90, 85, 88],
    "is_student": True
}
```

### Accessing Dictionary Values

```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "NYC"
}

# Access with square brackets
print(person["name"])               # "Alice"
# print(person["country"])          # KeyError! (key doesn't exist)

# Access with get() - safer, returns None if not found
print(person.get("name"))           # "Alice"
print(person.get("country"))        # None (no error)
print(person.get("country", "USA")) # "USA" (default value)

# Check if key exists
if "age" in person:
    print(person["age"])

# Check if key doesn't exist
if "country" not in person:
    print("Country not specified")
```

### Modifying Dictionaries

```python
person = {"name": "Alice", "age": 25}

# Add or update entries
person["city"] = "NYC"              # Add new key-value pair
person["age"] = 26                  # Update existing value

# Update multiple entries
person.update({"job": "Engineer", "city": "SF"})

# Remove entries
del person["city"]                  # Remove key-value pair
# del person["country"]             # KeyError! (doesn't exist)

# pop() - Remove and return value
age = person.pop("age")             # Returns 26, removes "age" key
default = person.pop("missing", 0)  # Returns 0 (key doesn't exist)

# popitem() - Remove and return arbitrary key-value pair
item = person.popitem()             # Returns tuple like ("name", "Alice")

# clear() - Remove all entries
person.clear()
```

### Dictionary Methods

```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "NYC"
}

# keys() - Get all keys
keys = person.keys()
print(keys)                         # dict_keys(['name', 'age', 'city'])
print(list(keys))                   # ['name', 'age', 'city']

# values() - Get all values
values = person.values()
print(list(values))                 # ['Alice', 25, 'NYC']

# items() - Get all key-value pairs
items = person.items()
print(list(items))                  # [('name', 'Alice'), ('age', 25), ('city', 'NYC')]

# copy() - Create shallow copy
person_copy = person.copy()

# setdefault() - Get value or set default if key doesn't exist
country = person.setdefault("country", "USA")
print(country)                      # "USA" (added to dictionary)
```

### Iterating Through Dictionaries

```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "NYC"
}

# Iterate through keys (default)
for key in person:
    print(key)                      # name, age, city

# Iterate through keys explicitly
for key in person.keys():
    print(key)

# Iterate through values
for value in person.values():
    print(value)                    # Alice, 25, NYC

# Iterate through key-value pairs (most common)
for key, value in person.items():
    print(f"{key}: {value}")
# Output:
# name: Alice
# age: 25
# city: NYC
```

### Nested Dictionaries

```python
# Dictionary of dictionaries
students = {
    "student1": {
        "name": "Alice",
        "age": 20,
        "grades": [90, 85, 88]
    },
    "student2": {
        "name": "Bob",
        "age": 22,
        "grades": [75, 80, 85]
    }
}

# Access nested values
print(students["student1"]["name"])         # "Alice"
print(students["student2"]["grades"][0])    # 75

# Modify nested values
students["student1"]["age"] = 21
students["student2"]["grades"].append(90)

# Iterate through nested dictionary
for student_id, info in students.items():
    print(f"{student_id}:")
    for key, value in info.items():
        print(f"  {key}: {value}")
```

### Dictionary Comprehensions

```python
# Create dictionaries with comprehensions
squares = {x: x**2 for x in range(6)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Transform existing dictionary
prices = {"apple": 0.50, "banana": 0.30, "cherry": 0.80}
prices_doubled = {item: price * 2 for item, price in prices.items()}
# {'apple': 1.0, 'banana': 0.6, 'cherry': 1.6}
```

### Why Use Dictionaries?

```python
# ✅ Fast lookups by key (O(1) average time)
phone_book = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9012"
}
print(phone_book["Alice"])          # Very fast lookup

# ✅ Store related data together
person = {
    "name": "Alice",
    "age": 25,
    "email": "alice@example.com",
    "skills": ["Python", "Java", "SQL"]
}

# ✅ Count occurrences
text = "hello world"
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

# ✅ Group data
students = [
    ("Alice", "A"),
    ("Bob", "B"),
    ("Charlie", "A"),
    ("David", "B")
]
by_grade = {}
for name, grade in students:
    if grade not in by_grade:
        by_grade[grade] = []
    by_grade[grade].append(name)
# {'A': ['Alice', 'Charlie'], 'B': ['Bob', 'David']}
```

## 🔄 Choosing the Right Data Structure

### Quick Reference

```python
# List - ordered, mutable, allows duplicates, indexed
my_list = [1, 2, 3, 2, 4]
my_list[0] = 10                     # ✅ Can modify
my_list.append(5)                   # ✅ Can add

# Tuple - ordered, immutable, allows duplicates, indexed
my_tuple = (1, 2, 3, 2, 4)
# my_tuple[0] = 10                  # ❌ Can't modify
# my_tuple.append(5)                # ❌ Can't add

# Set - unordered, mutable, unique values only, not indexed
my_set = {1, 2, 3, 4, 5}
my_set.add(6)                       # ✅ Can add
# my_set[0]                         # ❌ No indexing
my_set.add(3)                       # No effect (already exists)

# Dictionary - unordered, mutable, unique keys, key-based access
my_dict = {"a": 1, "b": 2, "c": 3}
my_dict["d"] = 4                    # ✅ Can add
# my_dict[0]                        # ❌ No numeric indexing
```

### Decision Guide

```python
# Use LIST when:
# - Order matters
# - You need to access by index
# - Duplicates are allowed
# - You need to modify elements
tasks = ["task1", "task2", "task3"]

# Use TUPLE when:
# - Data shouldn't change
# - Returning multiple values from function
# - Using as dictionary key
coordinates = (10, 20, 30)

# Use SET when:
# - You need unique values only
# - Fast membership testing
# - Mathematical set operations
unique_visitors = {"user1", "user2", "user3"}

# Use DICTIONARY when:
# - You need key-value associations
# - Fast lookup by key
# - Storing object attributes
user = {"name": "Alice", "age": 25}
```

## 📚 Mini-Programs in This Folder

Apply these concepts in the following programs:

1. **01_tuple_basics.py** - Tuple fundamentals
   - Create and initialize tuples
   - Access elements using indexing
   - Understand tuple immutability
   - Use tuple methods (count, index)
   - Practice tuple unpacking
   - Work with single-element and nested tuples

2. **02_set_operations.py** - Working with sets
   - Create sets and understand uniqueness
   - Add and remove elements
   - Perform union, intersection, difference operations
   - Test membership and subsets
   - Remove duplicates from sequences
   - Use set comprehensions

3. **03_dictionary_basics.py** - Dictionary fundamentals
   - Create dictionaries with key-value pairs
   - Access and modify dictionary values
   - Use dictionary methods (keys, values, items, get)
   - Check for key existence
   - Work with nested dictionaries
   - Iterate through dictionaries

4. **04_dict_methods.py** - Advanced dictionary operations
   - Use update(), pop(), popitem()
   - Work with setdefault() method
   - Create dictionary comprehensions
   - Merge and copy dictionaries
   - Count occurrences with dictionaries
   - Group and transform data

## 💡 Quick Tips

✅ **Best Practices:**
- Use tuples for fixed collections (coordinates, RGB colors, dates)
- Use sets to remove duplicates or test membership
- Use dictionaries for fast lookups and related data
- Choose immutable structures (tuples) when data shouldn't change
- Use descriptive keys in dictionaries
- Remember: sets and dictionary keys must be hashable (immutable)

❌ **Common Mistakes:**
- Forgetting comma in single-element tuple: `(5,)` not `(5)`
- Using `{}` for empty set (creates dict, not set!)
- Trying to index sets: `my_set[0]` won't work
- Using mutable objects as dictionary keys (lists, sets)
- Forgetting dictionaries are unordered (in Python < 3.7)
- Modifying dictionary/set while iterating over it

## 🎓 Key Takeaways

1. **Tuples** are immutable sequences - use for fixed data
2. **Sets** store unique values - use for deduplication and set operations
3. **Dictionaries** map keys to values - use for fast lookups
4. Tuples can be used as dictionary keys (they're hashable)
5. Sets automatically remove duplicates
6. Dictionary keys must be unique and immutable
7. Use `.get()` for safe dictionary access
8. Choose the right data structure for your use case
9. All three structures support comprehension syntax
10. Understanding when to use each structure makes code more efficient and clear

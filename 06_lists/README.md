# Lists

## 📖 What Are Lists?

A **list** is a collection of items stored in a single variable. Lists are one of the most versatile and commonly used data structures in Python.

### Understanding Lists

- Lists store **multiple values** in a single variable
- Lists are **ordered** (items have a specific position)
- Lists are **mutable** (can be changed after creation)
- Lists can contain **different types** (integers, strings, floats, even other lists)
- Lists use **square brackets** `[]`

### Why Use Lists?

✅ **Store collections** - Keep related items together  
✅ **Maintain order** - Items stay in the order you add them  
✅ **Dynamic size** - Grow or shrink as needed  
✅ **Versatile** - Store any type of data  
✅ **Powerful operations** - Many built-in methods  

## 🎯 Creating Lists

### Basic List Creation

```python
# Empty list
empty_list = []
also_empty = list()

# List of integers
numbers = [1, 2, 3, 4, 5]

# List of strings
fruits = ["apple", "banana", "cherry"]

# Mixed types
mixed = [42, "hello", 3.14, True]

# List of lists (2D list)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# List from range
numbers = list(range(5))            # [0, 1, 2, 3, 4]
evens = list(range(0, 10, 2))       # [0, 2, 4, 6, 8]
```

## 🔍 Accessing List Elements

### Indexing

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Positive indexing (from left, starts at 0)
print(fruits[0])        # 'apple' (first item)
print(fruits[1])        # 'banana'
print(fruits[4])        # 'elderberry' (last item)

# Negative indexing (from right, starts at -1)
print(fruits[-1])       # 'elderberry' (last item)
print(fruits[-2])       # 'date' (second to last)
print(fruits[-5])       # 'apple' (first item)

# Index diagram:
#   apple   banana  cherry  date    elderberry
#     0       1       2      3          4       (positive)
#    -5      -4      -3     -2         -1       (negative)

# Index errors
# print(fruits[10])     # IndexError! (out of range)
```

### Slicing

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing [start:stop] - from start to stop-1
print(numbers[2:5])         # [2, 3, 4]
print(numbers[0:3])         # [0, 1, 2]

# Omit start (defaults to beginning)
print(numbers[:4])          # [0, 1, 2, 3]

# Omit stop (defaults to end)
print(numbers[6:])          # [6, 7, 8, 9]

# Omit both (copy entire list)
print(numbers[:])           # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Negative indices
print(numbers[-3:])         # [7, 8, 9] (last 3)
print(numbers[:-2])         # [0, 1, 2, 3, 4, 5, 6, 7] (all but last 2)

# Step (every nth element)
print(numbers[::2])         # [0, 2, 4, 6, 8] (every 2nd)
print(numbers[1::2])        # [1, 3, 5, 7, 9] (every 2nd, starting at 1)

# Reverse a list
print(numbers[::-1])        # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

## ✏️ Modifying Lists

### Changing Elements

```python
# Lists are mutable - you can change elements
numbers = [1, 2, 3, 4, 5]
numbers[0] = 10             # First element: 1 → 10
numbers[-1] = 50            # Last element: 5 → 50
print(numbers)              # [10, 2, 3, 4, 50]

# Change multiple elements with slicing
numbers[1:3] = [20, 30]
print(numbers)              # [10, 20, 30, 4, 50]
```

### Adding Elements

```python
fruits = ["apple", "banana"]

# append() - Add to end (most common)
fruits.append("cherry")
print(fruits)               # ['apple', 'banana', 'cherry']

# insert() - Add at specific position
fruits.insert(1, "blueberry")
print(fruits)               # ['apple', 'blueberry', 'banana', 'cherry']

# extend() - Add multiple items from another list
fruits.extend(["date", "elderberry"])
print(fruits)               # ['apple', 'blueberry', 'banana', 'cherry', 'date', 'elderberry']

# + operator - Concatenate lists (creates new list)
more_fruits = fruits + ["fig", "grape"]
print(more_fruits)
```

### Removing Elements

```python
fruits = ["apple", "banana", "cherry", "date", "banana"]

# remove() - Remove first occurrence of value
fruits.remove("banana")
print(fruits)               # ['apple', 'cherry', 'date', 'banana']

# pop() - Remove and return element at index (default: last)
last = fruits.pop()
print(last)                 # 'banana'
print(fruits)               # ['apple', 'cherry', 'date']

first = fruits.pop(0)
print(first)                # 'apple'
print(fruits)               # ['cherry', 'date']

# del - Delete element(s) by index or slice
numbers = [1, 2, 3, 4, 5]
del numbers[0]              # Remove first
print(numbers)              # [2, 3, 4, 5]

del numbers[1:3]            # Remove slice
print(numbers)              # [2, 5]

# clear() - Remove all elements
numbers.clear()
print(numbers)              # []
```

## 📋 List Methods

### Adding and Removing

```python
# append(item) - Add item to end
numbers = [1, 2, 3]
numbers.append(4)           # [1, 2, 3, 4]

# insert(index, item) - Insert item at index
numbers.insert(0, 0)        # [0, 1, 2, 3, 4]

# extend(iterable) - Add all items from iterable
numbers.extend([5, 6])      # [0, 1, 2, 3, 4, 5, 6]

# remove(item) - Remove first occurrence
numbers.remove(0)           # [1, 2, 3, 4, 5, 6]

# pop([index]) - Remove and return item at index
last = numbers.pop()        # 6; list is now [1, 2, 3, 4, 5]
second = numbers.pop(1)     # 2; list is now [1, 3, 4, 5]

# clear() - Remove all items
numbers.clear()             # []
```

### Searching and Counting

```python
numbers = [1, 2, 3, 2, 4, 2, 5]

# index(item) - Find first index of item
pos = numbers.index(3)      # 2
# pos = numbers.index(10)   # ValueError! (not found)

# count(item) - Count occurrences
count = numbers.count(2)    # 3

# in operator - Check if item exists
print(3 in numbers)         # True
print(10 in numbers)        # False
print(10 not in numbers)    # True
```

### Sorting and Reversing

```python
numbers = [3, 1, 4, 1, 5, 9, 2]

# sort() - Sort in place (modifies original list)
numbers.sort()
print(numbers)              # [1, 1, 2, 3, 4, 5, 9]

# sort(reverse=True) - Sort descending
numbers.sort(reverse=True)
print(numbers)              # [9, 5, 4, 3, 2, 1, 1]

# sorted() - Return new sorted list (original unchanged)
original = [3, 1, 4, 1, 5]
sorted_list = sorted(original)
print(original)             # [3, 1, 4, 1, 5] (unchanged)
print(sorted_list)          # [1, 1, 3, 4, 5] (new list)

# reverse() - Reverse in place
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)              # [5, 4, 3, 2, 1]

# reversed() - Return reversed iterator
numbers = [1, 2, 3, 4, 5]
reversed_list = list(reversed(numbers))
print(numbers)              # [1, 2, 3, 4, 5] (unchanged)
print(reversed_list)        # [5, 4, 3, 2, 1]
```

### Copying Lists

```python
original = [1, 2, 3]

# ❌ WRONG: Assignment doesn't copy, creates reference
copy = original
copy.append(4)
print(original)             # [1, 2, 3, 4] (modified too!)

# ✅ CORRECT: Various ways to copy
original = [1, 2, 3]

# Method 1: copy() method
copy1 = original.copy()

# Method 2: list() constructor
copy2 = list(original)

# Method 3: Slicing
copy3 = original[:]

# All create independent copies
copy1.append(4)
print(original)             # [1, 2, 3] (unchanged)
print(copy1)                # [1, 2, 3, 4]
```

## 🔢 List Operations

### Concatenation and Repetition

```python
# + operator - Concatenate lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2        # [1, 2, 3, 4, 5, 6]

# * operator - Repeat lists
zeros = [0] * 5                 # [0, 0, 0, 0, 0]
pattern = [1, 2] * 3            # [1, 2, 1, 2, 1, 2]
```

### List Comprehensions

Create lists in a concise way.

```python
# Basic list comprehension
squares = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With condition
evens = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Transform items
fruits = ["apple", "banana", "cherry"]
upper_fruits = [fruit.upper() for fruit in fruits]
# ['APPLE', 'BANANA', 'CHERRY']

# Nested comprehension
matrix = [[i*j for j in range(3)] for i in range(3)]
# [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
```

## 🔄 Iterating Through Lists

### Basic Iteration

```python
fruits = ["apple", "banana", "cherry"]

# Iterate through items
for fruit in fruits:
    print(fruit)
# Output: apple, banana, cherry

# Iterate with index
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")
# Output:
# 0: apple
# 1: banana
# 2: cherry

# Better: Use enumerate()
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Start enumeration at 1
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")
# Output:
# 1: apple
# 2: banana
# 3: cherry
```

### Processing Lists

```python
# Sum all elements
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(total)                # 15

# Or use built-in sum()
print(sum(numbers))         # 15

# Find maximum
numbers = [45, 23, 67, 12, 89]
max_val = numbers[0]
for num in numbers:
    if num > max_val:
        max_val = num
print(max_val)              # 89

# Or use built-in max()
print(max(numbers))         # 89

# Filter items
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
print(evens)                # [2, 4, 6, 8, 10]

# Transform items
numbers = [1, 2, 3, 4, 5]
squares = []
for num in numbers:
    squares.append(num ** 2)
print(squares)              # [1, 4, 9, 16, 25]
```

## 🎯 Built-in Functions for Lists

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# len() - Length of list
print(len(numbers))         # 8

# min() - Minimum value
print(min(numbers))         # 1

# max() - Maximum value
print(max(numbers))         # 9

# sum() - Sum of all elements
print(sum(numbers))         # 31

# sorted() - Return sorted copy
print(sorted(numbers))      # [1, 1, 2, 3, 4, 5, 6, 9]

# reversed() - Return reversed iterator
print(list(reversed(numbers)))  # [6, 2, 9, 5, 1, 4, 1, 3]

# any() - True if any element is True
print(any([False, False, True]))    # True
print(any([False, False, False]))   # False

# all() - True if all elements are True
print(all([True, True, True]))      # True
print(all([True, False, True]))     # False
```

## 📊 2D Lists (Lists of Lists)

### Creating 2D Lists

```python
# Matrix (2D list)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access elements
print(matrix[0])            # [1, 2, 3] (first row)
print(matrix[0][0])         # 1 (first row, first column)
print(matrix[1][2])         # 6 (second row, third column)

# Modify elements
matrix[0][0] = 10
print(matrix[0])            # [10, 2, 3]
```

### Iterating 2D Lists

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Iterate rows
for row in matrix:
    print(row)

# Iterate all elements
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
# Output:
# 1 2 3
# 4 5 6
# 7 8 9

# With indices
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"[{i}][{j}] = {matrix[i][j]}")
```

## 🎨 Common List Patterns

### Filtering

```python
# Get positive numbers
numbers = [-2, 5, -8, 10, -3, 7]
positive = []
for num in numbers:
    if num > 0:
        positive.append(num)
print(positive)             # [5, 10, 7]

# List comprehension version
positive = [num for num in numbers if num > 0]
```

### Mapping (Transforming)

```python
# Square all numbers
numbers = [1, 2, 3, 4, 5]
squares = []
for num in numbers:
    squares.append(num ** 2)
print(squares)              # [1, 4, 9, 16, 25]

# List comprehension version
squares = [num**2 for num in numbers]
```

### Finding

```python
# Find first even number
numbers = [1, 3, 5, 8, 9, 11]
for num in numbers:
    if num % 2 == 0:
        print(f"Found: {num}")
        break
# Output: Found: 8

# Find all positions of a value
numbers = [1, 2, 3, 2, 4, 2, 5]
positions = []
for i, num in enumerate(numbers):
    if num == 2:
        positions.append(i)
print(positions)            # [1, 3, 5]
```

### Accumulation

```python
# Running total
numbers = [1, 2, 3, 4, 5]
running_totals = []
total = 0
for num in numbers:
    total += num
    running_totals.append(total)
print(running_totals)       # [1, 3, 6, 10, 15]
```

## 📚 Mini-Programs in This Folder

Apply these concepts in the following programs:

1. **01_list_basics.py** - List creation and basic operations
   - Create and initialize lists
   - Access list elements using indexing
   - Modify list elements
   - Understand list mutability vs string immutability

2. **02_list_methods.py** - Built-in list methods
   - Add elements (append, insert, extend)
   - Remove elements (remove, pop, clear)
   - Sort and reverse lists
   - Search for elements (index, count, in)
   - Copy lists properly

3. **03_list_operations.py** - List operations and slicing
   - Concatenate lists with +
   - Repeat lists with *
   - Extract sublists using slicing
   - Use built-in functions (sum, max, min, len)

4. **04_list_iteration.py** - Iterate through and process lists
   - Loop through list elements
   - Use enumerate() for index and value
   - Create new lists from existing ones
   - Perform calculations on list data
   - Filter and transform lists

## 📋 List Methods Quick Reference

### Adding Elements
- `.append(item)` - Add item to end
- `.insert(index, item)` - Insert item at position
- `.extend(iterable)` - Add all items from iterable

### Removing Elements
- `.remove(item)` - Remove first occurrence of item
- `.pop([index])` - Remove and return item at index (default: -1)
- `.clear()` - Remove all items

### Searching
- `.index(item)` - Find index of first occurrence
- `.count(item)` - Count occurrences
- `in` / `not in` - Check membership

### Ordering
- `.sort()` - Sort in place
- `.reverse()` - Reverse in place
- `.copy()` - Create shallow copy

### Built-in Functions
- `len(list)` - Number of items
- `min(list)` - Minimum value
- `max(list)` - Maximum value
- `sum(list)` - Sum of items
- `sorted(list)` - Return sorted copy
- `reversed(list)` - Return reversed iterator

## 💡 Quick Tips

✅ **Best Practices:**
- Use `.append()` to add single items
- Use `.extend()` or `+` to combine lists
- Use list comprehensions for simple transformations
- Use `enumerate()` when you need both index and value
- Use `.copy()` or `[:]` to create independent copies
- Use `in` to check membership
- Use built-in functions (sum, max, min) when possible

❌ **Common Mistakes:**
- Using `=` to copy (creates reference, not copy!)
- Modifying list while iterating over it
- Confusing `.append()` (adds single item) with `.extend()` (adds multiple)
- Index out of range errors
- Forgetting lists are mutable (changes affect all references)
- Using `.sort()` when you need `.sorted()` (or vice versa)

## 🎓 Key Takeaways

1. Lists store ordered collections of items
2. Lists are mutable (can be changed)
3. Index from 0 (or -1 from the end)
4. Slice with `[start:stop:step]`
5. Many built-in methods for common operations
6. Use `.copy()` or `[:]` to create independent copies
7. List comprehensions provide concise syntax
8. Use `enumerate()` for index and value together
9. Built-in functions: len, min, max, sum, sorted
10. Lists can contain any type, including other lists

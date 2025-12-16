# Loops and Iteration

## 📖 What Are Loops?

**Loops** are programming structures that repeat a block of code multiple times. Instead of writing the same code over and over, you use loops to automate repetition.

### Understanding Loops

- Loops execute a block of code **repeatedly**
- Each execution is called an **iteration**
- Loops continue until a **condition** is met (or a sequence ends)
- Essential for processing collections, counting, and repetitive tasks

### Why Use Loops?

✅ **Avoid repetition** - Write code once, execute many times  
✅ **Process collections** - Iterate through lists, strings, etc.  
✅ **Automate counting** - Count up, down, or in steps  
✅ **Accumulate values** - Calculate sums, products, etc.  
✅ **Search and filter** - Find items that match criteria  

## 🔄 For Loops

### Basic For Loop Syntax

```python
# Basic for loop with range
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4

# For loop with list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output: apple, banana, cherry

# For loop with string
for char in "Python":
    print(char)
# Output: P, y, t, h, o, n
```

### The range() Function

The `range()` function generates a sequence of numbers.

```python
# range(stop) - from 0 to stop-1
for i in range(5):
    print(i)                # 0, 1, 2, 3, 4

# range(start, stop) - from start to stop-1
for i in range(2, 6):
    print(i)                # 2, 3, 4, 5

# range(start, stop, step) - from start to stop-1, incrementing by step
for i in range(0, 10, 2):
    print(i)                # 0, 2, 4, 6, 8

# Negative step (counting backwards)
for i in range(10, 0, -1):
    print(i)                # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

# range() produces numbers on-demand (efficient for large ranges)
```

### Common For Loop Patterns

```python
# Print numbers 1 to 10
for i in range(1, 11):
    print(i)

# Print even numbers from 2 to 20
for i in range(2, 21, 2):
    print(i)

# Countdown from 10 to 1
for i in range(10, 0, -1):
    print(i)

# Iterate with index and value
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")
# Output:
# 0: apple
# 1: banana
# 2: cherry

# Better: Use enumerate()
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

## ⏸️ While Loops

### Basic While Loop Syntax

```python
# While loop continues while condition is True
count = 0
while count < 5:
    print(count)
    count += 1          # IMPORTANT: Update the condition variable!
# Output: 0, 1, 2, 3, 4

# While loop with user input
password = ""
while password != "secret":
    password = input("Enter password: ")
print("Access granted!")
```

### When to Use While vs For

```python
# ✅ Use FOR when you know the number of iterations
for i in range(10):                     # Exactly 10 times
    print(i)

# ✅ Use WHILE when the number of iterations is unknown
user_input = ""
while user_input != "quit":            # Until user types "quit"
    user_input = input("Enter command: ")

# ✅ Use WHILE for condition-based loops
number = 1
while number < 1000:                    # Until number exceeds 1000
    number *= 2
```

### Common While Loop Patterns

```python
# Counting with while
count = 1
while count <= 10:
    print(count)
    count += 1

# Countdown with while
countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1

# Accumulation with while
total = 0
number = 1
while number <= 100:
    total += number
    number += 1

# Condition-based while
number = 1
while number < 1000:
    print(number)
    number *= 2             # Double each time
```

### Infinite Loops (Be Careful!)

```python
# ❌ DANGER: Infinite loop (never stops)
while True:
    print("Forever!")       # Runs forever!

# ✅ SAFE: Infinite loop with break
while True:
    response = input("Continue? (yes/no): ")
    if response == "no":
        break               # Exit the loop
    print("Continuing...")

# ❌ DANGER: Forgetting to update condition variable
count = 0
while count < 5:
    print(count)
    # Forgot: count += 1   # Loop never ends!
```

## 🛑 Loop Control Statements

### The break Statement

Exits the loop immediately, regardless of the loop condition.

```python
# Break out of loop early
for i in range(10):
    if i == 5:
        break               # Exit loop when i is 5
    print(i)
# Output: 0, 1, 2, 3, 4

# Search with break
numbers = [3, 7, 2, 9, 4]
target = 9
for num in numbers:
    if num == target:
        print("Found!")
        break               # Stop searching once found

# While with break
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == "quit":
        break
    print(f"You entered: {user_input}")
```

### The continue Statement

Skips the rest of the current iteration and moves to the next one.

```python
# Skip certain values
for i in range(10):
    if i % 2 == 0:
        continue            # Skip even numbers
    print(i)
# Output: 1, 3, 5, 7, 9

# Process only valid inputs
for i in range(-5, 6):
    if i == 0:
        continue            # Skip zero (avoid division by zero)
    result = 10 / i
    print(f"10 / {i} = {result}")

# Filter during iteration
words = ["apple", "ab", "banana", "cd", "cherry"]
for word in words:
    if len(word) < 3:
        continue            # Skip short words
    print(word)
# Output: apple, banana, cherry
```

### The else Clause in Loops

The `else` block executes when the loop completes normally (not via `break`).

```python
# else with for loop
for i in range(5):
    print(i)
else:
    print("Loop completed!")
# Output: 0, 1, 2, 3, 4, Loop completed!

# else doesn't execute if break is used
for i in range(10):
    if i == 5:
        break
    print(i)
else:
    print("Loop completed!")    # This won't print
# Output: 0, 1, 2, 3, 4

# Practical use: Search pattern
numbers = [1, 3, 5, 7, 9]
target = 4
for num in numbers:
    if num == target:
        print("Found!")
        break
else:
    print("Not found!")         # Executes only if not found
# Output: Not found!
```

## 🔁 Nested Loops

Loops inside other loops - useful for multi-dimensional data or patterns.

```python
# Simple nested loop
for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")
# Output:
# i=0, j=0
# i=0, j=1
# i=0, j=2
# i=1, j=0
# ... and so on

# Multiplication table
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j}")

# Print a grid pattern
for row in range(5):
    for col in range(5):
        print("*", end=" ")
    print()                     # Newline after each row
# Output:
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# Triangle pattern
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()
# Output:
# *
# * *
# * * *
# * * * *
# * * * * *
```

## 📊 Accumulation Patterns

### Sum Accumulation

```python
# Calculate sum of numbers 1 to 100
total = 0
for i in range(1, 101):
    total += i                  # Accumulate sum
print(total)                    # 5050

# Sum of list elements
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
print(total)                    # 150

# Or use built-in sum()
print(sum(numbers))             # 150
```

### Product Accumulation

```python
# Calculate factorial (5! = 5 * 4 * 3 * 2 * 1)
n = 5
product = 1                     # Start with 1 for multiplication
for i in range(1, n + 1):
    product *= i
print(product)                  # 120
```

### Counting Accumulation

```python
# Count how many numbers are even
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
for num in numbers:
    if num % 2 == 0:
        count += 1
print(f"Even numbers: {count}") # 5

# Count vowels in a string
text = "Hello World"
vowel_count = 0
for char in text.lower():
    if char in "aeiou":
        vowel_count += 1
print(vowel_count)              # 3
```

### Building Lists

```python
# Create a list of squares
squares = []
for i in range(1, 11):
    squares.append(i ** 2)
print(squares)                  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Filter a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
print(evens)                    # [2, 4, 6, 8, 10]

# List comprehension (advanced - more concise)
squares = [i**2 for i in range(1, 11)]
evens = [num for num in numbers if num % 2 == 0]
```

### Tracking Maximum/Minimum

```python
# Find maximum value
numbers = [45, 23, 67, 12, 89, 34]
max_value = numbers[0]          # Start with first element
for num in numbers:
    if num > max_value:
        max_value = num
print(max_value)                # 89

# Find minimum value
min_value = numbers[0]
for num in numbers:
    if num < min_value:
        min_value = num
print(min_value)                # 12

# Or use built-in functions
print(max(numbers))             # 89
print(min(numbers))             # 12
```

## 🔢 Loop with enumerate()

Get both index and value when iterating.

```python
# Without enumerate (manual indexing)
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# With enumerate (cleaner)
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: cherry

# Start index at 1 instead of 0
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")
# Output:
# 1: apple
# 2: banana
# 3: cherry
```

## 🎯 Loop with zip()

Iterate through multiple sequences simultaneously.

```python
# Parallel iteration
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
# Output:
# Alice is 25 years old
# Bob is 30 years old
# Charlie is 35 years old

# zip stops at shortest sequence
numbers = [1, 2, 3, 4, 5]
letters = ["a", "b", "c"]
for num, letter in zip(numbers, letters):
    print(num, letter)
# Output:
# 1 a
# 2 b
# 3 c
```

## 🎨 Common Loop Patterns

### Input Validation Loop

```python
# Keep asking until valid input
while True:
    age = int(input("Enter your age: "))
    if age > 0 and age < 120:
        break
    print("Invalid age, try again")
```

### Sentinel Loop

```python
# Loop until sentinel value
total = 0
while True:
    value = input("Enter a number (or 'done'): ")
    if value == "done":
        break
    total += int(value)
print(f"Total: {total}")
```

### Processing Each Character

```python
# Iterate through string
word = "Python"
for char in word:
    print(char)

# Count specific characters
text = "Hello World"
count = 0
for char in text:
    if char.lower() == 'l':
        count += 1
print(f"Letter 'l' appears {count} times")  # 3
```

### Matrix/Grid Processing

```python
# Process 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
# Output:
# 1 2 3
# 4 5 6
# 7 8 9
```

## 📚 Mini-Programs in This Folder

Apply these concepts in the following programs:

1. **01_counting_loops.py** - Basic loop counting and iteration
   - Use for loops with `range()`
   - Create counting sequences (forward, backward, step)
   - Work with loop variables
   - Calculate sums using accumulation

2. **02_while_loops.py** - Conditional iteration with while loops
   - Use while loops for condition-based iteration
   - Update loop variables correctly
   - Know when to use while vs for loops
   - Implement counting and accumulation patterns

3. **03_loop_patterns.py** - Create visual patterns with loops
   - Use nested loops for 2D patterns
   - Print shapes (squares, triangles, pyramids)
   - Work with characters in loops
   - Combine loops with string operations

4. **04_loop_accumulation.py** - Accumulate values using loops
   - Calculate sums and products
   - Track maximum and minimum values
   - Build lists using loops
   - Count elements matching criteria

## 💡 Quick Tips

✅ **Best Practices:**
- Use `for` when you know the number of iterations
- Use `while` when the number of iterations is unknown
- Always update loop variables in while loops
- Use meaningful variable names (not just `i`, `j`)
- Use `enumerate()` when you need both index and value
- Use `break` to exit early, `continue` to skip iterations
- Be careful with nested loops (can be slow for large data)

❌ **Common Mistakes:**
- Infinite loops (forgetting to update condition)
- Off-by-one errors with `range()` (remember: stop is exclusive)
- Modifying a list while iterating over it
- Using the wrong loop type (for vs while)
- Forgetting the colon (:) after for/while
- Not indenting the loop body

## 🎓 Key Takeaways

1. For loops iterate over sequences (range, lists, strings)
2. While loops continue while a condition is True
3. `range(start, stop, step)` generates number sequences
4. Use `break` to exit early, `continue` to skip iterations
5. Nested loops process multi-dimensional data
6. Accumulation patterns: sum, product, count, max/min
7. `enumerate()` provides index and value
8. `zip()` iterates multiple sequences together
9. Always update loop variables in while loops to avoid infinite loops

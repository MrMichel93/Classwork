# Strings

## 📖 What Are Strings?

A **string** is a sequence of characters used to represent text in Python. Strings are one of the most commonly used data types.

### Understanding Strings

- Strings store **text data** (letters, numbers, symbols)
- Strings are **immutable** (cannot be changed after creation)
- Strings are **sequences** (ordered collection of characters)
- Each character has an **index** (position number)

### Creating Strings

```python
# Single quotes
name = 'Alice'

# Double quotes
message = "Hello, World!"

# Triple quotes (multi-line strings)
paragraph = """This is a
multi-line
string"""

# Empty string
empty = ""

# Strings with quotes inside
quote1 = "He said, 'Hello'"
quote2 = 'She said, "Hi"'
quote3 = "Use \" to escape quotes"
```

## 🎯 String Indexing

### Accessing Characters by Index

```python
text = "Python"

# Positive indexing (from left, starts at 0)
print(text[0])      # 'P' (first character)
print(text[1])      # 'y'
print(text[5])      # 'n' (last character)

# Negative indexing (from right, starts at -1)
print(text[-1])     # 'n' (last character)
print(text[-2])     # 'o' (second to last)
print(text[-6])     # 'P' (first character)

# Index diagram:
#  P   y   t   h   o   n
#  0   1   2   3   4   5    (positive)
# -6  -5  -4  -3  -2  -1    (negative)
```

### Index Errors

```python
text = "Python"
print(text[6])      # IndexError! (valid indices are 0-5)
print(text[100])    # IndexError! (out of range)
```

## ✂️ String Slicing

Extract a portion (substring) of a string.

### Slicing Syntax

```python
# string[start:stop:step]
text = "Python Programming"

# Basic slicing [start:stop] - from start to stop-1
print(text[0:6])    # 'Python' (indices 0-5)
print(text[7:18])   # 'Programming'

# Omit start (defaults to beginning)
print(text[:6])     # 'Python' (from start to index 5)

# Omit stop (defaults to end)
print(text[7:])     # 'Programming' (from index 7 to end)

# Omit both (copy entire string)
print(text[:])      # 'Python Programming'

# Negative indices in slicing
print(text[-11:])   # 'Programming' (last 11 characters)
print(text[:-12])   # 'Python' (all but last 12 characters)

# Step (every nth character)
print(text[::2])    # 'Pto rgamn' (every 2nd character)
print(text[::3])    # 'Ph oamn' (every 3rd character)

# Reverse a string (step -1)
print(text[::-1])   # 'gnimmargorP nohtyP'
```

### Common Slicing Patterns

```python
text = "Hello World"

# First 5 characters
print(text[:5])             # 'Hello'

# Last 5 characters
print(text[-5:])            # 'World'

# All but first character
print(text[1:])             # 'ello World'

# All but last character
print(text[:-1])            # 'Hello Worl'

# Middle characters
print(text[3:8])            # 'lo Wo'

# Every other character
print(text[::2])            # 'HloWrd'

# Reverse string
print(text[::-1])           # 'dlroW olleH'
```

## 🔧 String Methods

Strings have many built-in methods. Remember: strings are **immutable**, so methods return new strings.

### Case Conversion Methods

```python
text = "Hello World"

# Convert to uppercase
print(text.upper())         # 'HELLO WORLD'

# Convert to lowercase
print(text.lower())         # 'hello world'

# Title case (capitalize each word)
print(text.title())         # 'Hello World'

# Capitalize first character only
print(text.capitalize())    # 'Hello world'

# Swap case (upper ↔ lower)
print(text.swapcase())      # 'hELLO wORLD'

# Note: Original string is unchanged
print(text)                 # 'Hello World'
```

### Searching Methods

```python
text = "Python Programming"

# Check if string starts with substring
print(text.startswith("Python"))    # True
print(text.startswith("Java"))      # False

# Check if string ends with substring
print(text.endswith("ing"))         # True
print(text.endswith("ed"))          # False

# Find position of substring (returns index or -1)
print(text.find("Pro"))             # 7 (starting index)
print(text.find("Java"))            # -1 (not found)

# Find from right
print(text.rfind("o"))              # 9 (last 'o')

# Index of substring (raises error if not found)
print(text.index("Pro"))            # 7
# print(text.index("Java"))         # ValueError!

# Check if substring exists
print("Pro" in text)                # True
print("Java" in text)               # False
print("Pro" not in text)            # False
```

### Counting and Checking

```python
text = "Hello World"

# Count occurrences of substring
print(text.count("l"))              # 3
print(text.count("lo"))             # 1
print(text.count("x"))              # 0

# Length of string
print(len(text))                    # 11

# Check string characteristics
print("hello".isalpha())            # True (all letters)
print("hello123".isalpha())         # False (has numbers)
print("123".isdigit())              # True (all digits)
print("hello123".isalnum())         # True (letters and/or numbers)
print("hello world".isalnum())      # False (has space)
print("hello".islower())            # True (all lowercase)
print("HELLO".isupper())            # True (all uppercase)
print("   ".isspace())              # True (all whitespace)
```

### Replacing and Modifying

```python
text = "Hello World"

# Replace substring
print(text.replace("World", "Python"))      # 'Hello Python'
print(text.replace("l", "L"))               # 'HeLLo WorLd'

# Replace with limit
print(text.replace("l", "L", 2))            # 'HeLLo World' (only first 2)

# Remove whitespace
text = "  Hello World  "
print(text.strip())                         # 'Hello World' (both ends)
print(text.lstrip())                        # 'Hello World  ' (left)
print(text.rstrip())                        # '  Hello World' (right)

# Strip specific characters
text = "...Hello..."
print(text.strip("."))                      # 'Hello'

# Note: Original strings are unchanged!
```

### Splitting and Joining

```python
# Split string into list
text = "apple,banana,orange"
fruits = text.split(",")
print(fruits)                       # ['apple', 'banana', 'orange']

# Split on whitespace (default)
sentence = "Hello World Python"
words = sentence.split()
print(words)                        # ['Hello', 'World', 'Python']

# Split with limit
text = "a-b-c-d-e"
print(text.split("-", 2))          # ['a', 'b', 'c-d-e'] (max 2 splits)

# Join list into string
words = ["Hello", "World", "Python"]
print(" ".join(words))              # 'Hello World Python'
print("-".join(words))              # 'Hello-World-Python'
print("".join(words))               # 'HelloWorldPython'

# Join only works with strings
numbers = [1, 2, 3]
# print("".join(numbers))           # Error! Need strings
print("".join(str(n) for n in numbers))  # '123'
```

### Alignment and Padding

```python
text = "Hello"

# Center text (width 20)
print(text.center(20))              # '       Hello        '
print(text.center(20, "-"))         # '-------Hello--------'

# Left align
print(text.ljust(20))               # 'Hello               '
print(text.ljust(20, "*"))          # 'Hello***************'

# Right align
print(text.rjust(20))               # '               Hello'
print(text.rjust(20, "*"))          # '***************Hello'

# Zero padding (for numbers)
print("42".zfill(5))                # '00042'
print("-42".zfill(5))               # '-0042'
```

## 🔤 String Operators

### Concatenation (+)

```python
# Combine strings
first = "Hello"
last = "World"
full = first + " " + last           # 'Hello World'

# Multiple concatenations
greeting = "Hello" + " " + "there" + " " + "friend"
```

### Repetition (*)

```python
# Repeat strings
print("Ha" * 3)                     # 'HaHaHa'
print("=" * 20)                     # '===================='
print("-" * 10)                     # '----------'

# Useful for formatting
line = "=" * 40
print(line)
print("Title")
print(line)
```

### Membership (in, not in)

```python
# Check if substring exists
text = "Python Programming"
print("Python" in text)             # True
print("Java" in text)               # False
print("Java" not in text)           # True

# Case-sensitive
print("python" in text)             # False (lowercase)
print("python" in text.lower())     # True (after converting)
```

## 📝 String Formatting

### f-strings (Formatted String Literals)

```python
# Basic f-string
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old")

# Expressions in f-strings
x = 10
y = 5
print(f"{x} + {y} = {x + y}")       # '10 + 5 = 15'

# Format numbers
price = 19.99
print(f"Price: ${price:.2f}")       # 'Price: $19.99' (2 decimals)

pi = 3.14159
print(f"Pi: {pi:.3f}")              # 'Pi: 3.142' (3 decimals)

# Alignment in f-strings
name = "Alice"
print(f"{name:>10}")                # '     Alice' (right align, width 10)
print(f"{name:<10}")                # 'Alice     ' (left align, width 10)
print(f"{name:^10}")                # '  Alice   ' (center, width 10)
```

### format() Method

```python
# Basic format
name = "Alice"
age = 25
print("My name is {} and I am {} years old".format(name, age))

# With indices
print("{0} + {1} = {2}".format(10, 5, 15))

# With names
print("My name is {n} and I am {a} years old".format(n=name, a=age))
```

### Old-style % Formatting

```python
# Still seen in older code
name = "Alice"
age = 25
print("My name is %s and I am %d years old" % (name, age))
```

## 🔄 String Iteration

### Loop Through Characters

```python
# Basic iteration
text = "Python"
for char in text:
    print(char)
# Output: P, y, t, h, o, n

# With index using enumerate
for i, char in enumerate(text):
    print(f"{i}: {char}")
# Output:
# 0: P
# 1: y
# 2: t
# 3: h
# 4: o
# 5: n

# Count specific characters
text = "Hello World"
count = 0
for char in text:
    if char.lower() == 'l':
        count += 1
print(count)                        # 3
```

### Building Strings in Loops

```python
# Build new string from existing one
text = "Hello"
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print(reversed_text)                # 'olleH'

# Filter characters
text = "Hello123World456"
letters_only = ""
for char in text:
    if char.isalpha():
        letters_only += char
print(letters_only)                 # 'HelloWorld'

# Convert to uppercase character by character
text = "hello"
upper_text = ""
for char in text:
    upper_text += char.upper()
print(upper_text)                   # 'HELLO'
```

## 🔒 String Immutability

Strings cannot be modified after creation. You must create new strings.

```python
text = "Hello"

# ❌ Cannot modify individual characters
# text[0] = "h"                     # TypeError!

# ✅ Create new string instead
text = "h" + text[1:]               # 'hello'

# Methods return NEW strings
original = "hello"
upper = original.upper()
print(original)                     # 'hello' (unchanged)
print(upper)                        # 'HELLO' (new string)
```

## 🎨 Escape Characters

Special characters in strings.

```python
# Common escape characters
print("Hello\nWorld")               # \n = newline
print("Hello\tWorld")               # \t = tab
print("He said, \"Hi\"")            # \" = quote
print("Path: C:\\Users\\Name")      # \\ = backslash

# Raw strings (ignore escape characters)
print(r"C:\Users\Name")             # r prefix = raw string
```

## 📚 Mini-Programs in This Folder

Apply these concepts in the following programs:

1. **01_string_basics.py** - String creation and manipulation
   - Create and initialize strings
   - Use string indexing to access characters
   - Use string slicing to extract substrings
   - Concatenate strings

2. **02_string_methods.py** - Built-in string methods
   - Transform strings (upper, lower, title, capitalize)
   - Search within strings (find, index, in operator)
   - Replace and split strings
   - Use string checking methods (startswith, endswith, etc.)

3. **03_string_formatting.py** - Format strings with f-strings
   - Create dynamic string output
   - Format numbers in strings
   - Combine variables in strings
   - Align and pad strings

4. **04_string_iteration.py** - Iterate through and analyze strings
   - Loop through string characters
   - Count specific characters
   - Build new strings from existing ones
   - Process each character

## 📋 String Methods Quick Reference

### Case Methods
- `.upper()` - Convert to uppercase
- `.lower()` - Convert to lowercase
- `.title()` - Title case (each word capitalized)
- `.capitalize()` - Capitalize first character only
- `.swapcase()` - Swap upper/lower case

### Search Methods
- `.startswith(sub)` - Check if starts with substring
- `.endswith(sub)` - Check if ends with substring
- `.find(sub)` - Find index of substring (-1 if not found)
- `.rfind(sub)` - Find from right
- `.index(sub)` - Like find but raises error if not found
- `.count(sub)` - Count occurrences of substring

### Check Methods
- `.isalpha()` - All alphabetic characters
- `.isdigit()` - All digits
- `.isalnum()` - All alphanumeric
- `.isspace()` - All whitespace
- `.islower()` - All lowercase
- `.isupper()` - All uppercase

### Modify Methods
- `.replace(old, new)` - Replace substring
- `.strip()` - Remove whitespace from both ends
- `.lstrip()` - Remove whitespace from left
- `.rstrip()` - Remove whitespace from right
- `.split(sep)` - Split into list
- `.join(list)` - Join list into string

### Alignment Methods
- `.center(width)` - Center align
- `.ljust(width)` - Left align
- `.rjust(width)` - Right align
- `.zfill(width)` - Pad with zeros

## 💡 Quick Tips

✅ **Best Practices:**
- Use f-strings for formatting (Python 3.6+)
- Use `.lower()` for case-insensitive comparisons
- Use `in` to check for substrings
- Use `.strip()` to clean user input
- Use `.split()` and `.join()` for word processing
- Build strings efficiently (join list vs concatenation in loops)

❌ **Common Mistakes:**
- Trying to modify strings (they're immutable!)
- Forgetting strings are 0-indexed
- Using `+` in loops (slow for many concatenations)
- Confusing `.find()` (returns -1) with `.index()` (raises error)
- Not handling case in comparisons
- Off-by-one errors with slicing

## 🎓 Key Takeaways

1. Strings are sequences of characters (immutable)
2. Index from 0 (or -1 from the end)
3. Slice with `[start:stop:step]`
4. Many built-in methods for common operations
5. Methods return NEW strings (immutable!)
6. Use f-strings for formatting
7. Use `in` to check for substrings
8. Iterate with `for char in string:`

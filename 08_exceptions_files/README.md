# Exceptions and Files

## 📖 What Are Exceptions?

**Exceptions** are errors that occur during program execution. Instead of crashing, Python allows you to "catch" these errors and handle them gracefully. **File operations** let you read from and write to files on your computer.

### Understanding Exceptions and Files

- **Exceptions** interrupt normal program flow when errors occur
- **Exception handling** lets you respond to errors instead of crashing
- **Files** store data persistently on disk
- Python provides tools to safely read, write, and manipulate files
- Proper error handling makes programs robust and user-friendly

### Why Handle Exceptions and Work with Files?

✅ **Graceful errors** - Programs don't crash, show helpful messages instead  
✅ **User-friendly** - Handle invalid input without terminating  
✅ **Data persistence** - Save and load data between program runs  
✅ **Debugging** - Understand what went wrong and where  
✅ **Robust code** - Handle edge cases and unexpected situations  

## 🚨 Understanding Exceptions

### What Causes Exceptions?

```python
# Common exceptions

# ZeroDivisionError - dividing by zero
result = 10 / 0

# ValueError - invalid value for operation
number = int("abc")

# IndexError - accessing invalid list index
my_list = [1, 2, 3]
print(my_list[10])

# KeyError - accessing non-existent dictionary key
my_dict = {"a": 1}
print(my_dict["b"])

# FileNotFoundError - opening non-existent file
file = open("nonexistent.txt")

# TypeError - operation on incompatible types
result = "hello" + 5

# AttributeError - accessing non-existent attribute
text = "hello"
text.nonexistent_method()
```

### Common Exception Types

```python
# Built-in exception hierarchy (most common ones)

# Exception (base class for most exceptions)
# ├── ArithmeticError
# │   ├── ZeroDivisionError
# │   └── OverflowError
# ├── LookupError
# │   ├── IndexError
# │   └── KeyError
# ├── ValueError
# ├── TypeError
# ├── FileNotFoundError
# ├── PermissionError
# ├── AttributeError
# └── NameError
```

## 🛡️ Exception Handling

### The try-except Block

```python
# Basic try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
    result = None

print("Program continues...")

# Without exception handling (program crashes)
# result = 10 / 0  # Crash! Program stops here
# print("This never prints")
```

### Catching Specific Exceptions

```python
# Catch specific exception types
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

### Catching Multiple Exceptions

```python
# Multiple exceptions in one except clause
try:
    numbers = [1, 2, 3]
    index = int(input("Enter index: "))
    print(numbers[index])
except (ValueError, IndexError):
    print("Invalid input or index!")

# Or handle separately
try:
    numbers = [1, 2, 3]
    index = int(input("Enter index: "))
    print(numbers[index])
except ValueError:
    print("Please enter a valid number!")
except IndexError:
    print("Index out of range!")
```

### Getting Exception Information

```python
# Capture exception object for more info
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error occurred: {e}")
    print(f"Error type: {type(e).__name__}")

# General exception handler (catches any exception)
try:
    result = int("abc") + [1, 2]
except Exception as e:
    print(f"An error occurred: {type(e).__name__}")
    print(f"Details: {e}")
```

### The else Clause

```python
# else runs only if NO exception occurs
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("Invalid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    # Only runs if no exception
    print(f"Result: {result}")
    print("Calculation successful!")
```

### The finally Clause

```python
# finally ALWAYS runs (exception or not)
try:
    file = open("data.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    # This always runs - good for cleanup
    print("Cleanup code runs here")
    # file.close() if file exists

# Common pattern: resource cleanup
try:
    # Open resource
    connection = connect_to_database()
    # Use resource
    data = connection.fetch_data()
except Exception as e:
    print(f"Error: {e}")
finally:
    # Always close resource
    connection.close()
```

### Complete try-except-else-finally

```python
# All clauses together
try:
    # Code that might raise exception
    number = int(input("Enter number: "))
    result = 10 / number
except ValueError:
    # Runs if ValueError occurs
    print("Invalid input!")
except ZeroDivisionError:
    # Runs if ZeroDivisionError occurs
    print("Cannot divide by zero!")
else:
    # Runs if NO exception occurs
    print(f"Result: {result}")
finally:
    # ALWAYS runs
    print("Operation complete")
```

## 🔥 Raising Exceptions

### The raise Statement

```python
# Raise an exception manually
def check_positive(number):
    if number < 0:
        raise ValueError("Number must be positive!")
    return number

try:
    check_positive(-5)
except ValueError as e:
    print(e)  # "Number must be positive!"

# Raise without message
def validate_age(age):
    if age < 0 or age > 120:
        raise ValueError
    return age
```

### Re-raising Exceptions

```python
# Catch, log, then re-raise
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Logging error...")
    raise  # Re-raise the same exception
```

### Custom Exceptions

```python
# Create custom exception classes
class InvalidAgeError(Exception):
    """Custom exception for invalid ages"""
    pass

def set_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(f"Invalid age: {age}")
    return age

try:
    set_age(-5)
except InvalidAgeError as e:
    print(e)  # "Invalid age: -5"

# Custom exception with additional attributes
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        message = f"Insufficient funds: balance=${balance}, needed=${amount}"
        super().__init__(message)

try:
    raise InsufficientFundsError(50, 100)
except InsufficientFundsError as e:
    print(e)
    print(f"Short by: ${e.amount - e.balance}")
```

## 📁 Working with Files

### Opening Files

```python
# open(filename, mode)
# Modes:
# 'r' - read (default)
# 'w' - write (overwrites existing file)
# 'a' - append (adds to end of file)
# 'x' - create (fails if file exists)
# 'r+' - read and write
# 'b' - binary mode (e.g., 'rb', 'wb')

# Basic file opening
file = open("data.txt", "r")
content = file.read()
file.close()  # Always close files!

# File opening can fail
try:
    file = open("nonexistent.txt", "r")
except FileNotFoundError:
    print("File not found!")
```

### The with Statement (Context Manager)

```python
# Best practice: use 'with' (automatically closes file)
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
# File is automatically closed here

# Compare without 'with' (manual close)
file = open("data.txt", "r")
try:
    content = file.read()
finally:
    file.close()  # Must manually close

# Multiple files with 'with'
with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    content = infile.read()
    outfile.write(content.upper())
```

## 📖 Reading Files

### Reading Methods

```python
# read() - Read entire file as single string
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

# read(n) - Read n characters
with open("data.txt", "r") as file:
    first_10 = file.read(10)  # Read first 10 characters

# readline() - Read one line
with open("data.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()

# readlines() - Read all lines as list
with open("data.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # strip() removes newline

# Iterate line by line (memory efficient)
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())
```

### Reading with Exception Handling

```python
# Safe file reading
def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"File '{filename}' not found")
        return None
    except PermissionError:
        print(f"No permission to read '{filename}'")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

content = read_file("data.txt")
if content:
    print(content)
```

## ✍️ Writing Files

### Writing Methods

```python
# write() - Write string to file
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is line 2\n")

# writelines() - Write list of strings
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)

# Note: write() and writelines() don't add newlines automatically
with open("output.txt", "w") as file:
    file.write("Line 1")
    file.write("Line 2")  # Writes: "Line 1Line 2"

with open("output.txt", "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")  # Writes two lines
```

### Append Mode

```python
# 'a' mode - append to end of file
with open("log.txt", "a") as file:
    file.write("New log entry\n")

# Append doesn't erase existing content
with open("data.txt", "w") as file:
    file.write("Original content\n")

with open("data.txt", "a") as file:
    file.write("Appended content\n")

# Result: both lines in file
```

### Write Mode Overwrites!

```python
# 'w' mode - OVERWRITES entire file!
with open("data.txt", "w") as file:
    file.write("New content")
# Previous file content is GONE!

# Safe writing with exception handling
def write_file(filename, content):
    try:
        with open(filename, "w") as file:
            file.write(content)
        return True
    except PermissionError:
        print(f"No permission to write to '{filename}'")
        return False
    except Exception as e:
        print(f"Error writing file: {e}")
        return False
```

## 📊 Working with File Paths

### Path Operations

```python
import os

# Check if file exists
if os.path.exists("data.txt"):
    print("File exists")

# Check if path is file or directory
print(os.path.isfile("data.txt"))       # True if file
print(os.path.isdir("my_folder"))       # True if directory

# Get file size
size = os.path.getsize("data.txt")
print(f"File size: {size} bytes")

# Get absolute path
abs_path = os.path.abspath("data.txt")
print(abs_path)

# Join paths (works on all operating systems)
path = os.path.join("folder", "subfolder", "file.txt")
# Windows: folder\subfolder\file.txt
# Unix/Mac: folder/subfolder/file.txt

# Split path into directory and filename
directory, filename = os.path.split("/path/to/file.txt")
# directory: '/path/to'
# filename: 'file.txt'

# Get file extension
name, ext = os.path.splitext("data.txt")
# name: 'data'
# ext: '.txt'
```

## 📦 Working with JSON Files

### JSON Basics

```python
import json

# Python dict to JSON string
data = {
    "name": "Alice",
    "age": 25,
    "skills": ["Python", "Java", "SQL"]
}

json_string = json.dumps(data)
print(json_string)
# '{"name": "Alice", "age": 25, "skills": ["Python", "Java", "SQL"]}'

# JSON string to Python dict
json_string = '{"name": "Bob", "age": 30}'
data = json.loads(json_string)
print(data["name"])  # "Bob"
```

### Reading JSON Files

```python
import json

# Read JSON from file
try:
    with open("data.json", "r") as file:
        data = json.load(file)
        print(data)
except FileNotFoundError:
    print("JSON file not found")
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")

# Pretty print JSON
with open("data.json", "r") as file:
    data = json.load(file)
    print(json.dumps(data, indent=4))
```

### Writing JSON Files

```python
import json

# Write Python data as JSON
data = {
    "users": [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30}
    ],
    "total": 2
}

# Write to file
with open("output.json", "w") as file:
    json.dump(data, file, indent=4)

# Without indentation (compact)
with open("output.json", "w") as file:
    json.dump(data, file)
```

### JSON with Lists and Complex Data

```python
import json

# List of dictionaries
students = [
    {"name": "Alice", "grades": [90, 85, 88]},
    {"name": "Bob", "grades": [75, 80, 85]},
    {"name": "Charlie", "grades": [95, 92, 98]}
]

# Save to JSON
with open("students.json", "w") as file:
    json.dump(students, file, indent=2)

# Load from JSON
with open("students.json", "r") as file:
    loaded_students = json.load(file)
    for student in loaded_students:
        print(f"{student['name']}: {student['grades']}")
```

## 🎯 Common File Patterns

### Reading CSV-like Data

```python
# Read CSV-like data (comma-separated)
with open("data.csv", "r") as file:
    for line in file:
        # Split by comma and strip whitespace
        values = [v.strip() for v in line.split(",")]
        print(values)

# Skip header row
with open("data.csv", "r") as file:
    header = file.readline()  # Skip first line
    for line in file:
        values = line.strip().split(",")
        print(values)
```

### Counting Lines, Words, Characters

```python
# Count lines in file
with open("data.txt", "r") as file:
    line_count = len(file.readlines())
print(f"Lines: {line_count}")

# Count words in file
with open("data.txt", "r") as file:
    word_count = 0
    for line in file:
        words = line.split()
        word_count += len(words)
print(f"Words: {word_count}")

# Count characters in file
with open("data.txt", "r") as file:
    char_count = len(file.read())
print(f"Characters: {char_count}")
```

### Safe File Operations

```python
# Check before writing
import os

def safe_write(filename, content):
    """Write to file only if it doesn't exist"""
    if os.path.exists(filename):
        response = input(f"{filename} exists. Overwrite? (y/n): ")
        if response.lower() != 'y':
            print("Write cancelled")
            return False
    
    try:
        with open(filename, "w") as file:
            file.write(content)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

# Backup before modifying
def safe_modify(filename):
    """Create backup before modifying file"""
    if os.path.exists(filename):
        # Create backup
        backup = filename + ".bak"
        with open(filename, "r") as original:
            with open(backup, "w") as backup_file:
                backup_file.write(original.read())
        print(f"Backup created: {backup}")
```

## 📚 Mini-Programs in This Folder

Apply these concepts in the following programs:

1. **01_exception_handling.py** - Exception handling basics
   - Use try-except blocks to handle errors
   - Catch specific exception types (ValueError, ZeroDivisionError, IndexError)
   - Use try-except-else-finally structure
   - Create functions with exception handling
   - Raise exceptions manually
   - Work with exception messages

2. **02_file_reading.py** - Reading files in Python
   - Open and read files with context managers
   - Use different reading methods (read, readline, readlines)
   - Iterate through file line by line
   - Handle FileNotFoundError
   - Read and process file data
   - Close files properly

3. **03_file_writing.py** - Writing data to files
   - Write strings to files in write mode
   - Append data to existing files
   - Write lists to files
   - Use writelines() method
   - Handle write errors with try-except
   - Understand difference between 'w' and 'a' modes

4. **04_json_files.py** - Working with JSON data
   - Parse JSON strings with json.loads()
   - Generate JSON with json.dumps()
   - Read JSON files with json.load()
   - Write JSON files with json.dump()
   - Handle JSON decode errors
   - Work with nested JSON structures

## 💡 Quick Tips

✅ **Best Practices:**
- Always use `with` statement for files (automatic cleanup)
- Be specific with exceptions (catch ValueError, not Exception)
- Always close files if not using `with`
- Handle exceptions at the appropriate level
- Use meaningful error messages
- Check if file exists before operations
- Create backups before modifying important files

❌ **Common Mistakes:**
- Not closing files (use `with` to avoid this)
- Catching all exceptions with bare `except:` (hides bugs)
- Opening files in 'w' mode accidentally (overwrites content!)
- Not handling FileNotFoundError when reading
- Forgetting to strip newlines when reading lines
- Using relative paths without checking working directory
- Not handling JSON decode errors

## 🎓 Key Takeaways

1. Exceptions are errors that occur during program execution
2. Use try-except to handle exceptions gracefully
3. Specific exception handling is better than catching all exceptions
4. finally clause always runs (good for cleanup)
5. else clause runs only if no exception occurs
6. Use `with` statement for automatic file cleanup
7. File modes: 'r' (read), 'w' (write), 'a' (append)
8. 'w' mode overwrites files - use carefully!
9. JSON is great for storing structured data
10. Always validate and handle file operations with exceptions

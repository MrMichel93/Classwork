# Functions

## 📖 What Are Functions?

A **function** is a reusable block of code that performs a specific task. Functions help you organize code, avoid repetition, and make programs easier to understand and maintain.

### Understanding Functions

- Functions are like **mini-programs** within your program
- They take **inputs** (parameters), perform actions, and can return **outputs**
- You **define** a function once and can **call** it many times
- Functions promote **code reuse** and **modularity**

### Why Use Functions?

✅ **Avoid repetition** - Write code once, use it many times  
✅ **Organize code** - Break complex programs into smaller, manageable pieces  
✅ **Easier testing** - Test individual functions separately  
✅ **Easier maintenance** - Fix bugs in one place  
✅ **Readability** - Descriptive function names make code self-documenting  

## 🎯 Basic Syntax

### Defining a Function

```python
# Basic function definition
def greet():
    """This is a docstring - describes what the function does"""
    print("Hello, World!")

# Function with parameters
def greet_person(name):
    """Greet a person by name"""
    print(f"Hello, {name}!")

# Function with return value
def add(a, b):
    """Add two numbers and return the result"""
    return a + b
```

### Function Components

```python
def function_name(parameter1, parameter2):
    """Docstring: describes the function (optional but recommended)"""
    # Function body: code that runs when function is called
    result = parameter1 + parameter2
    return result  # Return value (optional)

# Breakdown:
# - def: keyword to define a function
# - function_name: name of the function (use snake_case)
# - (parameters): inputs the function accepts (optional)
# - :: required at the end of the def line
# - Indented block: the function body
# - return: sends a value back to the caller (optional)
```

## 📞 Calling Functions

### Basic Function Calls

```python
# Define a function
def say_hello():
    print("Hello!")

# Call the function
say_hello()         # Output: Hello!

# Call multiple times
say_hello()         # Output: Hello!
say_hello()         # Output: Hello!
```

### Functions with Arguments

```python
# Define function with parameters
def greet(name):
    print(f"Hello, {name}!")

# Call with argument
greet("Alice")      # Output: Hello, Alice!
greet("Bob")        # Output: Hello, Bob!

# Multiple parameters
def introduce(name, age):
    print(f"My name is {name} and I'm {age} years old")

introduce("Alice", 25)      # Output: My name is Alice and I'm 25 years old
```

## 🔄 Return Values

### The return Statement

```python
# Function that returns a value
def add(a, b):
    result = a + b
    return result

# Use the return value
sum_result = add(5, 3)      # sum_result = 8
print(sum_result)            # Output: 8

# Can use return value directly
print(add(10, 20))           # Output: 30
```

### Multiple Return Statements

```python
# Function can have multiple return statements
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"
    # When a return is executed, function exits immediately

grade = get_grade(85)       # grade = "B"
```

### Returning Multiple Values

```python
# Return multiple values as a tuple
def get_dimensions():
    length = 10
    width = 5
    height = 3
    return length, width, height

# Unpack the return values
l, w, h = get_dimensions()  # l=10, w=5, h=3

# Or get as a tuple
dimensions = get_dimensions()  # dimensions = (10, 5, 3)
```

### Functions Without Return

```python
# Function without return statement returns None
def say_hello():
    print("Hello!")
    # No return statement

result = say_hello()        # Prints "Hello!"
print(result)               # Output: None

# Explicit return None
def do_nothing():
    return None             # Optional - same as no return

# Early return without value
def validate_age(age):
    if age < 0:
        return              # Returns None and exits early
    print(f"Valid age: {age}")
```

## 📥 Parameters and Arguments

### Understanding the Difference

- **Parameter**: Variable in the function definition
- **Argument**: Actual value passed when calling the function

```python
def greet(name):        # 'name' is a parameter
    print(f"Hello, {name}")

greet("Alice")          # "Alice" is an argument
```

### Positional Arguments

```python
# Arguments matched by position
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}")

describe_pet("dog", "Buddy")        # animal_type="dog", pet_name="Buddy"
describe_pet("Buddy", "dog")        # Wrong order! animal_type="Buddy", pet_name="dog"
```

### Keyword Arguments

```python
# Arguments matched by name
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}")

# Order doesn't matter with keyword arguments
describe_pet(animal_type="dog", pet_name="Buddy")
describe_pet(pet_name="Buddy", animal_type="dog")   # Same result

# Mix positional and keyword (positional must come first)
describe_pet("dog", pet_name="Buddy")               # OK
describe_pet(animal_type="dog", "Buddy")            # Error! Positional after keyword
```

### Default Parameter Values

```python
# Parameters with default values
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")                      # Output: Hello, Alice!
greet("Bob", "Hi")                  # Output: Hi, Bob!
greet("Charlie", greeting="Hey")    # Output: Hey, Charlie!

# Default values must come after non-default parameters
def calculate_area(length, width=1):    # OK
    return length * width

def invalid(width=1, length):           # Error! Non-default after default
    return length * width
```

### Arbitrary Number of Arguments

```python
# *args: Accept any number of positional arguments (tuple)
def add_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(add_all(1, 2, 3))             # 6
print(add_all(1, 2, 3, 4, 5))       # 15

# **kwargs: Accept any number of keyword arguments (dictionary)
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")
# Output:
# name: Alice
# age: 25
# city: NYC
```

## 🔭 Scope

### Understanding Scope

**Scope** determines where a variable can be accessed in your code.

```python
# Global scope - accessible everywhere
global_var = "I'm global"

def my_function():
    # Local scope - only accessible inside this function
    local_var = "I'm local"
    print(global_var)       # Can access global variable
    print(local_var)        # Can access local variable

my_function()
print(global_var)           # OK - global variable
print(local_var)            # Error! local_var doesn't exist here
```

### Local vs Global Variables

```python
# Global variable
count = 0

def increment():
    # Create local variable (doesn't change global count)
    count = 1               # This is a NEW local variable
    print(f"Inside: {count}")

increment()                 # Output: Inside: 1
print(f"Outside: {count}")  # Output: Outside: 0 (global unchanged)

# To modify global variable, use 'global' keyword
def increment_global():
    global count            # Declare we want to use global variable
    count = count + 1
    print(f"Inside: {count}")

increment_global()          # Output: Inside: 1
print(f"Outside: {count}")  # Output: Outside: 1 (global changed)
```

### Best Practices for Scope

```python
# ✅ GOOD: Pass values as parameters, return results
def calculate_tax(amount, tax_rate):
    return amount * tax_rate

total = 100
tax = calculate_tax(total, 0.08)

# ❌ AVOID: Relying on global variables
total = 100
def calculate_tax_bad():
    global total            # Avoid this when possible
    return total * 0.08

# ✅ GOOD: Keep functions independent and testable
```

## 📝 Docstrings

### What Are Docstrings?

Docstrings are string literals that describe what a function does. They appear as the first statement in a function.

```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
    length (float): The length of the rectangle
    width (float): The width of the rectangle
    
    Returns:
    float: The area of the rectangle
    """
    return length * width

# Access docstring
print(calculate_area.__doc__)
help(calculate_area)
```

### Docstring Styles

```python
# Simple one-liner
def greet(name):
    """Greet a person by name."""
    print(f"Hello, {name}")

# Multi-line docstring
def complex_function(param1, param2):
    """
    Brief description of what the function does.
    
    More detailed explanation if needed.
    Can span multiple lines.
    
    Args:
        param1: Description of first parameter
        param2: Description of second parameter
    
    Returns:
        Description of return value
    """
    pass
```

## 🎭 Common Function Patterns

### Validation Functions

```python
# Return boolean to indicate valid/invalid
def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0

if is_even(4):
    print("4 is even")

def is_valid_age(age):
    """Check if age is in valid range."""
    return 0 <= age <= 120
```

### Calculation Functions

```python
# Perform calculations and return result
def calculate_circle_area(radius):
    """Calculate the area of a circle."""
    PI = 3.14159
    return PI * radius ** 2

def convert_celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32
```

### Transformation Functions

```python
# Transform input and return modified version
def to_uppercase(text):
    """Convert text to uppercase."""
    return text.upper()

def format_name(first, last):
    """Format name as 'Last, First'."""
    return f"{last}, {first}"
```

### Processing Functions

```python
# Process data without returning (side effects)
def print_report(name, score):
    """Print a formatted score report."""
    print("=" * 30)
    print(f"Student: {name}")
    print(f"Score: {score}")
    print("=" * 30)
```

## 🔧 Built-in Functions Review

Python has many built-in functions you've already been using:

```python
# Input/Output
print("Hello")              # Output to console
input("Enter name: ")       # Get user input

# Type conversion
int("42")                   # Convert to integer
float("3.14")               # Convert to float
str(42)                     # Convert to string

# Math functions
abs(-5)                     # Absolute value: 5
round(3.7)                  # Round: 4
max(1, 5, 3)               # Maximum: 5
min(1, 5, 3)               # Minimum: 1
sum([1, 2, 3])             # Sum: 6
pow(2, 3)                  # Power: 8

# Type checking
type(42)                    # Get type: <class 'int'>
isinstance(42, int)         # Check type: True

# String/List functions
len("hello")                # Length: 5
range(10)                   # Generate sequence 0-9
```

## 📚 Mini-Programs in This Folder

Apply these concepts in the following programs:

1. **01_basic_functions.py** - Introduction to function basics
   - Define functions with `def` keyword
   - Use parameters and return statements
   - Call functions with arguments
   - Understand function scope

2. **02_temperature_functions.py** - Temperature conversion functions
   - Create functions that perform calculations
   - Pass arguments and use return values
   - Build complex functions from simple ones
   - Practice with formulas

3. **03_string_functions.py** - String manipulation functions
   - Work with string methods inside functions
   - Return modified strings
   - Practice parameter passing
   - Create utility functions

4. **04_math_functions.py** - Mathematical utility functions
   - Create functions for common math operations
   - Find maximum, minimum, and averages
   - Calculate areas and other measurements
   - Combine multiple functions

## 💡 Quick Tips

✅ **Best Practices:**
- Use descriptive function names (verbs for actions)
- Keep functions focused on one task (Single Responsibility Principle)
- Use docstrings to document functions
- Prefer returning values over printing (more flexible)
- Use meaningful parameter names
- Keep functions short (generally under 20 lines)
- Avoid modifying global variables

❌ **Common Mistakes:**
- Forgetting the colon (:) after the def line
- Not indenting the function body
- Calling a function before defining it
- Forgetting to return a value (returns None by default)
- Using parentheses when defining: `def greet():` not `def greet():`
- Modifying global variables without `global` keyword
- Too many parameters (consider using a dictionary or object)

## 🎓 Key Takeaways

1. Functions are reusable blocks of code defined with `def`
2. Parameters are inputs; return values are outputs
3. Use descriptive names and docstrings
4. Scope determines where variables can be accessed
5. Functions promote code reuse and organization
6. Parameters can have default values
7. Use `return` to send values back to the caller
8. Keep functions focused and independent

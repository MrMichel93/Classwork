# Variables, Expressions and Statements

## 📖 What Are Variables?

A **variable** is a named container that stores a value in your computer's memory. Think of it like a labeled box where you can store information and retrieve it later using its name.

### Understanding Variables

- Variables have a **name** (identifier) that you choose
- Variables store a **value** (data)
- Variables have a **type** (int, float, string, bool, etc.)
- Variable values can be changed (they're "variable"!)

## 🎯 Basic Syntax

### Creating Variables (Assignment)

```python
# Basic variable assignment
name = "Alice"              # String variable
age = 25                    # Integer variable
height = 5.8                # Float variable
is_student = True           # Boolean variable

# Multiple assignments
x = y = z = 0               # All three variables get the same value
a, b, c = 1, 2, 3          # Assign multiple values at once
```

### Variable Naming Rules

✅ **Valid names:**
- Use letters (a-z, A-Z), numbers (0-9), and underscores (_)
- Must start with a letter or underscore
- Case-sensitive (`age` and `Age` are different)
- Examples: `my_variable`, `total_sum`, `student_1`, `_private`

❌ **Invalid names:**
- Cannot start with a number: `2variable` ❌
- Cannot use special characters: `my-var`, `price$` ❌
- Cannot use Python keywords: `for`, `if`, `while` ❌

### Naming Conventions (Best Practices)

```python
# Use lowercase with underscores (snake_case)
student_name = "John"
total_price = 99.99
is_valid = True

# Descriptive names are better than short ones
temperature_celsius = 25        # Good
temp = 25                       # Less clear
t = 25                          # Avoid
```

## 📊 Data Types

### Common Data Types

```python
# Integer (int) - whole numbers
age = 25
year = 2024
negative_number = -10

# Float - decimal numbers
price = 19.99
temperature = 98.6
pi = 3.14159

# String (str) - text
name = "Alice"
message = 'Hello World'
multi_line = """This is
a multi-line
string"""

# Boolean (bool) - True or False
is_student = True
has_passed = False
```

### Checking Types

```python
# Use type() to check a variable's type
print(type(42))           # <class 'int'>
print(type(3.14))         # <class 'float'>
print(type("Hello"))      # <class 'str'>
print(type(True))         # <class 'bool'>
```

### Type Conversion

```python
# Convert between types
age_str = "25"
age_int = int(age_str)          # Convert string to int: 25

price_float = 19.99
price_int = int(price_float)    # Convert float to int: 19 (truncates)

number = 42
number_str = str(number)        # Convert int to string: "42"
number_float = float(number)    # Convert int to float: 42.0

# Be careful with conversions
int("abc")                      # Error! Can't convert non-numeric string
```

## ➕ Operators

### Arithmetic Operators

```python
# Basic arithmetic
a = 10
b = 3

addition = a + b           # 13
subtraction = a - b        # 7
multiplication = a * b     # 30
division = a / b           # 3.3333... (always returns float)
floor_division = a // b    # 3 (integer division, rounds down)
modulo = a % b             # 1 (remainder)
exponent = a ** b          # 1000 (10 to the power of 3)

# Negative numbers
negative = -a              # -10
```

### Assignment Operators

```python
# Standard assignment
x = 5

# Compound assignment operators (shortcuts)
x += 3      # Same as: x = x + 3  → x is now 8
x -= 2      # Same as: x = x - 2  → x is now 6
x *= 4      # Same as: x = x * 4  → x is now 24
x /= 2      # Same as: x = x / 2  → x is now 12.0
x //= 5     # Same as: x = x // 5 → x is now 2.0
x %= 2      # Same as: x = x % 2  → x is now 0.0
x **= 3     # Same as: x = x ** 3 → x is now 0.0
```

### Operator Precedence (Order of Operations)

```python
# Python follows PEMDAS order:
# 1. Parentheses ()
# 2. Exponents **
# 3. Multiplication *, Division /, Floor Division //, Modulo %
# 4. Addition +, Subtraction -

result = 2 + 3 * 4        # 14 (multiplication first)
result = (2 + 3) * 4      # 20 (parentheses first)
result = 10 - 2 + 3       # 11 (left to right for same precedence)
result = 2 ** 3 ** 2      # 512 (right to left for exponents: 2^(3^2))
```

## 💬 Expressions and Statements

### What's an Expression?

An **expression** is any combination of values, variables, and operators that produces a value.

```python
# All of these are expressions (they produce values)
5 + 3                # Produces: 8
age * 2              # Produces: a number (if age is defined)
"Hello" + " World"   # Produces: "Hello World"
10 > 5               # Produces: True
```

### What's a Statement?

A **statement** is a complete line of code that performs an action.

```python
# These are statements (they perform actions)
x = 5                        # Assignment statement
print("Hello")               # Function call statement
age = age + 1                # Assignment with expression
```

## 📤 Input and Output

### The print() Function

```python
# Basic printing
print("Hello, World!")                    # Print text
print(42)                                 # Print number
print(3.14)                               # Print float

# Print multiple items (separated by space)
name = "Alice"
age = 25
print("Name:", name, "Age:", age)         # Name: Alice Age: 25

# Print with custom separator
print("apple", "banana", "cherry", sep=", ")  # apple, banana, cherry

# Print without newline at the end
print("Hello", end=" ")
print("World")                            # Hello World (on same line)

# Print with custom end character
print("Loading", end="...")               # Loading... (no newline)
```

### The input() Function

```python
# Get user input (always returns a string)
name = input("Enter your name: ")
print("Hello,", name)

# Convert input to numbers
age_str = input("Enter your age: ")
age = int(age_str)                        # Convert to integer

# One-liner conversion
age = int(input("Enter your age: "))
price = float(input("Enter price: "))
```

## 🔢 Common Built-in Functions

### Mathematical Functions

```python
# abs() - absolute value
abs(-10)              # 10
abs(5)                # 5

# round() - round to nearest integer
round(3.7)            # 4
round(3.4)            # 3
round(3.14159, 2)     # 3.14 (round to 2 decimal places)

# pow() - power function
pow(2, 3)             # 8 (same as 2 ** 3)
pow(5, 2)             # 25

# max() and min() - maximum and minimum
max(5, 10, 3)         # 10
min(5, 10, 3)         # 3

# sum() - sum of iterable
sum([1, 2, 3, 4])     # 10
```

## 📝 String Operations

### String Concatenation

```python
# Combine strings with +
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name    # "John Doe"

# Repeat strings with *
laugh = "ha" * 3                             # "hahaha"
line = "-" * 20                              # "--------------------"
```

### String Formatting (f-strings)

```python
# f-strings (formatted string literals) - Python 3.6+
name = "Alice"
age = 25
message = f"My name is {name} and I am {age} years old"
# "My name is Alice and I am 25 years old"

# Format numbers in f-strings
price = 19.99
print(f"Price: ${price:.2f}")                # Price: $19.99
```

## 🧮 Working with Constants

### Using Constants

```python
# Constants are variables that shouldn't change
# Convention: Use UPPERCASE names
PI = 3.14159
GRAVITY = 9.8
TAX_RATE = 0.08

# Calculate circle area
radius = 5
area = PI * radius ** 2
```

## 📚 Mini-Programs in This Folder

Apply these concepts in the following programs:

1. **01_calculator.py** - Practice arithmetic operations and expressions
   - Create variables for numbers
   - Use all arithmetic operators (+, -, *, /, //, %, **)
   - Print results with descriptive messages

2. **02_temperature_converter.py** - Convert between temperature scales
   - Work with float variables
   - Apply conversion formulas
   - Format numeric output

3. **03_shopping_cart.py** - Calculate shopping cart totals with tax
   - Use multiple variables for related data
   - Perform calculations with money
   - Apply constants (TAX_RATE)

4. **04_area_calculator.py** - Calculate areas and perimeters
   - Use variables in geometric formulas
   - Work with the constant PI
   - Calculate multiple related values

## 💡 Quick Tips

✅ **Best Practices:**
- Use descriptive variable names
- Follow naming conventions (snake_case)
- Initialize variables before using them
- Use constants (UPPERCASE) for values that don't change
- Add comments to explain complex calculations

❌ **Common Mistakes:**
- Forgetting to convert input() to int or float
- Using variables before assigning them
- Confusing = (assignment) with == (comparison)
- Integer division confusion: 7 / 2 = 3.5 but 7 // 2 = 3

## 🎓 Key Takeaways

1. Variables store data with a name and type
2. Python has built-in data types: int, float, str, bool
3. Expressions produce values, statements perform actions
4. Operators follow precedence rules (PEMDAS)
5. Use `print()` for output and `input()` for user input
6. Convert between types with int(), float(), str()
7. Use descriptive names and follow conventions

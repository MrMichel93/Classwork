# Conditionals

## 📖 What Are Conditionals?

**Conditionals** are programming structures that allow your code to make decisions and execute different code blocks based on whether conditions are true or false. They control the flow of your program.

### Understanding Conditionals

- Conditionals use **conditions** (expressions that evaluate to True or False)
- They create **branches** in your code (different paths of execution)
- Only the code in the True branch executes
- Essential for making programs interactive and dynamic

## 🎯 Basic Syntax

### The if Statement

```python
# Basic if statement
age = 18
if age >= 18:
    print("You are an adult")
    print("You can vote")

# Single line if (not recommended for readability)
if age >= 18: print("Adult")
```

### The if-else Statement

```python
# if-else: Two possible paths
age = 15
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

### The if-elif-else Statement

```python
# if-elif-else: Multiple conditions
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Note: Only the FIRST True condition executes
```

### Nested if Statements

```python
# if statements inside other if statements
age = 20
has_license = True

if age >= 18:
    print("You are old enough to drive")
    if has_license:
        print("You can drive!")
    else:
        print("But you need a license first")
else:
    print("You are too young to drive")
```

## 🔍 Comparison Operators

Use these operators to compare values and create conditions:

```python
a = 10
b = 5

# Equal to
a == b          # False (10 is not equal to 5)

# Not equal to
a != b          # True (10 is not equal to 5)

# Greater than
a > b           # True (10 is greater than 5)

# Less than
a < b           # False (10 is not less than 5)

# Greater than or equal to
a >= b          # True (10 is greater than or equal to 5)
a >= 10         # True (10 is equal to 10)

# Less than or equal to
a <= b          # False (10 is not less than or equal to 5)
```

### Comparing Different Types

```python
# Numbers
5 == 5.0        # True (values are equal)
5 > 3.2         # True

# Strings
"apple" == "apple"      # True
"apple" == "Apple"      # False (case-sensitive)
"abc" < "abd"           # True (alphabetical comparison)
"10" < "2"              # True (string comparison, not numeric!)

# Be careful comparing different types
5 == "5"        # False (int vs string)
```

## 🔗 Logical Operators

Combine multiple conditions with logical operators:

### The `and` Operator

Both conditions must be True for the result to be True.

```python
age = 25
has_ticket = True

# Both must be True
if age >= 18 and has_ticket:
    print("You can enter the concert")

# Truth table for 'and'
True and True       # True
True and False      # False
False and True      # False
False and False     # False
```

### The `or` Operator

At least one condition must be True for the result to be True.

```python
is_weekend = True
is_holiday = False

# At least one must be True
if is_weekend or is_holiday:
    print("No work today!")

# Truth table for 'or'
True or True        # True
True or False       # True
False or True       # True
False or False      # False
```

### The `not` Operator

Inverts the boolean value (True becomes False, False becomes True).

```python
is_raining = False

# not inverts the value
if not is_raining:
    print("It's a nice day!")

# Truth table for 'not'
not True            # False
not False           # True
```

### Combining Logical Operators

```python
age = 25
has_ticket = True
is_member = False

# Multiple logical operators
if (age >= 18 and has_ticket) or is_member:
    print("Entry allowed")

# Use parentheses for clarity
if age >= 18 and (has_ticket or is_member):
    print("Entry allowed if adult with ticket or membership")
```

## ✅ Boolean Values and Expressions

### Boolean Type

```python
# Boolean variables
is_student = True
has_passed = False

# Boolean expressions (evaluate to True or False)
10 > 5              # True
3 == 3              # True
"hi" == "bye"       # False
```

### Truthy and Falsy Values

In Python, some values are considered "truthy" or "falsy" in conditionals:

```python
# Falsy values (treated as False)
if 0: ...               # False (zero)
if "": ...              # False (empty string)
if []: ...              # False (empty list)
if None: ...            # False (None value)

# Truthy values (treated as True)
if 1: ...               # True (non-zero numbers)
if "hello": ...         # True (non-empty strings)
if [1, 2]: ...          # True (non-empty lists)
```

### Checking for True/False Explicitly

```python
# Check if value is exactly True or False
value = 1
if value is True:       # False (1 is not exactly True)
    print("Exactly True")

if value:               # True (1 is truthy)
    print("Truthy value")

# Better practice: be explicit
is_valid = True
if is_valid == True:    # Works, but unnecessary
if is_valid:            # Better - more Pythonic
```

## 🔤 String Comparisons

### The `in` Operator

Check if a substring exists in a string:

```python
# Check if substring is in string
password = "secret123"

if "123" in password:
    print("Password contains numbers")

if "abc" not in password:
    print("Password doesn't contain 'abc'")

# Case-sensitive
if "SECRET" in password:    # False (case matters)
    print("Found")
```

### String Comparison Methods

```python
text = "Hello World"

# Check string contents
if text.startswith("Hello"):
    print("Starts with Hello")

if text.endswith("World"):
    print("Ends with World")

# Check character types
if text.isalpha():          # False (has space)
    print("All letters")

if text.isdigit():          # False (has letters)
    print("All digits")

if text.islower():          # False (has uppercase)
    print("All lowercase")

if text.isupper():          # False (has lowercase)
    print("All uppercase")
```

## 🎭 Common Conditional Patterns

### Range Checking

```python
# Check if value is in a range
age = 25
if 18 <= age < 65:
    print("Working age adult")

# Equivalent to:
if age >= 18 and age < 65:
    print("Working age adult")
```

### Multiple Conditions

```python
# Check multiple values
grade = "B"
if grade == "A" or grade == "B" or grade == "C":
    print("Passing grade")

# More elegant with 'in'
if grade in ["A", "B", "C"]:
    print("Passing grade")

# Check against multiple conditions
score = 85
if 80 <= score <= 89:           # Chained comparison
    print("Grade B range")
```

### Validating Input

```python
# Validate user input
age = int(input("Enter age: "))

# Check for valid range
if age < 0 or age > 120:
    print("Invalid age")
else:
    print("Valid age")

# Validate non-empty input
name = input("Enter name: ")
if name == "":
    print("Name cannot be empty")
elif len(name) < 2:
    print("Name too short")
else:
    print("Valid name")
```

### Ternary Operator (Conditional Expression)

```python
# Compact if-else: value_if_true if condition else value_if_false
age = 20
status = "adult" if age >= 18 else "minor"

# Equivalent to:
if age >= 18:
    status = "adult"
else:
    status = "minor"

# Use for simple assignments, but don't overuse
message = "Pass" if score >= 60 else "Fail"
max_value = a if a > b else b
```

## 🎯 Condition Evaluation Order

### Short-Circuit Evaluation

Python evaluates conditions from left to right and stops as soon as the result is known:

```python
# 'and' stops at first False
def expensive_check():
    print("Expensive check called")
    return True

age = 15
if age >= 18 and expensive_check():     # expensive_check() never called
    print("Allowed")
# Only prints nothing (age >= 18 is False, so second condition not checked)

# 'or' stops at first True
is_admin = True
if is_admin or expensive_check():       # expensive_check() never called
    print("Access granted")
# Prints "Access granted" (is_admin is True, so second condition not checked)
```

## 🚫 Common Mistakes and Pitfalls

### Assignment vs Comparison

```python
# WRONG: Using = instead of ==
x = 5
if x = 5:           # SyntaxError! This is assignment, not comparison
    print("Five")

# CORRECT: Use == for comparison
if x == 5:          # This works!
    print("Five")
```

### Checking for True/False

```python
is_valid = True

# Works but unnecessary
if is_valid == True:
    print("Valid")

# Better - more Pythonic
if is_valid:
    print("Valid")

# For False checks
if not is_valid:
    print("Invalid")
```

### Comparing Floats

```python
# Be careful with float comparisons due to precision
result = 0.1 + 0.2
if result == 0.3:               # Might be False due to floating point precision!
    print("Equal")

# Better approach for float comparison
if abs(result - 0.3) < 0.0001:  # Check if difference is very small
    print("Approximately equal")
```

### Chained Comparisons

```python
x = 5

# WRONG: This doesn't work as expected
if x == 3 or 4 or 5:            # Always True! (4 and 5 are truthy)
    print("Found")

# CORRECT: Proper way
if x == 3 or x == 4 or x == 5:
    print("Found")

# BETTER: Use 'in'
if x in [3, 4, 5]:
    print("Found")
```

## 📚 Mini-Programs in This Folder

Apply these concepts in the following programs:

1. **01_grade_checker.py** - Assign letter grades based on scores
   - Use if-elif-else statements
   - Practice comparison operators (>=, <)
   - Validate input ranges
   - Handle edge cases

2. **02_age_classifier.py** - Classify people into age groups
   - Work with multiple conditions
   - Use logical operators (and, or)
   - Apply age-based rules
   - Create age range checks

3. **02_number_comparator.py** - Compare and analyze numbers
   - Determine relationships between numbers
   - Practice nested if statements
   - Use comparison operators (==, !=, >, <)
   - Work with multiple variables

4. **04_password_validator.py** - Validate passwords based on rules
   - Use string comparisons
   - Apply the 'in' operator
   - Combine multiple validation conditions
   - Provide meaningful feedback

## 💡 Quick Tips

✅ **Best Practices:**
- Use clear, descriptive condition names
- Keep conditions simple and readable
- Use 'in' for checking multiple values
- Avoid deep nesting (max 2-3 levels)
- Put the most likely condition first in elif chains
- Use parentheses to clarify complex conditions

❌ **Common Mistakes:**
- Using = instead of == in conditions
- Forgetting the colon (:) at the end of if/elif/else
- Not indenting the code block after if/elif/else
- Comparing strings with numbers without conversion
- Using `if x == True:` instead of `if x:`

## 🎓 Key Takeaways

1. Conditionals control program flow based on True/False conditions
2. Use if, elif, else for different execution paths
3. Comparison operators: ==, !=, >, <, >=, <=
4. Logical operators: and, or, not
5. The 'in' operator checks membership in strings and lists
6. Python uses short-circuit evaluation for efficiency
7. Avoid common pitfalls: = vs ==, proper indentation, clear conditions
8. Keep conditions simple and use parentheses for complex logic

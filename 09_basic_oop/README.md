# Basic Object-Oriented Programming (OOP)

## 📖 What is Object-Oriented Programming?

**Object-Oriented Programming (OOP)** is a programming paradigm that organizes code around objects - bundles of data (attributes) and functions (methods) that work together. Instead of thinking in terms of functions and data separately, you think in terms of objects that represent real-world entities.

### Understanding OOP

- **Objects** are instances of classes (like variables are instances of types)
- **Classes** are blueprints or templates for creating objects
- **Attributes** are variables that belong to an object (data)
- **Methods** are functions that belong to an object (behavior)
- OOP helps organize and structure complex programs

### Why Use Object-Oriented Programming?

✅ **Organization** - Group related data and functions together  
✅ **Reusability** - Create multiple objects from one class  
✅ **Modularity** - Changes to one class don't affect others  
✅ **Real-world modeling** - Objects represent real entities  
✅ **Maintainability** - Easier to update and debug  
✅ **Scalability** - Build large programs more effectively  

## 🏗️ Classes and Objects

### What is a Class?

A **class** is a blueprint for creating objects. It defines what attributes and methods objects of that class will have.

```python
# Simple class definition
class Dog:
    pass  # Empty class (for now)

# Create an instance (object) of the class
my_dog = Dog()
print(my_dog)  # <__main__.Dog object at 0x...>
```

### Creating a Basic Class

```python
# Class with attributes
class Dog:
    pass

# Create dog and add attributes directly
my_dog = Dog()
my_dog.name = "Buddy"
my_dog.age = 3
my_dog.breed = "Golden Retriever"

print(f"{my_dog.name} is a {my_dog.age} year old {my_dog.breed}")
# Output: Buddy is a 3 year old Golden Retriever
```

### Multiple Objects

```python
# Create multiple objects from same class
class Dog:
    pass

dog1 = Dog()
dog1.name = "Buddy"
dog1.age = 3

dog2 = Dog()
dog2.name = "Max"
dog2.age = 5

# Each object is independent
print(dog1.name)  # Buddy
print(dog2.name)  # Max
```

## 🎯 The __init__ Method (Constructor)

### What is __init__?

The `__init__` method is a special method that runs automatically when you create a new object. It's used to initialize the object's attributes.

```python
# Class with __init__ method
class Dog:
    def __init__(self, name, age, breed):
        """Initialize dog attributes"""
        self.name = name
        self.age = age
        self.breed = breed

# Create dog (attributes set automatically)
my_dog = Dog("Buddy", 3, "Golden Retriever")

print(my_dog.name)   # Buddy
print(my_dog.age)    # 3
print(my_dog.breed)  # Golden Retriever
```

### Understanding self

```python
# 'self' refers to the instance being created/used
class Person:
    def __init__(self, name, age):
        self.name = name    # self.name is the instance attribute
        self.age = age      # name is the parameter

# When you create an object:
person = Person("Alice", 25)
# Python automatically passes 'person' as 'self'
# So: person.name = "Alice", person.age = 25
```

### Default Parameter Values in __init__

```python
# Parameters with default values
class Dog:
    def __init__(self, name, age=0, breed="Mixed"):
        self.name = name
        self.age = age
        self.breed = breed

# Use defaults
dog1 = Dog("Buddy")                    # age=0, breed="Mixed"

# Override defaults
dog2 = Dog("Max", 5, "Labrador")       # age=5, breed="Labrador"

# Mix and match with keyword arguments
dog3 = Dog("Charlie", breed="Poodle")  # age=0, breed="Poodle"
```

### Multiple Attribute Types

```python
# Attributes can be any type
class Student:
    def __init__(self, name, age, grades, is_active=True):
        self.name = name                # String
        self.age = age                  # Integer
        self.grades = grades            # List
        self.is_active = is_active      # Boolean

student = Student("Alice", 20, [90, 85, 88])
print(student.name)        # Alice
print(student.grades)      # [90, 85, 88]
print(student.is_active)   # True
```

## 🎬 Methods

### What are Methods?

Methods are functions that belong to a class. They define what objects can do.

```python
# Class with methods
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        """Method to make the dog bark"""
        print(f"{self.name} says Woof!")
    
    def birthday(self):
        """Increase dog's age by 1"""
        self.age += 1
        print(f"Happy birthday {self.name}! Now {self.age} years old.")

# Create dog and call methods
my_dog = Dog("Buddy", 3)
my_dog.bark()       # Buddy says Woof!
my_dog.birthday()   # Happy birthday Buddy! Now 4 years old.
print(my_dog.age)   # 4
```

### Methods with Parameters

```python
# Methods can take parameters (besides self)
class Calculator:
    def __init__(self, name):
        self.name = name
    
    def add(self, a, b):
        """Add two numbers"""
        return a + b
    
    def multiply(self, a, b):
        """Multiply two numbers"""
        return a * b

calc = Calculator("My Calculator")
print(calc.add(5, 3))       # 8
print(calc.multiply(4, 7))  # 28
```

### Methods with Return Values

```python
# Methods can return values
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        """Calculate and return area"""
        return self.width * self.height
    
    def perimeter(self):
        """Calculate and return perimeter"""
        return 2 * (self.width + self.height)
    
    def is_square(self):
        """Check if rectangle is a square"""
        return self.width == self.height

rect = Rectangle(5, 10)
print(rect.area())        # 50
print(rect.perimeter())   # 30
print(rect.is_square())   # False

square = Rectangle(5, 5)
print(square.is_square()) # True
```

### Methods Accessing Other Methods

```python
# Methods can call other methods
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        """Deposit money"""
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        """Withdraw money"""
        if amount > self.balance:
            print("Insufficient funds!")
            return False
        self.balance -= amount
        return True
    
    def transfer(self, other_account, amount):
        """Transfer money to another account"""
        if self.withdraw(amount):  # Call withdraw method
            other_account.deposit(amount)  # Call deposit on other account
            print(f"Transferred ${amount} to {other_account.owner}")
            return True
        return False

account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500)

account1.transfer(account2, 200)
print(f"Alice: ${account1.balance}")  # 800
print(f"Bob: ${account2.balance}")    # 700
```

## 📊 Attributes

### Instance Attributes

```python
# Instance attributes - unique to each object
class Car:
    def __init__(self, make, model, year):
        self.make = make      # Instance attribute
        self.model = model    # Instance attribute
        self.year = year      # Instance attribute

car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2021)

# Each car has its own attributes
print(car1.make)  # Toyota
print(car2.make)  # Honda
```

### Modifying Attributes

```python
# Access and modify attributes directly
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 25)
print(person.age)   # 25

# Modify attribute
person.age = 26
print(person.age)   # 26

# Add new attribute (not recommended)
person.city = "NYC"
print(person.city)  # NYC
```

### Computed Attributes

```python
# Attributes calculated from other attributes
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        """Calculate area (not stored, computed each time)"""
        return 3.14159 * self.radius ** 2
    
    def diameter(self):
        """Calculate diameter"""
        return 2 * self.radius

circle = Circle(5)
print(circle.radius)    # 5
print(circle.area())    # 78.53975
print(circle.diameter()) # 10
```

## 🏷️ Class vs Instance Attributes

### Class Attributes

Class attributes are shared by all instances of a class.

```python
# Class attribute - shared by all instances
class Dog:
    species = "Canis familiaris"  # Class attribute
    
    def __init__(self, name, age):
        self.name = name    # Instance attribute
        self.age = age      # Instance attribute

dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# All dogs share the same species
print(dog1.species)  # Canis familiaris
print(dog2.species)  # Canis familiaris

# But each has unique name
print(dog1.name)     # Buddy
print(dog2.name)     # Max
```

### Class Attributes for Counting

```python
# Use class attribute to track all instances
class Student:
    total_students = 0  # Class attribute
    
    def __init__(self, name):
        self.name = name
        Student.total_students += 1  # Increment for each new student

student1 = Student("Alice")
print(Student.total_students)  # 1

student2 = Student("Bob")
print(Student.total_students)  # 2

student3 = Student("Charlie")
print(Student.total_students)  # 3
```

## 📝 The __str__ Method

### String Representation

The `__str__` method defines how an object is represented as a string.

```python
# Without __str__
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog = Dog("Buddy", 3)
print(dog)  # <__main__.Dog object at 0x...> (not very useful)

# With __str__
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} (age {self.age})"

dog = Dog("Buddy", 3)
print(dog)  # Buddy (age 3) (much better!)
```

### Useful __str__ Examples

```python
# Book class with __str__
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.pages} pages)"

book = Book("Python Basics", "John Doe", 350)
print(book)  # 'Python Basics' by John Doe (350 pages)

# Rectangle with __str__
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"

rect = Rectangle(5, 10)
print(rect)  # Rectangle(5x10)
```

## 👥 Working with Multiple Objects

### Storing Objects in Lists

```python
# Create list of objects
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def __str__(self):
        return f"{self.name}: {self.grade}"

students = [
    Student("Alice", 90),
    Student("Bob", 85),
    Student("Charlie", 95)
]

# Iterate through objects
for student in students:
    print(student)
# Output:
# Alice: 90
# Bob: 85
# Charlie: 95
```

### Comparing Objects

```python
# Compare objects based on attributes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def is_older_than(self, other):
        """Compare age with another person"""
        return self.age > other.age

person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

if person2.is_older_than(person1):
    print(f"{person2.name} is older than {person1.name}")
```

### Objects as Method Parameters

```python
# Pass objects to methods of other objects
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance_to(self, other_point):
        """Calculate distance to another point"""
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return (dx**2 + dy**2) ** 0.5

point1 = Point(0, 0)
point2 = Point(3, 4)

distance = point1.distance_to(point2)
print(f"Distance: {distance}")  # 5.0
```

## 🎯 Common Class Patterns

### Counter Class

```python
class Counter:
    def __init__(self, start=0):
        self.count = start
    
    def increment(self):
        self.count += 1
    
    def decrement(self):
        self.count -= 1
    
    def reset(self):
        self.count = 0
    
    def get_count(self):
        return self.count

counter = Counter()
counter.increment()
counter.increment()
counter.increment()
print(counter.get_count())  # 3
```

### Data Container Class

```python
class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    
    def get_info(self):
        """Return formatted person info"""
        return f"Name: {self.name}, Age: {self.age}, Email: {self.email}"
    
    def is_adult(self):
        """Check if person is 18 or older"""
        return self.age >= 18

person = Person("Alice", 25, "alice@example.com")
print(person.get_info())
print(f"Adult: {person.is_adult()}")
```

### Validator Class

```python
class PasswordValidator:
    def __init__(self, min_length=8):
        self.min_length = min_length
    
    def is_valid_length(self, password):
        """Check if password meets minimum length"""
        return len(password) >= self.min_length
    
    def has_number(self, password):
        """Check if password contains a number"""
        return any(char.isdigit() for char in password)
    
    def has_uppercase(self, password):
        """Check if password contains uppercase letter"""
        return any(char.isupper() for char in password)
    
    def is_valid(self, password):
        """Check all validation rules"""
        return (self.is_valid_length(password) and
                self.has_number(password) and
                self.has_uppercase(password))

validator = PasswordValidator()
password = "MyPass123"
if validator.is_valid(password):
    print("Password is valid")
else:
    print("Password is invalid")
```

## 🔍 Accessing and Checking Attributes

### hasattr, getattr, setattr

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 25)

# hasattr() - Check if attribute exists
print(hasattr(person, "name"))    # True
print(hasattr(person, "city"))    # False

# getattr() - Get attribute value
name = getattr(person, "name")    # "Alice"
city = getattr(person, "city", "Unknown")  # "Unknown" (default)

# setattr() - Set attribute value
setattr(person, "age", 26)
setattr(person, "city", "NYC")    # Create new attribute

print(person.age)   # 26
print(person.city)  # NYC
```

## 📚 Mini-Programs in This Folder

Apply these concepts in the following programs:

1. **01_simple_class.py** - Introduction to classes
   - Define classes with the `class` keyword
   - Create instances (objects) from classes
   - Add attributes to objects
   - Use the `__init__` method for initialization
   - Create multiple independent objects
   - Understand the difference between class and instance

2. **02_class_attributes.py** - Class vs instance attributes
   - Understand instance attributes (unique to each object)
   - Use class attributes (shared by all objects)
   - Track data across all instances
   - Modify instance and class attributes
   - Use class attributes for constants and counters

3. **03_class_methods.py** - Methods and behavior
   - Define methods inside classes
   - Use the `self` parameter correctly
   - Create methods with parameters
   - Return values from methods
   - Call methods from other methods
   - Implement the `__str__` method

4. **04_multiple_objects.py** - Working with multiple objects
   - Create and manage multiple instances
   - Store objects in lists
   - Iterate through collections of objects
   - Compare objects based on attributes
   - Pass objects as parameters
   - Work with objects interacting with each other

## 💡 Quick Tips

✅ **Best Practices:**
- Use `__init__` to initialize all attributes
- Use meaningful class and method names (PascalCase for classes)
- Keep methods focused on a single task
- Use `self` to access instance attributes and methods
- Implement `__str__` for readable object representation
- Document classes and methods with docstrings
- Group related data and behavior in the same class

❌ **Common Mistakes:**
- Forgetting `self` as first parameter in methods
- Not using `self.` to access instance attributes
- Creating attributes outside `__init__` (confusing)
- Using class attributes when instance attributes are needed
- Modifying class attributes directly (affects all instances)
- Not calling methods with parentheses: `obj.method()` not `obj.method`

## 🎓 Key Takeaways

1. **Classes** are blueprints for creating objects
2. **Objects** are instances of classes
3. **__init__** initializes object attributes
4. **self** refers to the instance being used
5. **Methods** define what objects can do
6. **Instance attributes** are unique to each object
7. **Class attributes** are shared by all objects
8. **__str__** defines string representation of objects
9. Objects can be stored in lists and other data structures
10. OOP helps organize code by grouping related data and behavior

# Advanced Object-Oriented Programming

## 📖 Advanced OOP Concepts

This module covers professional OOP patterns and techniques used in production code. You'll learn about properties, special methods, class/static methods, and abstract classes - tools that make your code more robust, maintainable, and Pythonic.

### What You'll Learn

- **Properties** - Control attribute access with getters and setters
- **Class methods** - Methods that work with the class itself
- **Static methods** - Utility functions within a class
- **Magic methods** - Special methods that enable operator overloading
- **Abstract classes** - Define interfaces and enforce implementation

### Why Learn Advanced OOP?

✅ **Professional code** - Write production-quality software  
✅ **Data validation** - Control and validate attribute access  
✅ **Flexibility** - Change implementation without breaking interface  
✅ **Operator overloading** - Make custom objects behave like built-ins  
✅ **Enforce contracts** - Use abstract classes as interfaces  
✅ **Better design** - Apply design patterns effectively  

## 🎯 Properties

### Why Use Properties?

Properties allow you to add logic when getting or setting attributes while maintaining simple syntax.

```python
# Without properties - direct attribute access
class Person:
    def __init__(self, age):
        self.age = age  # No validation!

person = Person(-5)  # Invalid age accepted!
print(person.age)    # -5

# With properties - controlled access
class Person:
    def __init__(self, age):
        self._age = age  # "Private" attribute
    
    @property
    def age(self):
        """Getter - called when accessing person.age"""
        return self._age
    
    @age.setter
    def age(self, value):
        """Setter - called when setting person.age = value"""
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

person = Person(25)
print(person.age)    # 25 (calls getter)
person.age = 26      # Calls setter
# person.age = -5    # ValueError!
```

### Property Syntax

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Getter - access with obj.celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter - modify with obj.celsius = value"""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    
    @celsius.deleter
    def celsius(self):
        """Deleter - delete with del obj.celsius"""
        print("Deleting temperature")
        del self._celsius

temp = Temperature(25)
print(temp.celsius)      # 25 (calls getter)
temp.celsius = 30        # Calls setter
# temp.celsius = -300    # ValueError!
del temp.celsius         # Calls deleter
```

### Computed Properties

```python
# Properties can compute values on-the-fly
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @property
    def area(self):
        """Computed property - not stored, calculated when accessed"""
        return self.width * self.height
    
    @property
    def perimeter(self):
        """Another computed property"""
        return 2 * (self.width + self.height)

rect = Rectangle(5, 10)
print(rect.area)       # 50 (computed, not stored)
print(rect.perimeter)  # 30 (computed, not stored)

# Change dimensions - area updates automatically
rect.width = 7
print(rect.area)       # 70 (recomputed)
```

### Read-Only Properties

```python
# Property with getter only (no setter) = read-only
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @property
    def diameter(self):
        """Read-only property (no setter)"""
        return self._radius * 2
    
    @property
    def area(self):
        """Read-only property"""
        return 3.14159 * self._radius ** 2

circle = Circle(5)
print(circle.diameter)   # 10
# circle.diameter = 20   # AttributeError! (no setter)
print(circle.area)       # 78.53975
```

### Validation with Properties

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance
    
    @property
    def balance(self):
        """Get balance"""
        return self._balance
    
    @balance.setter
    def balance(self, value):
        """Set balance with validation"""
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount  # Uses setter (validates!)
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        self.balance -= amount  # Uses setter (validates!)

account = BankAccount("Alice", 1000)
account.deposit(500)
print(account.balance)    # 1500
# account.balance = -100  # ValueError!
```

## 🏭 Class Methods

### What are Class Methods?

Class methods are methods that work with the class itself, not instances. They take `cls` (the class) as the first parameter instead of `self`.

```python
class Student:
    school = "Python Academy"  # Class attribute
    
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    @classmethod
    def get_school(cls):
        """Class method - works with class, not instance"""
        return cls.school
    
    @classmethod
    def set_school(cls, school_name):
        """Modify class attribute"""
        cls.school = school_name

# Call on class (no instance needed)
print(Student.get_school())  # Python Academy

# Change for all instances
Student.set_school("Advanced Python Academy")
print(Student.get_school())  # Advanced Python Academy

student = Student("Alice", "A")
print(student.get_school())  # Advanced Python Academy (class-wide change)
```

### Alternative Constructors

```python
# Class methods as alternative constructors
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def from_string(cls, date_string):
        """Create Date from string like '2024-12-25'"""
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)
    
    @classmethod
    def today(cls):
        """Create Date with today's date"""
        import datetime
        today = datetime.date.today()
        return cls(today.year, today.month, today.day)
    
    def __str__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

# Different ways to create Date objects
date1 = Date(2024, 12, 25)              # Regular constructor
date2 = Date.from_string("2024-12-25")  # From string
date3 = Date.today()                     # Today's date

print(date1)  # 2024-12-25
print(date2)  # 2024-12-25
print(date3)  # Current date
```

### Factory Methods

```python
class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country
    
    @classmethod
    def from_birth_year(cls, name, birth_year, country):
        """Create Person from birth year"""
        import datetime
        age = datetime.date.today().year - birth_year
        return cls(name, age, country)
    
    @classmethod
    def from_dict(cls, data):
        """Create Person from dictionary"""
        return cls(data['name'], data['age'], data['country'])
    
    def __str__(self):
        return f"{self.name}, {self.age}, from {self.country}"

person1 = Person("Alice", 25, "USA")
person2 = Person.from_birth_year("Bob", 1995, "UK")
person3 = Person.from_dict({"name": "Charlie", "age": 30, "country": "Canada"})

print(person1)
print(person2)
print(person3)
```

## 📌 Static Methods

### What are Static Methods?

Static methods are regular functions that happen to live in a class. They don't receive `self` or `cls` automatically.

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        """Static method - no self, no cls"""
        return a + b
    
    @staticmethod
    def is_even(n):
        """Check if number is even"""
        return n % 2 == 0
    
    @staticmethod
    def factorial(n):
        """Calculate factorial"""
        if n == 0 or n == 1:
            return 1
        return n * MathUtils.factorial(n - 1)

# Call without instance
print(MathUtils.add(5, 3))       # 8
print(MathUtils.is_even(4))      # True
print(MathUtils.factorial(5))    # 120

# Can also call on instance (but uncommon)
math = MathUtils()
print(math.add(2, 2))            # 4
```

### When to Use Static Methods?

```python
# Use static methods for utility functions related to the class
class StringValidator:
    @staticmethod
    def is_email(text):
        """Validate email format"""
        return '@' in text and '.' in text.split('@')[1]
    
    @staticmethod
    def is_phone(text):
        """Validate phone format (simple)"""
        return text.replace('-', '').isdigit() and len(text) >= 10
    
    @staticmethod
    def is_valid_username(username):
        """Validate username"""
        return (len(username) >= 3 and 
                username.isalnum() and 
                username[0].isalpha())

# Use as namespace for related functions
print(StringValidator.is_email("user@example.com"))   # True
print(StringValidator.is_phone("555-1234"))           # False (too short)
print(StringValidator.is_valid_username("user123"))   # True
```

### Static vs Class vs Instance Methods

```python
class MyClass:
    class_var = "I'm a class variable"
    
    def __init__(self, value):
        self.instance_var = value
    
    def instance_method(self):
        """Has access to instance (self) and class (self.__class__)"""
        print(f"Instance: {self.instance_var}")
        print(f"Class: {self.__class__.class_var}")
    
    @classmethod
    def class_method(cls):
        """Has access to class (cls) but not instance"""
        print(f"Class: {cls.class_var}")
        # print(self.instance_var)  # Error! No self
    
    @staticmethod
    def static_method():
        """No access to instance or class"""
        print("I'm a static method")
        # print(self.instance_var)  # Error! No self
        # print(cls.class_var)      # Error! No cls

obj = MyClass("instance value")
obj.instance_method()  # Can access both
MyClass.class_method()  # Can access class
MyClass.static_method()  # Access to neither
```

## ✨ Magic Methods (Dunder Methods)

### What are Magic Methods?

Magic methods (also called dunder methods for "double underscore") are special methods that enable operator overloading and other Python features.

```python
# Common magic methods
class Point:
    def __init__(self, x, y):
        """Constructor"""
        self.x = x
        self.y = y
    
    def __str__(self):
        """String representation (for print)"""
        return f"Point({self.x}, {self.y})"
    
    def __repr__(self):
        """Developer-friendly representation"""
        return f"Point(x={self.x}, y={self.y})"
    
    def __eq__(self, other):
        """Equality comparison (==)"""
        return self.x == other.x and self.y == other.y
    
    def __add__(self, other):
        """Addition (+)"""
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)

print(p1)           # Point(1, 2) (calls __str__)
print(repr(p1))     # Point(x=1, y=2) (calls __repr__)
print(p1 == p2)     # False (calls __eq__)
p3 = p1 + p2        # Calls __add__
print(p3)           # Point(4, 6)
```

### String Representation Methods

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        """For end users - called by print() and str()"""
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        """For developers - called by repr() and in debugger"""
        return f"Book('{self.title}', '{self.author}', {self.pages})"

book = Book("Python Basics", "John Doe", 350)

print(book)       # 'Python Basics' by John Doe (uses __str__)
print(repr(book)) # Book('Python Basics', 'John Doe', 350) (uses __repr__)
print([book])     # [Book('Python Basics', 'John Doe', 350)] (uses __repr__)
```

### Comparison Magic Methods

```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def __eq__(self, other):
        """Equal to (==)"""
        return self.grade == other.grade
    
    def __ne__(self, other):
        """Not equal to (!=)"""
        return self.grade != other.grade
    
    def __lt__(self, other):
        """Less than (<)"""
        return self.grade < other.grade
    
    def __le__(self, other):
        """Less than or equal (<=)"""
        return self.grade <= other.grade
    
    def __gt__(self, other):
        """Greater than (>)"""
        return self.grade > other.grade
    
    def __ge__(self, other):
        """Greater than or equal (>=)"""
        return self.grade >= other.grade
    
    def __str__(self):
        return f"{self.name}: {self.grade}"

alice = Student("Alice", 90)
bob = Student("Bob", 85)

print(alice > bob)   # True (90 > 85)
print(alice == bob)  # False
print(alice <= bob)  # False

# Can now sort students!
students = [bob, alice, Student("Charlie", 95)]
students.sort()  # Sorts by grade using comparison methods
for student in students:
    print(student)
```

### Arithmetic Magic Methods

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """Addition (+)"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Subtraction (-)"""
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """Multiplication (*)"""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __truediv__(self, scalar):
        """Division (/)"""
        return Vector(self.x / scalar, self.y / scalar)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(10, 20)
v2 = Vector(5, 10)

print(v1 + v2)    # Vector(15, 30)
print(v1 - v2)    # Vector(5, 10)
print(v1 * 2)     # Vector(20, 40)
print(v1 / 2)     # Vector(5.0, 10.0)
```

### Container Magic Methods

```python
class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def __len__(self):
        """Length (len())"""
        return len(self.items)
    
    def __getitem__(self, index):
        """Get item (cart[index])"""
        return self.items[index]
    
    def __setitem__(self, index, value):
        """Set item (cart[index] = value)"""
        self.items[index] = value
    
    def __delitem__(self, index):
        """Delete item (del cart[index])"""
        del self.items[index]
    
    def __contains__(self, item):
        """Membership test (item in cart)"""
        return item in self.items
    
    def __iter__(self):
        """Make iterable (for item in cart)"""
        return iter(self.items)
    
    def add(self, item):
        self.items.append(item)

cart = ShoppingCart()
cart.add("apple")
cart.add("banana")
cart.add("cherry")

print(len(cart))           # 3 (calls __len__)
print(cart[0])             # apple (calls __getitem__)
cart[1] = "blueberry"      # Calls __setitem__
print("apple" in cart)     # True (calls __contains__)

for item in cart:          # Calls __iter__
    print(item)
```

### Callable Objects

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, value):
        """Make object callable like a function"""
        return value * self.factor

double = Multiplier(2)
triple = Multiplier(3)

# Call object like a function
print(double(5))   # 10 (calls __call__)
print(triple(5))   # 15 (calls __call__)

# Practical example: counter
class Counter:
    def __init__(self):
        self.count = 0
    
    def __call__(self):
        """Increment and return count"""
        self.count += 1
        return self.count

counter = Counter()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
```

## 🎨 Abstract Classes

### What are Abstract Classes?

Abstract classes define interfaces that child classes must implement. They can't be instantiated directly.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class - cannot create instances"""
    
    @abstractmethod
    def area(self):
        """All children must implement area()"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """All children must implement perimeter()"""
        pass

# Cannot create Shape directly
# shape = Shape()  # TypeError: Can't instantiate abstract class

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        """Must implement area()"""
        return self.width * self.height
    
    def perimeter(self):
        """Must implement perimeter()"""
        return 2 * (self.width + self.height)

# Can create Rectangle (implements all abstract methods)
rect = Rectangle(5, 10)
print(rect.area())       # 50
print(rect.perimeter())  # 30
```

### Why Use Abstract Classes?

```python
from abc import ABC, abstractmethod

# Define interface with abstract class
class PaymentProcessor(ABC):
    """All payment processors must implement these methods"""
    
    @abstractmethod
    def process_payment(self, amount):
        """Process a payment"""
        pass
    
    @abstractmethod
    def refund(self, transaction_id, amount):
        """Process a refund"""
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing ${amount} via credit card")
        return True
    
    def refund(self, transaction_id, amount):
        print(f"Refunding ${amount} to card {transaction_id}")
        return True

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing ${amount} via PayPal")
        return True
    
    def refund(self, transaction_id, amount):
        print(f"Refunding ${amount} to PayPal {transaction_id}")
        return True

# Both implement same interface
processors = [CreditCardProcessor(), PayPalProcessor()]
for processor in processors:
    processor.process_payment(100)
```

### Abstract Classes with Concrete Methods

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def make_sound(self):
        """Abstract - must be implemented"""
        pass
    
    def sleep(self):
        """Concrete - inherited by all children"""
        print(f"{self.name} is sleeping")
    
    def eat(self):
        """Concrete - inherited by all children"""
        print(f"{self.name} is eating")

class Dog(Animal):
    def make_sound(self):
        """Must implement abstract method"""
        print(f"{self.name} says Woof!")

dog = Dog("Buddy")
dog.make_sound()  # Must implement
dog.sleep()       # Inherited
dog.eat()         # Inherited
```

## 📚 Mini-Programs in This Folder

Apply these concepts in the following programs:

1. **01_properties.py** - Properties and validation
   - Use @property decorator for getters
   - Use @property_name.setter for setters
   - Create computed properties
   - Implement read-only properties
   - Validate attribute values
   - Use private attributes with properties

2. **02_class_methods_static.py** - Class and static methods
   - Define class methods with @classmethod
   - Define static methods with @staticmethod
   - Use class methods as alternative constructors
   - Create factory methods
   - Organize utility functions with static methods
   - Understand when to use each method type

3. **03_magic_methods.py** - Special methods
   - Implement `__str__` and `__repr__`
   - Override comparison operators (`__eq__`, `__lt__`, etc.)
   - Implement arithmetic operators (`__add__`, `__sub__`, etc.)
   - Create container methods (`__len__`, `__getitem__`, etc.)
   - Make objects callable with `__call__`
   - Enable iteration with `__iter__`

4. **04_abstract_classes.py** - Abstract base classes
   - Use ABC and @abstractmethod
   - Define interfaces with abstract classes
   - Force method implementation in child classes
   - Mix abstract and concrete methods
   - Create polymorphic code with abstractions
   - Understand when to use abstract classes

## 💡 Quick Tips

✅ **Best Practices:**
- Use properties for data validation and computed values
- Implement `__str__` for user-friendly output
- Implement `__repr__` for debugging
- Use abstract classes to define interfaces
- Class methods for alternative constructors
- Static methods for utility functions
- Follow naming conventions (e.g., _private_attribute)

❌ **Common Mistakes:**
- Forgetting @property decorator (makes it a regular method)
- Not using super() in abstract class children
- Overusing magic methods (keep it intuitive)
- Using class methods when static methods are better
- Making everything a property (only when needed)
- Not implementing all abstract methods in children
- Confusing `__str__` and `__repr__` purposes

## 🎓 Key Takeaways

1. **Properties** control attribute access with getters/setters
2. **@property** makes methods look like attributes
3. **Class methods** work with the class, take `cls` parameter
4. **Static methods** are utility functions in a class
5. **Magic methods** enable operator overloading
6. **`__str__`** for users, **`__repr__`** for developers
7. **Abstract classes** define interfaces and enforce implementation
8. **@abstractmethod** makes methods required in children
9. Use these tools to write **professional**, **maintainable** code
10. Advanced OOP makes Python objects behave like built-in types

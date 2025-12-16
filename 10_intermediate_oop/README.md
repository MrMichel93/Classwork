# Intermediate Object-Oriented Programming

## 📖 What is Inheritance?

**Inheritance** is a fundamental OOP concept that allows a class to inherit attributes and methods from another class. This promotes code reuse and creates hierarchical relationships between classes.

### Understanding Inheritance

- **Parent class** (base class, superclass) - The class being inherited from
- **Child class** (derived class, subclass) - The class that inherits
- Child classes **inherit** all attributes and methods from parent
- Child classes can **add** new attributes and methods
- Child classes can **override** parent methods to customize behavior
- Inheritance creates an "is-a" relationship (Dog is-a Animal)

### Why Use Inheritance?

✅ **Code reuse** - Don't repeat code, inherit from parent  
✅ **Organization** - Create logical hierarchies  
✅ **Maintainability** - Fix bugs in one place (parent class)  
✅ **Extensibility** - Add features without modifying parent  
✅ **Polymorphism** - Treat different objects uniformly  
✅ **Specialization** - Create specific versions of general concepts  

## 🌳 Basic Inheritance

### Creating a Parent Class

```python
# Parent class (base class)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        print(f"{self.name} makes a sound")
    
    def info(self):
        print(f"{self.name} is a {self.species}")

# Use parent class
animal = Animal("Generic", "Unknown")
animal.make_sound()  # Generic makes a sound
animal.info()        # Generic is a Unknown
```

### Creating a Child Class

```python
# Child class inherits from Animal
class Dog(Animal):
    pass

# Dog inherits everything from Animal
dog = Dog("Buddy", "Canis familiaris")
dog.make_sound()  # Buddy makes a sound
dog.info()        # Buddy is a Canis familiaris
```

### Child Class Syntax

```python
# Syntax: class ChildClass(ParentClass):
class Animal:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        print(f"{self.name} moves")

class Dog(Animal):      # Dog inherits from Animal
    pass

class Cat(Animal):      # Cat inherits from Animal
    pass

class Bird(Animal):     # Bird inherits from Animal
    pass

# All child classes inherit move() method
dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Tweety")

dog.move()   # Buddy moves
cat.move()   # Whiskers moves
bird.move()  # Tweety moves
```

## 🎯 Extending Child Classes

### Adding New Methods

```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")

# Child class with additional methods
class Dog(Animal):
    def bark(self):
        """New method - only Dog has this"""
        print(f"{self.name} says Woof!")
    
    def fetch(self):
        """Another new method"""
        print(f"{self.name} fetches the ball")

dog = Dog("Buddy")
dog.eat()     # Inherited from Animal
dog.bark()    # New method in Dog
dog.fetch()   # New method in Dog
```

### Adding New Attributes

```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

# Child class with additional attributes
class Dog(Animal):
    def __init__(self, name, breed):
        self.name = name           # Set inherited attribute
        self.breed = breed         # New attribute

dog = Dog("Buddy", "Golden Retriever")
print(dog.name)    # Buddy (from Animal)
print(dog.breed)   # Golden Retriever (new in Dog)
```

## 🔄 Method Overriding

### What is Method Overriding?

**Overriding** means defining a method in a child class that already exists in the parent class. The child's version replaces the parent's version.

```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print(f"{self.name} makes a generic sound")

# Child class overrides make_sound
class Dog(Animal):
    def make_sound(self):
        """Override parent method"""
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def make_sound(self):
        """Override parent method"""
        print(f"{self.name} says Meow!")

# Each child has its own version
dog = Dog("Buddy")
cat = Cat("Whiskers")
animal = Animal("Generic")

dog.make_sound()     # Buddy says Woof!
cat.make_sound()     # Whiskers says Meow!
animal.make_sound()  # Generic makes a generic sound
```

### Why Override Methods?

```python
# Parent class with generic behavior
class Shape:
    def __init__(self, name):
        self.name = name
    
    def area(self):
        """Generic area method"""
        return 0

# Each child overrides area() with specific calculation
class Rectangle(Shape):
    def __init__(self, width, height):
        self.name = "Rectangle"
        self.width = width
        self.height = height
    
    def area(self):
        """Rectangle-specific area"""
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.name = "Circle"
        self.radius = radius
    
    def area(self):
        """Circle-specific area"""
        return 3.14159 * self.radius ** 2

# Each shape calculates area differently
rect = Rectangle(5, 10)
circle = Circle(7)

print(f"{rect.name} area: {rect.area()}")      # 50
print(f"{circle.name} area: {circle.area()}")  # 153.93791
```

### Overriding __init__

```python
# Parent __init__
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print(f"Vehicle created: {brand} {model}")

# Child overrides __init__ to add attributes
class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        # Must initialize parent attributes
        self.brand = brand
        self.model = model
        self.num_doors = num_doors  # New attribute
        print(f"Car created with {num_doors} doors")

car = Car("Toyota", "Camry", 4)
print(f"{car.brand} {car.model} has {car.num_doors} doors")
```

## 🔗 The super() Function

### What is super()?

`super()` lets you call methods from the parent class, especially useful when overriding `__init__`.

```python
# Using super() in __init__
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print(f"Vehicle initialized: {brand} {model}")

class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        # Call parent __init__ with super()
        super().__init__(brand, model)
        self.num_doors = num_doors
        print(f"Car initialized with {num_doors} doors")

car = Car("Toyota", "Camry", 4)
# Output:
# Vehicle initialized: Toyota Camry
# Car initialized with 4 doors
```

### super() with Methods

```python
# Using super() in regular methods
class Animal:
    def __init__(self, name):
        self.name = name
    
    def info(self):
        print(f"Name: {self.name}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def info(self):
        # Call parent's info() first
        super().info()
        # Then add child-specific info
        print(f"Breed: {self.breed}")

dog = Dog("Buddy", "Golden Retriever")
dog.info()
# Output:
# Name: Buddy
# Breed: Golden Retriever
```

### Why Use super()?

```python
# Without super() - repetitive
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        self.brand = brand       # Repeat parent code
        self.model = model       # Repeat parent code
        self.year = year         # Repeat parent code
        self.num_doors = num_doors

# With super() - clean and maintainable
class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)  # Call parent
        self.num_doors = num_doors            # Add new attribute
```

### Extending Parent Methods

```python
# Extend parent method behavior
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, I'm {self.name}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def greet(self):
        # Call parent greet() first
        super().greet()
        # Add student-specific greeting
        print(f"My student ID is {self.student_id}")

student = Student("Alice", 20, "S12345")
student.greet()
# Output:
# Hello, I'm Alice
# My student ID is S12345
```

## 🎭 Multiple Inheritance

### What is Multiple Inheritance?

A class can inherit from multiple parent classes, combining their features.

```python
# Multiple parent classes
class Flyer:
    def fly(self):
        print("Flying in the air")

class Swimmer:
    def swim(self):
        print("Swimming in water")

# Child inherits from both
class Duck(Flyer, Swimmer):
    def quack(self):
        print("Quack!")

duck = Duck()
duck.fly()    # From Flyer
duck.swim()   # From Swimmer
duck.quack()  # From Duck
```

### Multiple Inheritance Syntax

```python
# Syntax: class Child(Parent1, Parent2, Parent3):
class Walker:
    def walk(self):
        print("Walking on land")

class Flyer:
    def fly(self):
        print("Flying in air")

class Swimmer:
    def swim(self):
        print("Swimming in water")

# Inherits from all three
class SuperAnimal(Walker, Flyer, Swimmer):
    def do_everything(self):
        self.walk()
        self.fly()
        self.swim()

animal = SuperAnimal()
animal.do_everything()
```

### Method Resolution Order (MRO)

```python
# When multiple parents have same method, which is called?
class Parent1:
    def greet(self):
        print("Hello from Parent1")

class Parent2:
    def greet(self):
        print("Hello from Parent2")

class Child(Parent1, Parent2):
    pass

child = Child()
child.greet()  # Hello from Parent1 (first parent in list)

# Check method resolution order
print(Child.__mro__)
# (<class 'Child'>, <class 'Parent1'>, <class 'Parent2'>, <class 'object'>)
```

### Practical Multiple Inheritance

```python
# Mixins - small classes that add specific functionality
class TimestampMixin:
    """Add timestamp functionality to any class"""
    def __init__(self):
        from datetime import datetime
        self.created_at = datetime.now()
    
    def get_age(self):
        from datetime import datetime
        age = datetime.now() - self.created_at
        return age.total_seconds()

class IdMixin:
    """Add ID functionality to any class"""
    _next_id = 1
    
    def __init__(self):
        self.id = IdMixin._next_id
        IdMixin._next_id += 1

class User(TimestampMixin, IdMixin):
    def __init__(self, name):
        TimestampMixin.__init__(self)
        IdMixin.__init__(self)
        self.name = name
    
    def __str__(self):
        return f"User(id={self.id}, name={self.name})"

user1 = User("Alice")
user2 = User("Bob")

print(user1)  # User(id=1, name=Alice)
print(user2)  # User(id=2, name=Bob)
print(f"User1 age: {user1.get_age():.2f} seconds")
```

## 🏗️ Inheritance Hierarchies

### Multi-Level Inheritance

```python
# Grandparent -> Parent -> Child
class Animal:
    def __init__(self, name):
        self.name = name
    
    def breathe(self):
        print(f"{self.name} breathes")

class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.warm_blooded = True
    
    def feed_milk(self):
        print(f"{self.name} feeds milk to babies")

class Dog(Mammal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} barks")

dog = Dog("Buddy", "Golden Retriever")
dog.breathe()    # From Animal (grandparent)
dog.feed_milk()  # From Mammal (parent)
dog.bark()       # From Dog (itself)
```

### Complex Hierarchies

```python
# Multiple children from same parent
class Shape:
    def __init__(self, color):
        self.color = color
    
    def describe(self):
        print(f"A {self.color} shape")

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

class Triangle(Shape):
    def __init__(self, color, base, height):
        super().__init__(color)
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

# All are shapes, but each calculates area differently
shapes = [
    Rectangle("red", 5, 10),
    Circle("blue", 7),
    Triangle("green", 6, 8)
]

for shape in shapes:
    shape.describe()
    print(f"Area: {shape.area()}\n")
```

## 🔍 Checking Inheritance

### isinstance() and issubclass()

```python
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
cat = Cat()
animal = Animal()

# isinstance() - check if object is instance of class
print(isinstance(dog, Dog))      # True
print(isinstance(dog, Animal))   # True (Dog inherits from Animal)
print(isinstance(dog, Cat))      # False

# issubclass() - check if class inherits from another
print(issubclass(Dog, Animal))   # True
print(issubclass(Cat, Animal))   # True
print(issubclass(Dog, Cat))      # False
print(issubclass(Animal, object))  # True (all classes inherit from object)
```

### type() with Inheritance

```python
class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()

# type() returns exact class
print(type(dog))           # <class 'Dog'>
print(type(dog) == Dog)    # True
print(type(dog) == Animal) # False (type is Dog, not Animal)

# isinstance() checks inheritance chain
print(isinstance(dog, Dog))    # True
print(isinstance(dog, Animal)) # True
```

## 🎯 Common Inheritance Patterns

### Template Pattern

```python
# Parent defines structure, children implement details
class DataProcessor:
    def process(self, data):
        """Template method - defines the steps"""
        self.load(data)
        self.validate()
        self.transform()
        self.save()
    
    def load(self, data):
        print(f"Loading data: {data}")
        self.data = data
    
    def validate(self):
        """Override in child class"""
        pass
    
    def transform(self):
        """Override in child class"""
        pass
    
    def save(self):
        """Override in child class"""
        pass

class CSVProcessor(DataProcessor):
    def validate(self):
        print("Validating CSV format")
    
    def transform(self):
        print("Transforming CSV data")
        self.data = self.data.upper()
    
    def save(self):
        print(f"Saving CSV: {self.data}")

processor = CSVProcessor()
processor.process("csv,data,here")
```

### Is-A Relationship

```python
# Use inheritance when there's an "is-a" relationship
# Dog is-a Animal ✅
# Car is-a Vehicle ✅
# Student is-a Person ✅

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        print(f"{self.brand} vehicle starting")

class Car(Vehicle):  # Car is-a Vehicle
    def __init__(self, brand, num_doors):
        super().__init__(brand)
        self.num_doors = num_doors

class Motorcycle(Vehicle):  # Motorcycle is-a Vehicle
    def __init__(self, brand, engine_size):
        super().__init__(brand)
        self.engine_size = engine_size

# Both are vehicles
car = Car("Toyota", 4)
motorcycle = Motorcycle("Harley", 1200)

car.start()         # Toyota vehicle starting
motorcycle.start()  # Harley vehicle starting
```

## 📚 Mini-Programs in This Folder

Apply these concepts in the following programs:

1. **01_inheritance.py** - Basic inheritance
   - Create parent and child classes
   - Inherit attributes and methods from parent
   - Understand inheritance syntax
   - Create multiple children from same parent
   - Use inherited methods in child classes
   - Verify inheritance with isinstance()

2. **02_method_overriding.py** - Override parent methods
   - Override methods in child classes
   - Customize inherited behavior
   - Create specialized implementations
   - Understand when and why to override
   - Compare parent and child method behavior
   - Override `__str__` and `__init__`

3. **03_super_function.py** - Using super()
   - Call parent class methods with super()
   - Extend parent `__init__` in child classes
   - Add child attributes while preserving parent
   - Extend parent method behavior
   - Understand super() in multi-level inheritance
   - Use super() for cleaner, maintainable code

4. **04_multiple_inheritance.py** - Multiple inheritance
   - Inherit from multiple parent classes
   - Combine functionality from different sources
   - Understand method resolution order (MRO)
   - Use mixins to add functionality
   - Check MRO with `__mro__` attribute
   - Handle conflicts in multiple inheritance

## 💡 Quick Tips

✅ **Best Practices:**
- Use inheritance for "is-a" relationships
- Keep inheritance hierarchies shallow (2-3 levels max)
- Use super() instead of calling parent directly
- Override `__init__` with super().__init__() call
- Document inheritance relationships
- Prefer composition over inheritance when not "is-a"
- Use isinstance() instead of type() for checking types

❌ **Common Mistakes:**
- Forgetting to call super().__init__() in child __init__
- Using inheritance for "has-a" relationships (use composition)
- Deep inheritance hierarchies (hard to maintain)
- Not understanding method resolution order
- Overriding methods without good reason
- Multiple inheritance without understanding MRO
- Trying to inherit from built-in types incorrectly

## 🎓 Key Takeaways

1. **Inheritance** allows classes to reuse code from parent classes
2. **Child classes** inherit all attributes and methods from parents
3. **Method overriding** lets children customize parent behavior
4. **super()** calls parent class methods, especially in `__init__`
5. **Multiple inheritance** allows inheriting from multiple parents
6. **MRO** determines which method is called in multiple inheritance
7. Use inheritance for **"is-a"** relationships
8. **isinstance()** checks if object is instance of class (includes inheritance)
9. Keep inheritance hierarchies **simple** and **shallow**
10. Override methods to **specialize** behavior for child classes

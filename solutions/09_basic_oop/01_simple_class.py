"""Reference solution for Mini-Program 1: Simple Class."""


class Dog:
    """A simple class whose attributes can be added to each instance."""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


if __name__ == "__main__":
    my_dog = Dog()
    my_dog.name, my_dog.age, my_dog.breed = "Buddy", 3, "Golden Retriever"
    another_dog = Dog()
    another_dog.name, another_dog.age, another_dog.breed = "Max", 5, "Labrador"
    person1 = Person("Alex", 16)
    book1 = Book("Python Basics", "Ada Lee", 240)
    book2 = Book("Learning Objects", "Sam Kim", 180)
    book1.pages = 250
    print(my_dog.name, my_dog.age, my_dog.breed)
    print(my_dog.name, another_dog.name)
    print(person1.name, person1.age)
    print(book1.title, book2.title, book1.pages)

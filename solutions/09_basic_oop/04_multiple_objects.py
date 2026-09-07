"""Reference solution for Mini-Program 4: Working with Multiple Objects."""


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_value(self):
        return self.price * self.quantity

    def display_info(self):
        print(f"{self.name}: ${self.price:.2f}, quantity {self.quantity}")


class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = list(grades)

    def calculate_average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def add_grade(self, grade):
        self.grades.append(grade)


class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def checkout_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                return True
        return False


if __name__ == "__main__":
    inventory = [
        Product("Laptop", 999.99, 5),
        Product("Mouse", 25.00, 10),
        Product("Keyboard", 60.00, 4),
    ]
    for product in inventory:
        product.display_info()
    print(f"Grand total: ${sum(product.get_total_value() for product in inventory):.2f}")

    students = [
        Student("Avery", 16, [90, 85, 95]),
        Student("Jordan", 17, [88, 92, 84]),
        Student("Casey", 16, [95, 98, 94]),
    ]
    for student in students:
        print(student.name, student.calculate_average())
    print("Highest average:", max(students, key=Student.calculate_average).name)

"""Reference solution for Mini-Program 5: Object Composition and Aggregation."""


class Address:
    def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def get_full_address(self):
        return f"{self.street}, {self.city}, {self.state} {self.zip_code}"


class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def get_info(self):
        return f"{self.name}, age {self.age}: {self.address.get_full_address()}"


class Course:
    def __init__(self, course_code, name, credits, professor=None):
        self.course_code = course_code
        self.code = course_code
        self.name = name
        self.credits = credits
        self.professor = professor
        self.enrolled_students = []

    def get_course_info(self):
        return f"{self.course_code}: {self.name} ({self.credits} credits)"

    def assign_professor(self, professor):
        self.professor = professor

    def enroll_student(self, student):
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)


class Student:
    def __init__(self, name, student_id, courses=None, major_department=None):
        self.name = name
        self.student_id = student_id
        self.courses = list(courses or [])
        self.enrolled_courses = self.courses
        self.major_department = major_department

    def add_course(self, course):
        self.courses.append(course)

    def enroll_course(self, course):
        if course not in self.courses:
            self.add_course(course)
            course.enroll_student(self)

    def drop_course(self, course_code):
        for course in self.courses:
            if course.course_code == course_code:
                self.courses.remove(course)
                return True
        return False

    def get_total_credits(self):
        return sum(course.credits for course in self.courses)

    def list_courses(self):
        return [course.get_course_info() for course in self.courses]


class Engine:
    def __init__(self, horsepower, fuel_type):
        self.horsepower = horsepower
        self.fuel_type = fuel_type
        self.running = False

    def start(self):
        self.running = True
        return "Engine started"

    def stop(self):
        self.running = False
        return "Engine stopped"

    def get_info(self):
        return f"{self.horsepower} hp {self.fuel_type} engine"


class Car:
    def __init__(self, make, model, year, engine):
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine

    def start_car(self):
        return self.engine.start()

    def stop_car(self):
        return self.engine.stop()

    def get_car_info(self):
        return f"{self.year} {self.make} {self.model} with {self.engine.get_info()}"


class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def checkout(self):
        if not self.available:
            return False
        self.available = False
        return True

    def return_book(self):
        self.available = True
        return True

    def get_info(self):
        status = "available" if self.available else "checked out"
        return f"{self.title} by {self.author} ({self.isbn}) is {status}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book_by_title(self, title):
        return next((book for book in self.books if book.title == title), None)

    def checkout_book(self, isbn):
        book = next((book for book in self.books if book.isbn == isbn), None)
        return book.checkout() if book else False

    def return_book(self, isbn):
        book = next((book for book in self.books if book.isbn == isbn), None)
        return book.return_book() if book else False

    def list_available_books(self):
        return [book for book in self.books if book.available]


class BankAccount:
    def __init__(self, account_number, balance, account_type):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            return False
        self.balance -= amount
        return True

    def get_balance(self):
        return self.balance


class Customer:
    def __init__(self, name, customer_id, accounts=None):
        self.name = name
        self.customer_id = customer_id
        self.accounts = list(accounts or [])

    def add_account(self, account):
        self.accounts.append(account)

    def get_total_balance(self):
        return sum(account.get_balance() for account in self.accounts)

    def transfer(self, from_account_num, to_account_num, amount):
        source = next((a for a in self.accounts if a.account_number == from_account_num), None)
        target = next((a for a in self.accounts if a.account_number == to_account_num), None)
        if source is None or target is None or not source.withdraw(amount):
            return False
        target.deposit(amount)
        return True

    def list_accounts(self):
        return list(self.accounts)


class Room:
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width


class House:
    def __init__(self, address, rooms=None):
        self.address = address
        self.rooms = list(rooms or [])

    def add_room(self, room):
        self.rooms.append(room)

    def get_total_area(self):
        return sum(room.get_area() for room in self.rooms)

    def count_rooms(self):
        return len(self.rooms)

    def list_rooms(self):
        return [room.name for room in self.rooms]


class Department:
    def __init__(self, name, code, courses=None):
        self.name = name
        self.code = code
        self.courses = list(courses or [])

    def add_course(self, course):
        self.courses.append(course)

    def list_courses(self):
        return [course.get_course_info() for course in self.courses]


class Professor:
    def __init__(self, name, employee_id, department):
        self.name = name
        self.employee_id = employee_id
        self.department = department

    def assign_to(self, course):
        course.assign_professor(self)


def find_students_by_major(students, department):
    """Return students whose major is the given Department object."""

    return [student for student in students if student.major_department is department]


if __name__ == "__main__":
    address = Address("1 Main Street", "Springfield", "IL", "62701")
    student = Student("Avery", "S100")
    student.add_course(Course("CS101", "Python", 3))
    engine = Engine(180, "gasoline")
    car = Car("Toyota", "Corolla", 2024, engine)
    print(Person("Avery", 16, address).get_info())
    print(student.get_total_credits(), student.list_courses())
    print(car.start_car(), car.get_car_info(), car.stop_car())

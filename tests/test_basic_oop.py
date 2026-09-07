"""Tests for basic OOP reference solutions."""

import unittest

from solution_loader import load_solution


class BasicOOPTests(unittest.TestCase):
    def test_simple_class(self):
        lesson = load_solution("09_basic_oop", "01_simple_class.py")
        dog = lesson.Dog()
        dog.name = "Buddy"
        self.assertEqual(dog.name, "Buddy")
        self.assertEqual(lesson.Person("Avery", 16).age, 16)
        book = lesson.Book("Title", "Author", 100)
        book.pages = 120
        self.assertEqual(book.pages, 120)

    def test_class_attributes(self):
        lesson = load_solution("09_basic_oop", "02_class_attributes.py")
        self.assertEqual(lesson.Car("Toyota", "Camry").wheels, 4)
        account = lesson.BankAccount("Avery", 25)
        self.assertEqual(account.bank_name, "Python Bank")
        lesson.Student("Avery", 11)
        lesson.Student("Jordan", 12)
        self.assertEqual(lesson.Student.total_students, 2)
        lesson.InstanceTracker()
        self.assertEqual(lesson.InstanceTracker.total_instances, 1)

    def test_class_methods(self):
        lesson = load_solution("09_basic_oop", "03_class_methods.py")
        calculator = lesson.Calculator()
        calculator.add(10)
        calculator.subtract(3)
        self.assertEqual(calculator.get_result(), 7)
        self.assertAlmostEqual(lesson.Circle(5).calculate_area(), 78.53975)
        self.assertEqual(lesson.Rectangle(4, 6).calculate_perimeter(), 20)
        counter = lesson.Counter()
        counter.increment()
        counter.reset()
        self.assertEqual(counter.get_count(), 0)
        self.assertEqual(lesson.Temperature(0).to_kelvin(), 273.15)

    def test_multiple_objects(self):
        lesson = load_solution("09_basic_oop", "04_multiple_objects.py")
        self.assertEqual(lesson.Product("Book", 12.5, 3).get_total_value(), 37.5)
        student = lesson.Student("Avery", 16, [80, 100])
        student.add_grade(90)
        self.assertEqual(student.calculate_average(), 90)
        library = lesson.Library()
        library.add_book(lesson.Book("Python", "Ada"))
        self.assertTrue(library.checkout_book("Python"))
        self.assertFalse(library.checkout_book("Python"))

    def test_composition_aggregation(self):
        lesson = load_solution("09_basic_oop", "05_composition_aggregation.py")
        address = lesson.Address("1 Main St", "Springfield", "IL", "62701")
        self.assertEqual(address.get_full_address(), "1 Main St, Springfield, IL 62701")
        student = lesson.Student("Avery", "S1")
        student.add_course(lesson.Course("CS1", "Python", 3))
        self.assertEqual(student.get_total_credits(), 3)
        engine = lesson.Engine(180, "gasoline")
        car = lesson.Car("Toyota", "Corolla", 2024, engine)
        self.assertEqual(car.start_car(), "Engine started")
        self.assertTrue(engine.running)
        library = lesson.Library("School")
        book = lesson.Book("Python", "Ada", "123")
        library.add_book(book)
        self.assertTrue(library.checkout_book("123"))
        self.assertFalse(book.available)
        customer = lesson.Customer("Avery", "C1")
        customer.add_account(lesson.BankAccount("1", 100, "checking"))
        customer.add_account(lesson.BankAccount("2", 20, "savings"))
        self.assertTrue(customer.transfer("1", "2", 25))
        self.assertEqual(customer.get_total_balance(), 120)
        house = lesson.House(address, [lesson.Room("Kitchen", 10, 12)])
        self.assertEqual((house.count_rooms(), house.get_total_area()), (1, 120))
        department = lesson.Department("Science", "SCI")
        professor = lesson.Professor("Ada", "P1", department)
        course = lesson.Course("CS2", "Objects", 3)
        department.add_course(course)
        professor.assign_to(course)
        student = lesson.Student("Jordan", "S2", major_department=department)
        student.enroll_course(course)
        self.assertEqual(lesson.find_students_by_major([student], department), [student])
        self.assertIs(course.professor, professor)
